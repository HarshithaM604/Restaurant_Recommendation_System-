from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description =f.read()

REPO_NAME = "RESTURANT_RECOMENDATION"
AUTHOR_USER_NAME= "Deepak"
SRC_REPO ="src"
LIST_OF_REQUIREMENTS =['streamlit','numpy','pandas','sklearn']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author= AUTHOR_USER_NAME,
    description="A resturant Reccomendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url=f"https://github.com/",
    author_email="deepakyalameli11@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS

)