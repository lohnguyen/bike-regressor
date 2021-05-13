import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image

def home(features):
    st.title('Home')

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

    st.write("Here's our first attempt at using data to create a table:")
    st.write(df)
    st.write(features)


def data_visualization():
    st.title('Data Visualization')

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


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
