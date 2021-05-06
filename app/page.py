import numpy as np
import pandas as pd
import streamlit as st

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


def about_us():
    st.title('About Us')
