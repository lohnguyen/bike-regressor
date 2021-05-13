import pandas as pd
import seaborn as sb
import streamlit as st
import matplotlib.pyplot as plt


# @st.cache
def heatmap():
    df = dataset()
    fig, ax = plt.subplots(figsize=(20, 15))
    sb.heatmap(df.corr(), fmt='.2f', annot=True, ax=ax)
    return fig


@st.cache
def dataset():
    return pd.read_csv('machine_learning/datasets/raw_data.csv', encoding='unicode_escape')

