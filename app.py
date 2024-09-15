from flask import Flask, request, jsonify, render_template
from sklearn import preprocessing
import pickle
import numpy as np
import pandas as pd
import streamlit as st
import warnings


st.header("Resturant reccomendation System Using ML")

model = pickle.load(open('drr/res_model.pkl','rb'))
res_name =pickle.load(open('drr/res_name.pkl','rb'))
res_rating =pickle.load(open('drr/Data_per.pkl','rb'))
#url =pickle.load(open('drr/save_url.pkl','rb'))
indices =pickle.load(open('drr/indices.pkl','rb'))
df_percent= res_rating
 

warnings.filterwarnings('always')
warnings.filterwarnings('ignore')
def recommend_res(name,cosine_similarities):#,df_percent):
    recommend_restaurant = []
    #the index of hotel entered
    idx = indices[indices==name].index[0]
    #the restaurants with a similar cosine value and order these
    score_series=pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    # top 30 restaurants indexes with silmilar cosine sim value
    top30_indexes=list(score_series.iloc[0:31].index)

    #Name of the top 30 restaurants
    for each in top30_indexes:
        recommend_restaurant.append(list(df_percent.index)[each])

    #the new dataset to show similar restaurants
    df_new=pd.DataFrame(columns=['cuisines','Mean_Rating','cost'])
    #top30 similar restaurants with some of their column
    for each in recommend_restaurant:
        temp=pd.DataFrame(df_percent[['cuisines','Mean_Rating', 'cost']][df_percent.index == each].sample())
        df_new = pd.concat([df_new,temp])
        
    #drop the same named restaurants and list top10 by highest rating
    df_new=df_new.drop_duplicates(subset=['cuisines','Mean_Rating','cost'],keep=False)
    df_new=df_new.sort_values(by='Mean_Rating',ascending=False).head(10)

    
    #print('TOP %s RESTAURANTS LIKE %s WITH SIMILAR REVIEWS: ' % (str(len(df_new)), name))
    return df_new 

selected_resturant = st.selectbox("Type or select a Resturant",res_name ) 

if st.button ('Show Recommendation'):
    recommendation_res  = recommend_res(selected_resturant,model)#,res_rating)
    print(recommendation_res)
    

    st.write(recommendation_res)
    #col1, col2, col3, col4, col5 = st.columns(5)

    #with col1:
        #st.write(recommendation_res)
        #st.text(recommendation_res.iloc[0])
        #st.u(res_url[1])

    #with col2:
    #    st.text(recommendation_res['cuisines'])
        #st.text(recommendation_res.iloc[1])
        #st.u(res_url[2])

    #with col3:
    #    st.text(recommendation_res['Mean_Rating'])
        #st.text(recommendation_res.iloc[2])
        #st.u(res_url[3])

    #with col4:
    #    st.text(recommendation_res['cost'])
        #st.text(recommendation_res.iloc[3])
        #st.u(res_url[4])

    #with col5:
    #    st.text(recommendation_res.iloc[4])
        #st.u(res_url[5])
