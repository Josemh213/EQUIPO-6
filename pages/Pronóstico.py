import streamlit as st
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
#subtítulo
st.header('Datos')
#leo los datos
df = pd.read_csv('data/data_final.csv', index_col=0)
st.markdown('Datos de los Usuarios')
st.write(df)

#Mostramos el modelo
st.markdown('Resultado del modelo Random Forest para los datos históricos')
util.modelo_rf(df)


