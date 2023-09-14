import streamlit as st

st.title('Weather Forecast for the Next Days!')
place=st.text_input('place :')
days=st.slider("Forecast Days",min_value=1,max_value=5,step=1
               ,help="select the number of forecasted days")

option=st.selectbox("select data to view",options=("temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")