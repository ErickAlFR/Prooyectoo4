import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto 4')
st.write('*Web app hecha en Python* :sunglasses:')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botó

if hist_button:
    st.write('Histograma en función de la medida del odómetro')
    fig= px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

#build_histogram = st.checkbox('Construir un histograma')
#if build_histogram:


hist_button= st.button('Mostrar diagrama de dispersión')
if hist_button:
    st.write('Diagrama de dispersión que relaciona precio, año y condición')
    fig = px.scatter(car_data, x="price", y="model_year", color='condition')
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('Marca la casilla para visualizar un histograma')
if build_histogram:
    st.write('Histograma en función del precio')
    fig= px.histogram(car_data,x='price')

    st.plotly_chart(fig,use_container_width=True)