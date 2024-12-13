import pandas as pd
import streamlit as st
import utilidades as util

#configurar la pagina principal
st.set_page_config(
    page_title="PSMAD",#"Prevención del suicidio por medio de Analítica de Datos"
    page_icon=":heartpulse:",
    initial_sidebar_state="expanded",
    layout="centered"
)

#llamamos el menú
util.generarMenu()



st.title("PSMAD - Prevención del suicidio por medio de Analítica de Datos")
st.write (
     """ Este proyecto busca abordar la problemática del suicidio, una de las principales causas de muerte a nivel nacional principalmente en el departamento de Antioquia y mas especificamente en la ciudad de Medellin, y una crisis de salud pública que afecta a individuos de todas las edades, géneros y contextos sociales. Existen varios problemas y necesidades clave relacionados con esta situación""")
          
st.write("""Fuente: SIVIGILA""")      
          
st.write(
    """ https://docs.google.com/spreadsheets/d/1YbboqgR2RLodCmEjO0JT9W6rgbDUJmxR/edit?usp=drive_link&ouid=115218483543020908368&rtpof=true&sd=true""")




from PIL import Image
imagen = Image.open("media\imagen_2.jpg")
st.image(imagen, caption="Salud Mental",
        use_container_width=False,width=200)
hide_stream_style = """

        <style>

        #MainMenu {visibility: hidden;}

        footer {visibility: hidden;}

        </style>

        """

st.header("Key Performance Indicators (KPIs)")

st.write("""

- KPI: Identificar a través de los parámetros de los intentos de suicidios de usuarios,  como el género, la edad, ubicación, para determinar la problematica.

""")
