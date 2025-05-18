# app.py - Análisis de Modelos Poblacionales con Transformada de Laplace
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import rcParams

# Configuración para despliegue en Streamlit Sharing
st.set_page_config(
    page_title="Modelos Poblacionales con Laplace",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': None,
        'About': "Análisis interactivo de modelos de crecimiento poblacional"
    }
)

# Configuración profesional de visualización
rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.facecolor': 'white',
    'grid.color': '#dddddd',
    'grid.linestyle': '--',
    'legend.fontsize': 10
})

# Título principal
st.title("Análisis de Modelos Poblacionales")
st.markdown("""
**Exploración interactiva** de los modelos de crecimiento exponencial y logístico, 
con análisis mediante Transformada de Laplace.
""")

# Sidebar con controles interactivos
with st.sidebar:
    st.header("⚙️ Parámetros del Modelo")
    r_max = st.slider("Tasa de crecimiento (rₘₐₓ)", 0.1, 2.0, 0.5, 0.05)
    K = st.slider("Capacidad de carga (K)", 100, 5000, 1000, 100)
    N0 = st.slider("Población inicial (N₀)", 1, 100, 10, 1)
    t_max = st.slider("Tiempo máximo (t)", 5, 50, 10, 1)
    
    st.markdown("---")
    st.markdown("**🔍 Ecuaciones diferenciales:**")
    st.latex(r"\text{Exponencial: } \frac{dN}{dt} = r_{max}N")
    st.latex(r"\text{Logístico: } \frac{dN}{dt} = r_{max}\left(1 - \frac{N}{K}\right)N")

# Funciones de los modelos (sin cambios)
def exponencial(t, N0, r):
    return N0 * np.exp(r * t)

def logistico(t, N0, r, K):
    return K / (1 + ((K - N0)/N0) * np.exp(-r * t))

# Generación de datos
t_vals = np.linspace(0, t_max, 200)
N_exp = exponencial(t_vals, N0, r_max)
N_log = logistico(t_vals, N0, r_max, K)

# Organización en pestañas
tab1, tab2 = st.tabs(["📈 Crecimiento Exponencial", "📊 Crecimiento Logístico"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🧮 Ecuación Diferencial")
        st.latex(rf"\frac{{dN}}{{dt}} = {r_max:.2f}N")
        
        st.markdown("### 🔍 Solución con Laplace")
        st.latex(rf"\mathcal{{L}}\{{N\}} = \frac{{{N0}}}{{s - {r_max:.2f}}}")
        st.latex(rf"N(t) = {N0}e^{{{r_max:.2f}t}}")
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(t_vals, N_exp, 'b-', linewidth=2.5, label='Solución')
        ax.set_title('Crecimiento Exponencial', pad=20)
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Población (N)')
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

with tab2:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🧮 Ecuación Diferencial")
        st.latex(rf"\frac{{dN}}{{dt}} = {r_max:.2f}\left(1 - \frac{{N}}{{{K}}}\right)N")
        
        st.markdown("### 🔍 Linealización y Laplace")
        st.latex(r"u = \frac{1}{N} \Rightarrow \frac{du}{dt} + ru = \frac{r}{K}")
        st.latex(rf"N(t) = \frac{{{K}}}{{1 + \left(\frac{{{K}-{N0}}}{{{N0}}}\right)e^{{-{r_max:.2f}t}}}}")
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(t_vals, N_log, 'r-', linewidth=2.5, label='Solución')
        ax.axhline(y=K, color='gray', linestyle='--', label=f'K = {K}')
        ax.set_title('Crecimiento Logístico', pad=20)
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Población (N)')
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

# Gráfico comparativo
st.markdown("## 📌 Comparación de Modelos")
fig_comp, ax = plt.subplots(figsize=(10, 5))
ax.plot(t_vals, N_exp, 'b-', label=f'Exponencial (r={r_max:.2f})')
ax.plot(t_vals, N_log, 'r-', label=f'Logístico (K={K})')
ax.axhline(y=K, color='gray', linestyle='--', alpha=0.5)
ax.set_title('Comparación de Modelos Poblacionales', pad=20)
ax.set_xlabel('Tiempo')
ax.set_ylabel('Población (N)')
ax.grid(True)
ax.legend()
st.pyplot(fig_comp)

# Explicación teórica con ecuaciones dinámicas
with st.expander("📚 Explicación Teórica Detallada"):
    st.markdown(f"""
    ### Crecimiento Exponencial
    - **Ecuación diferencial**: 
      $\frac{{dN}}{{dt}} = {r_max:.2f}N$
    - **Solución general**: 
      $N(t) = N_0 e^{{rt}} = {N0}e^{{{r_max:.2f}t}}$
    - **Transformada de Laplace**:
      1. Aplicamos Laplace: $s\mathcal{{L}}\{{N\}} - N(0) = {r_max:.2f}\mathcal{{L}}\{{N\}}$
      2. Despejamos: $\mathcal{{L}}\{{N\}} = \\frac{{{N0}}}{{s - {r_max:.2f}}}$
      3. Transformada inversa: $N(t) = {N0}e^{{{r_max:.2f}t}}$
    
    ### Crecimiento Logístico
    - **Ecuación diferencial**: 
      $\frac{{dN}}{{dt}} = {r_max:.2f}N\\left(1 - \\frac{{N}}{{{K}}}\\right)$
    - **Linealización** (sustitución de Bernoulli):
      1. Definimos $u = \\frac{{1}}{{N}}$
      2. Derivamos: $\\frac{{du}}{{dt}} = -\\frac{{1}}{{N^2}}\\frac{{dN}}{{dt}}$
      3. Sustituimos: $\\frac{{du}}{{dt}} + {r_max:.2f}u = \\frac{{{r_max:.2f}}}{{{K}}}$
    - **Solución**: 
      $N(t) = \\frac{{{K}}}{{1 + \\left(\\frac{{{K}-{N0}}}{{{N0}}}\\right)e^{{-{r_max:.2f}t}}}}$
    
    ### Interpretación Biológica
    - **r = {r_max:.2f}**: Tasa intrínseca de crecimiento
    - **K = {K}**: Capacidad de carga del ambiente
    - **N₀ = {N0}**: Población inicial
    
    ### Aplicaciones
    - **Microbiología**: Crecimiento bacteriano (fase exponencial)
    - **Ecología**: Modelado de poblaciones animales
    - **Epidemiología**: Propagación de enfermedades
    """)

# Pie de página
st.markdown("---")
st.markdown("🔍 **App creada para análisis de modelos poblacionales** | 📊 **Visualización interactiva**")
