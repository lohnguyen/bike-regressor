import streamlit as st


def navigation():
    menu = ["Home", "Data Visualization", "About Us"]
    return st.sidebar.selectbox("Navigation", menu)


def header(content):
    st.sidebar.markdown(f'## {content}')


def home():
    header("Sample Attributes")
    temperature = st.sidebar.slider("Temperature (C):", 0.0, 3.0, 0.7, 0.1)
    humidity = st.sidebar.slider("Humidity (%):", 0, 50, 40)
    wind_speed = st.sidebar.slider("Wind speed (m/s):", 0.0, 1.0, 0.9, 0.05)
    visibility = st.sidebar.slider("Visibility (10m):", 0, 6, 2)
    return temperature, humidity, wind_speed, visibility


def data_visualization():
    st.sidebar.slider("Zoom (%):", 0, 100, 50)


def about_us():
    st.sidebar.slider("Howdy:", 0, 100, 50)
