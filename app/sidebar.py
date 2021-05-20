import streamlit as st


def navigation():
    menu = ["Home", "Data Visualization", "Report", "About Us"]
    return st.sidebar.selectbox("Navigation", menu)


def header(content):
    st.sidebar.markdown(f'## {content}')


def home():
    header("Sample Attributes")

    sample = {}
    sample['Model'] = st.sidebar.radio("Model:", ("Linear Regression", "Random Forest", "Gradient Boosting", "SVM"))
    sample['Hour'] = st.sidebar.slider("Hour (hours):", 0, 10, 5, 1)
    sample['Temp'] = st.sidebar.slider("Temperature (C):", -30.0, 60.0, 25.0, 1.0)
    sample['Hum'] = st.sidebar.slider("Humidity (%):", 20, 50, 1)
    sample['Wind'] = st.sidebar.slider("Wind speed (m/s):", 0.0, 10.0, 2.0, 0.1)
    sample['Visb'] = st.sidebar.slider("Visibility (10m):", 1000, 2000, 1500, 1)
    sample['Rainfall'] = st.sidebar.slider("Rainfall (mm):", 0.0, 1.0, 0.5, 0.1)
    sample['Snow'] = st.sidebar.slider("Snowfall (cm):", 0.0, 1.0, 0.5, 0.1)
    sample['DWeek'] = st.sidebar.radio("Day of Week:", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))
    sample['Holiday'] = st.sidebar.radio("Holiday:", ("Yes", "No"))
    sample['Fday'] = st.sidebar.radio("Functioning Day:", ("Yes", "No"))
    sample['Season'] = st.sidebar.radio("Season:", ("Spring", "Summer", "Autumn", "Winter"))

    return sample


def data_visualization():
    pass


def report():
    pass


def about_us():
    pass
