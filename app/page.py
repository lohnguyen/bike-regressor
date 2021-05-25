import model
import cache
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components 

from PIL import Image

def home(sample):
    html_title = r"""
        <div style="background.color:#333547; padding:.5em; margin-bottom:2em">
            <div style="text_align:center; font-size:30pt; color:white">
                <div>🤖</div>
                <div>Bike Prediction</div>
                <div>🚵🚵‍♂️🚵‍♀️</div>
            </div>
        </div>
    """
    st.markdown(html_title, unsafe_allow_html=True)
    st.markdown(r'''
                    Our Bike Prediction models allow you to gauge the demand for bikes for any time in Seoul. 
                    A prediction requires eleven attributes as the followings:

                    - Continuous: time of day, temperature, humidity, windspeed, visibility, rainfall, snowfall.
                    - Categorical: day of week, whether it is a holiday, season, and whether it is a business day.

                   ⬅️ To start, adjust the values for each attribute using the slidebar on the left.
                ''')

    st.header("Entered Values")
    model_type = sample['Model'].lower().replace(" ", "_")
    del sample['Model']
    columns = ["Time of Day", "Temperature (C)", "Humidity (%)", "Wind speed (m/s)", "Visibility (10m)",
                "Rainfall (mm)", "Snowfall (cm)", "Day of Week", "Holiday", "Functioning Day", "Season"]
    st.write(pd.DataFrame([sample.values()], columns=columns))

    st.header("Prediction")
    pred = model.predict_bike_count(sample, model_type)
    intensity = ''
    icon = ''
    if pred < 1185: 
        intensity = 'slightly'
        icon = '😅'
    if pred >= 1185 and pred < 2370: 
        intensity = 'moderately'
        icon = '🥳'
    elif pred >= 2370: 
        intensity = 'very'
        icon = '😱'
    st.markdown(f'''
                    > We predict that **{pred}** bikes will be demanded.

                    > It is going to be a *{intensity} busy* {icon} time to rent bikes in Seoul.
                ''')

    st.header('Which model to use?')
    st.write(r'''
                Here, we include 4 different models . 
                We recommend using Random Forests or Gradient Boosting as they are the most accurate and comparable to one another. 
                Support Vector Machine (SVM) is still accurate and trustworthy for a choice. 
                Linear Regression is not accurate, but if you are curious, feel free to compare the outcomes between this algorithm and the others.
            ''')

    st.header("Model Comparison")
    st.markdown(r"""
        | Model             | $R^2$ without Grid Search | $R^2$ with Grid Search |
        | :---              |                      ---: |                   ---: |
        | Random Forest     | 0.908                     | 0.910                  |
        | Gradient Boosting | 0.835                     | 0.928                  |
        | SVM               | 0.799                     | 0.898                  |
        | Linear Regression | 0.531                     | 0.538                  |
    """)

    st.header("Is this accurate for other places than Seoul?")
    st.write("""
                These predictions are only accurate for Seoul, South Korea. 
                As we can predict the bike rental patterns in Seoul with high accuracy, our models can be trained with similar datasets collected for other metropolitan areas or bike friendly universities.
            """)



def data_visualization():
    figures = cache.figures()

    st.header('Average Bike Rental Per Week')
    st.write("Figure 1. This graph shows the link between temperature and average bike rentals per week. The general trend we see is that as the weather becomes warm, bike rentals go up until it reaches a point at which it becomes too warm.")
    components.html(figures[0], height=600)

    st.header('Bike Rentals by Day')
    st.write("Figure 2. This graph depicts the average number of bikes rented per hour segmented out by day of the week. What we can learn from this data is that there are clear spikes during commute times on weekdays as well as a gradual trend upward as the day goes on.")
    components.html(figures[1], height=600)


    st.header('Average Monthly Bike Usage')
    st.write("Figure 3. In this chart we see the negative correlation between average bike count and snowfall.")
    components.html(figures[2], height=600)

    st.header("Humidity Across Time.")
    st.write("Figure 4. This graph shows a lot of the relations between weather data. Humidity and rain correlate very highly and it appears that there is more rainfall in the summer months.")
    components.html(figures[3], height=600)

    st.header("Average Bike Rental vs. Rain & Humidity")
    st.write("Figure 5. These two charts show the dips in bike usage at the times when rainfall and humidity spike.")
    components.html(figures[4], height=1000)


def about_us():
    st.title('Group 7')

    col1, col2 = st.beta_columns(2)
    photos = cache.photos()

    col1.image(photos['sonya'], caption='Sonya Gomez')
    col1.write("Hello, my name is Sonya Gomez. I am a CS Major at UC Davis, currently a Junior. I chose CS as my major because being a CS major will give me the freedom to work anywhere under any company I support the values of. In this project, I contributed in the writing aspect and also had a small role within the software team.")

    col2.image(photos['mack'], caption='Mack Gregory')
    col2.write("Hello, I am Mack Gregory. I am a third year Computer Science student at UC Davis. I love studying computer science as a way of being able to make sense of the world around me through data, and programmatically making tasks easier and safer. I hope to take the knowledge from UC Davis into a career in computer security protecting people from breaches of their private data, while ensuring that we can still have progress in modern technology. In this project I helped with writing, data analysis and data exploration.")

    col1.image(photos['joshua'], caption='Joshua Guillen')
    col1.write("My name is Joshua Guillen. I am a senior at UC Davis majoring in Cognitive Science with an emphasis in computation. I chose this major because it allowed me to combine my interest in the human mind through other disciplines besides psychology such as computer science, artificial intelligence, linguistics, philosophy, and neuroscience. I hope my major allows me to work on artificial intelligence such as developing more convincing chatbots. For this project, I was the project leader tasked with facilitating communication between my group members while keeping them on track with our tasks and deadlines. I also helped with data exploration/visualization, and video creation.")

    col2.image(photos['bryce'], caption='Bryce Joseph-Nelson')
    col2.write("Hi, I am Bryce Joseph-Nelson. I am a Cognitive Science senior at UC Davis specializing in computation. I chose this major because the field fascinates me, but my end goal is to use this technical background to assist in my goal of going into marketing for highly technical startups. I’ve worked with a number of biotech companies and see a huge need for being able to communicate complicated information easily through mediums such as video.")

    col1.image(photos['malini'], caption='Malini Manimaran')
    col1.write("Hello, I’m Malini Manimaran. I am a junior at UC Davis with a triple major in Cognitive Science, Math, and Political Science. I became really interested in these three topics because of the intersection of governance and scientific data. I hope to work on developing artificial intelligence that will better inform politicians about their constituencies. For this project, I worked on the initial data exploration/analysis, visualization, and report write up.")

    col2.image(photos['devon'], caption='Devon Mirsalis')
    col2.write("I’m a junior at UC Davis studying for a Computer Science major.  I transferred in from Foothill College, where I majored in Mathematics and Computer Science, but I chose to focus on Computer Science because of the many interesting opportunities in the tech industry.  For this project, I worked on machine learning, specifically brainstorming with other members and creating the Random Forest and Gradient Boosting models.")

    col1.image(photos['charles'], caption='Charles Nguyen')
    col1.write("I am a Computer Science senior at UC Davis. I am passionate about improving people's lives with technology and interested in STEM education, healthcare, and user privacy. For this project, I was in charge of developing the web application using Streamlit. I also implemented a deep neural network and contributed to the writing.")

    col2.image(photos['gabriel'], caption='Gabriel Raulet')
    col2.write("I am a senior majoring in Computer Science and minoring in Mathematics at UC Davis.  I chose computer science as a major because I love developing applications/algorithms and using theory to help solve these problems more efficiently. I hope to work in the computational sciences on problems related to biology/ecology. For this project, I developed a random forest regressor model using a custom tree data structure for predicting demand.")

    col1.image(photos['albert'], caption='Albert Stanley')
    col1.write("I am a junior at UC Davis studying Computer Science. I chose my major because I enjoyed the problem solving nature of work in computer science, and I want to work within the machine learning field since it has brought about many of the interesting technologies we have today. I helped with data cleaning, training the linear regression model and training time series models.")

    col2.image(photos['jordan'], caption='Jordan Stefani')
    col2.write("I am a Senior at UC Davis studying biotechnology and bioinformatics. I initially chose my major because I liked biology and hoped that the “technology” aspect of my major would make my degree more practical. Later, I found a passion for bioinformatics which led me to delve into computer science and math.")
