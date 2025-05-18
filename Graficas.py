import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import rcParams
from sympy import symbols, latex

# Configuración de la página
st.set_page_config(page_title="Modelos Interactivos", layout="wide")

# Configuración estética
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

# Título y descripción
st.title("Modelos de Crecimiento Poblacional Interactivos")
st.markdown("""
Explore cómo cambian las ecuaciones y gráficas al modificar los parámetros.
Tanto las curvas como las expresiones matemáticas se actualizan en tiempo real.
""")

# Sidebar con controles
with st.sidebar:
    st.header("Controles Interactivos")
    r_max = st.slider("Tasa de crecimiento (rₘₐₓ)", 0.1, 2.0, 0.5, 0.05)
    K = st.slider("Capacidad de carga (K)", 100, 5000, 1000, 100)
    N0 = st.slider("Población inicial (N₀)", 1, 100, 10, 1)
    t_max = st.slider("Tiempo máximo (t)", 5, 50, 10, 1)

# Funciones de los modelos
def exponencial(t, N0, r):
    return N0 * np.exp(r * t)

def logistico(t, N0, r, K):
    return K / (1 + ((K - N0)/N0) * np.exp(-r * t))

# Generar datos
t_vals = np.linspace(0, t_max, 200)
N_exp = exponencial(t_vals, N0, r_max)
N_log = logistico(t_vals, N0, r_max, K)

# Crear pestañas para organizar el contenido
tab1, tab2 = st.tabs(["Crecimiento Exponencial", "Crecimiento Logístico"])

with tab1:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Ecuación Diferencial")
        st.latex(rf"\frac{{dN}}{{dt}} = {r_max:.2f}N")
        
        st.markdown("### Solución General")
        st.latex(rf"N(t) = {N0}e^{{{r_max:.2f}t}}")
        
        st.markdown("### Transformada de Laplace")
        st.latex(rf"\mathcal{{L}}\{{N\}} = \frac{{{N0}}}{{s - {r_max:.2f}}}")
        st.latex(rf"N(t) = {N0}e^{{{r_max:.2f}t}}")
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(t_vals, N_exp, 'b-', linewidth=2.5)
        ax.set_title('Crecimiento Exponencial', fontsize=14)
        ax.set_xlabel('Tiempo', fontsize=12)
        ax.set_ylabel('Población (N)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig)

with tab2:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Ecuación Diferencial")
        st.latex(rf"\frac{{dN}}{{dt}} = {r_max:.2f}\left(1 - \frac{{N}}{{{K}}}\right)N")
        
        st.markdown("### Solución General")
        st.latex(rf"N(t) = \frac{{{K}}}{{1 + \left(\frac{{{K}-{N0}}}{{{N0}}}\right)e^{{-{r_max:.2f}t}}}}")
        
        st.markdown("### Linealización por Sustitución")
        st.latex(r"u = \frac{1}{N} \Rightarrow \frac{du}{dt} = -\frac{1}{N^2}\frac{dN}{dt}")
        st.latex(rf"\frac{{du}}{{dt}} + {r_max:.2f}u = \frac{{{r_max:.2f}}}{{{K}}}")
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(t_vals, N_log, 'r-', linewidth=2.5)
        ax.axhline(y=K, color='gray', linestyle='--', label=f'K = {K}')
        ax.set_title('Crecimiento Logístico', fontsize=14)
        ax.set_xlabel('Tiempo', fontsize=12)
        ax.set_ylabel('Población (N)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        st.pyplot(fig)

# Comparación interactiva
st.markdown("## Comparación Interactiva de Modelos")
st.markdown(f"""
- **Tasa de crecimiento (r):** {r_max:.2f}
- **Población inicial (N₀):** {N0}
- **Capacidad de carga (K):** {K} (solo logístico)
""")

# Gráfica comparativa
fig_comp, ax = plt.subplots(figsize=(10, 6))
ax.plot(t_vals, N_exp, 'b-', label='Exponencial')
ax.plot(t_vals, N_log, 'r-', label='Logístico')
ax.axhline(y=K, color='gray', linestyle='--', label=f'K = {K}')
ax.set_title('Comparación de Modelos', fontsize=14)
ax.set_xlabel('Tiempo', fontsize=12)
ax.set_ylabel('Población (N)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
st.pyplot(fig_comp)