import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import rcParams

# Configuración de la página
st.set_page_config(
    page_title="Modelos Poblacionales con Laplace",
    page_icon="📈",
    layout="wide"
)

# Configuración estética
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

# Título
st.title("Análisis de Crecimiento Poblacional")
st.markdown("""
Aplicación interactiva que muestra modelos de crecimiento con Transformada de Laplace.
""")

# Sidebar
with st.sidebar:
    st.header("⚙️ Parámetros")
    r_max = st.slider("Tasa de crecimiento (rₘₐₓ)", 0.1, 2.0, 0.5, 0.05)
    K = st.slider("Capacidad de carga (K)", 100, 5000, 1000, 100)
    N0 = st.slider("Población inicial (N₀)", 1, 100, 10, 1)
    t_max = st.slider("Tiempo máximo (t)", 5, 50, 10, 1)

# Funciones de modelos
def modelo_exponencial(t, N0, r):
    return N0 * np.exp(r * t)

def modelo_logistico(t, N0, r, K):
    return K / (1 + ((K - N0)/N0) * np.exp(-r * t))

# Soluciones analíticas
t_vals = np.linspace(0, t_max, 200)
N_exp = modelo_exponencial(t_vals, N0, r_max)
N_log = modelo_logistico(t_vals, N0, r_max, K)

# Pestañas
tab1, tab2 = st.tabs(["📈 Exponencial", "🔄 Logístico"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        ### Ecuación Diferencial
        ```math
        \\frac{{dN}}{{dt}} = {r_max:.2f}N
        ```
        """)
        st.markdown(f"""
        ### Solución (Transformada de Laplace)
        ```math
        N(t) = {N0}e^{{{r_max:.2f}t}}
        ```
        """)
        
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        ### Ecuación Diferencial
        ```math
        \\frac{{dN}}{{dt}} = {r_max:.2f}\\left(1 - \\frac{{N}}{{{K}}}\\right)N
        ```
        """)
        st.markdown(f"""
        ### Solución (Sustitución)
        ```math
        N(t) = \\frac{{{K}}}{{1 + \\left(\\frac{{{K}-{N0}}}{{{N0}}}\\right)e^{{-{r_max:.2f}t}}}}
        ```
        """)

# Footer
st.markdown("---")
st.caption("Creado para el curso de Modelos Matemáticos | [GitHub Repo](https://github.com/tu_usuario/tu_repositorio)")
