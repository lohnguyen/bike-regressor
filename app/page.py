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

    col1, col2, col3 = st.beta_columns(3)
    dir = 'app/static'

    we = Image.open(f'{dir}/we.jpg')
    col1.image(we, caption='We')
    col1.write("I'm We.")

    bare = Image.open(f'{dir}/bare.jpg')
    col2.image(bare, caption='Bare')
    col2.write("I'm Bare.")

    bears = Image.open(f'{dir}/bears.jpg')
    col3.image(bears, caption='Bears')
    col3.write("I'm Bears.")

