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
import sklearn 

def generarMenu():
    with st.sidebar:
        st.header('PSMAD')
        st.page_link('Home.py', label='Inicio', icon='🏠')
        st.page_link('pages/Pronóstico.py', label='Pronóstico PSMAD', icon='💚')
        st.page_link('pages/Graficos.py', label='Graficas', icon='🌳')


def modelo_rf(df):
    #Variable a predeci
    Y = df.iloc[:,0]
    #Variables predictoras
    X = df.iloc[:,1:34] 
    #Variables de prueba  ->  prueba
    #Variables de entrenamiento -> entrenar
    X_entrenar, X_prueba, Y_entrenar, Y_prueba = train_test_split(X, Y, train_size=0.85, random_state=0)
    st.markdown('-Separamos los datos')
    st.write('Set de entrenamiento')
    st.info(X_entrenar.shape)
    st.write('Set de eprueba')
    st.info(X_prueba.shape)
    st.markdown('-Detalles de las variables')
    st.write('Variables Predictoras')
    st.info(list(X.columns))
    st.write('Variable a Predecir')
    st.info(Y.name)

    #Creamos el arbol
    arbol = DecisionTreeClassifier(max_depth=4)
    #entrenamos el arbol
    arbol.fit(X_entrenar,Y_entrenar)
    st.subheader('**Características del modelo')
    st.markdown('-Set de Prueba')
    #Hacemos la predición
    Y_prediccion = arbol.predict(X_prueba)
    accuracy = accuracy_score(Y_prueba,Y_prediccion)
    st.write('Accurac:')
    st.info(accuracy)
    #Parámeros
    #st.subheader('**Parámetros del modeo')
    #st.write(arbol.get_param())
    #Guardamos el moelo
    #archivo_modelo = open('data\modelo_rf.sav', 'b')
    #dump(arbol, archivo_modelo)
    #archivo_modelo.clo

