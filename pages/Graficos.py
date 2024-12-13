import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay
import utilidades as util
from pickle import dump
from pickle import load
import numpy as np
import plotly.express as px


#configurar la pagina principal
st.set_page_config(
    page_title="PSMAD",#"Prevención del suicidio por medio de Analítica de Datos"
    page_icon=":heartpulse:",
    initial_sidebar_state="expanded",
    layout="centered"
)
#llamamos el menú
util.generarMenu()

#Título
st.title("Tasa de Suicidios por Indicadores")
#leo los datos
df2= pd.read_csv('data/data_final.csv', index_col=0)
#selector de gráficos

st.header('Visualizador de Gráficos')
tipo = st.selectbox('Seleccione el tipo de gráfico',
                    ['Barras','Líneas','Tortas'])
#selector de las variables a comparar
variable = st.selectbox('Seleccione la variable a comparar',
                      df2.columns[1:].values)


#después de seleccionar
if tipo == 'Barras':
    fig = px.bar(df2,x='inten_pre',
                y=variable, barmode='group',
    title=f'Tasa de Suicidios por Indicadores {variable}')
elif tipo == 'Líneas':
    fig = px.line(df2,x='inten_pre',
              y=variable,
    title=f'Tasa de Suicidios por Indicadores {variable}')

elif tipo == 'Tortas':
    fig = px.pie(
        df2, 
        names='inten_pre',  # Columna que representa las categorías
        values=variable,    # Columna que representa los valores
        title=f'Tasa de Suicidios por Indicadores {variable}'  # Título del gráfico
    )
    

st.plotly_chart(fig)


