import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forecast for the Next Days!')
place=st.text_input('place :')
days=st.slider("Forecast Days",min_value=1,max_value=5,step=1
               ,help="select the number of forecasted days")
option=st.selectbox("select data to view",options=("temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature /sky data
        filtered_data=get_data(place=place,forecast_days=days)
        #create a temperature plot
        if option=="temperature":
            temperature=[dict["main"]["temp"] for dict in filtered_data]
            temperature=[temp/10 for temp in temperature]
            dates=[dict["dt_txt"] for dict in filtered_data]
            figure=px.line(x=dates,y=temperature,labels={"x":"dates",
                                              "y":"temperature"})
            st.plotly_chart(figure)
        # show the sky condition with image
        if option=="Sky":
            images={"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition=[dict["weather"][0]["main"] for dict in filtered_data]
            image_path=[images[condition] for condition in sky_condition]
            st.image(image_path,width=100)
    except KeyError:
        st.subheader("oh you entered non-existing place")

