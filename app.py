# app.py - Versión lista para despliegue
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import rcParams
from sympy import symbols

# Configuración esencial para Streamlit Sharing
st.set_page_config(
    page_title="Modelos de Crecimiento Poblacional",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': None,
        'About': "Análisis de modelos poblacionales con Transformada de Laplace"
    }
)

# Configuración estética mejorada para producción
rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.autolayout': True  # Ajuste automático del layout
})
