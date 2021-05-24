import model
import cache
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components 

from PIL import Image

def home(sample):
    st.title('Home')

    model_type = sample['Model'].lower().replace(" ", "_")
    del sample['Model']

    st.header("Sample Attributes")
    columns = ["Time of Day", "Temperature (C)", "Humidity (%)", "Wind speed (m/s)", "Visibility (10m)",
                "Rainfall (mm)", "Snowfall (cm)", "Day of Week", "Holiday", "Functioning Day", "Season"]
    st.write(pd.DataFrame([sample.values()], columns=columns))

    st.header("Prediction")
    pred = model.predict_bike_count(sample, model_type)
    st.write(pred)

    st.header("Model Comparisons")
    st.markdown(r"""
        | Model             | R^2   | Grid Search | R^2 + Grid Search |
        | :---              |  ---: | :---        |              ---: |
        | SVM               | 0.799 | Yes         | 0.898             |
        | Linear Regression | 0.531 | No          | N/A               |
        | Gradient Boosting | 0.835 | Yes         | 0.928             |
        | Random Forest     | 0.908 | Yes         | 0.91              |
    """)

    st.header('Dataset')
    st.write(cache.dataset())

    # st.header('Heatmap')
    # st.pyplot(cache.heatmap())


def data_visualization():
    st.title('Data Visualization')

    st.subheader('Average Bike Rental Per Week')
    st.write("Figure 1. This graph shows the link between temperature and average bike rentals per week. The general trend we see is that as the weather becomes warm, bike rentals go up until it reaches a point at which it becomes too warm.")
    figure1 = r"""<div class='tableauPlaceholder' id='viz1621818186711' style='position: relative'><noscript><a href='#'><img alt='Average bike rental per week color coded by temperature. ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;HeatMap&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Weather_16218177883130&#47;HeatMap' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;HeatMap&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1621818186711');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""    
    components.html(figure1, height=600)

    st.subheader('Bike Rentals by Day')
    st.write("Figure 2. This graph depicts the average number of bikes rented per hour segmented out by day of the week. What we can learn from this data is that there are clear spikes during commute times on weekdays as well as a gradual trend upward as the day goes on.")
    figure2 = r"""<div class='tableauPlaceholder' id='viz1621817840209' style='position: relative'><noscript><a href='#'><img alt='Bike Rentals by Day ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;BikeRentalsbyDay&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Weather_16218177883130&#47;BikeRentalsbyDay' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;BikeRentalsbyDay&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1621817840209');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(figure2, height=600)


    st.subheader('Average Monthly Bike Usage')
    st.write("Figure 3. In this chart we see the negative correlation between average bike count and snowfall.")
    figure3 = r"""<div class='tableauPlaceholder' id='viz1621818382036' style='position: relative'><noscript><a href='#'><img alt='Average monthly bike usage with snowfall coloration ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;MonthlyPlotSnow&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Weather_16218177883130&#47;MonthlyPlotSnow' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;MonthlyPlotSnow&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1621818382036');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(figure3, height=600)

    st.subheader("Humidity Across Time.")
    st.write("Figure 4. This graph shows a lot of the relations between weather data. Humidity and rain correlate very highly and it appears that there is more rainfall in the summer months.")
    figure4 = r"""<div class='tableauPlaceholder' id='viz1621818921009' style='position: relative'><noscript><a href='#'><img alt='Humidity across time with rainfall (size) and temperature (color) data. ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;HumidityvsRainfall&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Weather_16218177883130&#47;HumidityvsRainfall' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;HumidityvsRainfall&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1621818921009');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(figure4, height=600)

    st.subheader("Average Bike Rental vs. Rain & Humidity")
    st.write("Figure 5. These two charts show the dips in bike usage at the times when rainfall and humidity spike.")
    figure5 = r"""<div class='tableauPlaceholder' id='viz1621819397503' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Weather_16218177883130&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;We&#47;Weather_16218177883130&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1621819397503');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(figure5, height=1000)


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

    we = Image.open(f'{dir}/albert.jpg')
    col1.image(we, caption='Albert Stanley')
    col1.write("I am a junior at UC Davis studying Computer Science. I chose my major because I enjoyed the problem solving nature of work in computer science, and I want to work within the machine learning field since it has brought about many of the interesting technologies we have today. I helped with data cleaning, training the linear regression model and training time series models.")

    bare = Image.open(f'{dir}/bears.jpg')
    col2.image(bare, caption='Jordan Stefani')
    col2.write("")
