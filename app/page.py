import model
import cache
import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image

def home(sample):
    st.title('Home')

    model_type = sample['Model'].lower().replace(" ", "_")
    del sample['Model']

    st.header("Sample Attributes")
    st.write(sample)

    st.header("Prediction")
    pred = model.predict_bike_count(sample, model_type)
    st.write(pred)


def data_visualization():
    st.title('Data Visualization')

    st.header('Dataset')
    st.write(cache.dataset())

    st.header('Heatmap')
    st.pyplot(cache.heatmap())

    st.header('Charts')
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
    st.area_chart(chart_data)


def report():
    st.title('Report')

    st.markdown('''
    ## This is the document title

    This is some _markdown_.
    ''')

    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


def about_us():
    st.title('Group 7')

    col1, col2 = st.beta_columns(2)
    dir = 'app/static'

    we = Image.open(f'{dir}/sonya.jpg')
    col1.image(we, caption='Sonya Gomez')
    col1.write("Hello, my name is Sonya Gomez. I am a CS Major at UC Davis, currently a Junior. I chose CS as my major because being a CS major will give me the freedom to work anywhere under any company I support the values of. In this project, I contributed in the writing aspect and also had a small role within the software team.")

    bare = Image.open(f'{dir}/mack.jpg')
    col2.image(bare, caption='Mack Gregory')
    col2.write("Hello, I am Mack Gregory. I am a third year Computer Science student at UC Davis. I love studying computer science as a way of being able to make sense of the world around me through data, and programmatically making tasks easier and safer. I hope to take the knowledge from UC Davis into a career in computer security protecting people from breaches of their private data, while ensuring that we can still have progress in modern technology. In this project I helped with writing, data analysis and data exploration.")

    we = Image.open(f'{dir}/joshua.jpg')
    col1.image(we, caption='Joshua Guillen')
    col1.write("My name is Joshua Guillen. I am a senior at UC Davis majoring in Cognitive Science with an emphasis in computation. I chose this major because it allowed me to combine my interest in the human mind through other disciplines besides psychology such as computer science, artificial intelligence, linguistics, philosophy, and neuroscience. I hope my major allows me to work on artificial intelligence such as developing more convincing chatbots. For this project, I was the project leader tasked with facilitating communication between my group members while keeping them on track with our tasks and deadlines. I also helped with data exploration/visualization, and video creation.")

    bare = Image.open(f'{dir}/bryce.jpg')
    col2.image(bare, caption='Bryce Joseph-Nelson')
    col2.write("Hi, I am Bryce Joseph-Nelson. I am a Cognitive Science senior at UC Davis specializing in computation. I chose this major because the field fascinates me, but my end goal is to use this technical background to assist in my goal of going into marketing for highly technical startups. I’ve worked with a number of biotech companies and see a huge need for being able to communicate complicated information easily through mediums such as video. [Through this project, I worked with some preliminary data exploration and assisted in various aspects of the web app. --- role unsure]")

    we = Image.open(f'{dir}/malini.jpg')
    col1.image(we, caption='Malini Manimaran')
    col1.write("Hello, I’m Malini Manimaran. I am a junior at UC Davis with a triple major in Cognitive Science, Math, and Political Science. I became really interested in these three topics because of the intersection of governance and scientific data. I hope to work on developing artificial intelligence that will better inform politicians about their constituencies. For this project, I worked on the initial data exploration/analysis, visualization, and report write up.")

    bare = Image.open(f'{dir}/we.jpg')
    col2.image(bare, caption='Devon Mirsalis')
    col2.write("")

    we = Image.open(f'{dir}/charles.jpg')
    col1.image(we, caption='Charles Nguyen')
    col1.write("I am a Computer Science senior at UC Davis. I am passionate about improving people's lives with technology and interested in STEM education, healthcare, and user privacy. For this project, I was in charge of developing the web application using Streamlit. I also implemented a deep neural network to compare with other models.")

    bare = Image.open(f'{dir}/bare.jpg')
    col2.image(bare, caption='Gabriel Raulet')
    col2.write("")

    we = Image.open(f'{dir}/bears.jpg')
    col1.image(we, caption='Albert Stanley')
    col1.write("I am a junior at UC Davis studying Computer Science. I chose my major because I enjoyed the problem solving nature of work in computer science, and I want to work within the machine learning field since it has brought about many of the interesting technologies we have today. I helped with data cleaning, training the linear regression model and training time series models.")

    bare = Image.open(f'{dir}/we.jpg')
    col2.image(bare, caption='Jordan Stefani')
    col2.write("")
