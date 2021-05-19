import streamlit as st


def navigation():
    menu = ["Home", "Data Visualization", "Report", "About Us"]
    return st.sidebar.selectbox("Navigation", menu)


def header(content):
    st.sidebar.markdown(f'## {content}')


def home():
    header("Sample Attributes")

    num_rentals = st.sidebar.slider("Rental count (bike):", 0, 1000, 100, 5)
    duration = st.sidebar.slider("Hour (hours):", 0, 10, 5, 1)
    temperature = st.sidebar.slider("Temperature (C):", -30.0, 60.0, 25.0, 1.0)
    humidity = st.sidebar.slider("Humidity (%):", 20, 50, 1)
    wind_speed = st.sidebar.slider("Wind speed (m/s):", 0.0, 10.0, 2.0, 0.1)
    visibility = st.sidebar.slider("Visibility (10m):", 1000, 2000, 1500, 1)
    dew_point_temp = st.sidebar.slider("Dew Point Temperature (C):", -30.0, 60.0, 25.0, 1.0)
    solar_radiation = st.sidebar.slider("Solar Radiation (MJ/m2):", 0.0, 1.0, 0.5, 0.01)
    rainfall = st.sidebar.slider("Rainfall (mm):", 0.0, 1.0, 0.5, 0.1)
    snowfall = st.sidebar.slider("Snowfall (cm):", 0.0, 1.0, 0.5, 0.1)
    season = st.sidebar.radio("Season:", ("Spring", "Summer", "Fall", "Winter"))
    holiday = st.sidebar.radio("Holiday:", ("Yes", "No"))
    functioning_day = st.sidebar.radio("Functioning Day:", ("Yes", "No"))

    return (num_rentals, duration, temperature, humidity, wind_speed, visibility, dew_point_temp, 
            solar_radiation, rainfall, snowfall, season, holiday, functioning_day)


def data_visualization():
    pass


def report():
    pass


def about_us():
    pass
