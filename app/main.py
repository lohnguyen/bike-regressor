import page
import sidebar

import numpy as np
import pandas as pd
import streamlit as st


def home():
    features = sidebar.home()
    page.home(features)


def data_visualization():
    sidebar.data_visualization()
    page.data_visualization()


def about_us():
    sidebar.about_us()
    page.about_us()


if __name__ == "__main__":
    nav_option = sidebar.navigation()

    if nav_option == "Home": home()
    elif nav_option == "Data Visualization": data_visualization()
    elif nav_option == "About Us": about_us()


