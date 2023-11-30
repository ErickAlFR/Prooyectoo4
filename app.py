import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botó

if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig= px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

#build_histogram = st.checkbox('Construir un histograma')
#if build_histogram:


hist_button= st.button('Mostrar diagrama de dispersión')
if hist_button:
    st.write('Diagrama de dispersión que relaciona precio, año y condición')
    fig = px.scatter(car_data, x="price", y="model_year", symbol='condition')
    fig.show()