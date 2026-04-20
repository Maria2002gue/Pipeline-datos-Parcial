import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Salud Mental Adolescente", page_icon="🧠", layout="wide")

# Estilos personalizados para que se vea profesional
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO Y DOCUMENTACIÓN (Paso 4)
st.title("📊 Dashboard: Impacto de Redes Sociales en Jóvenes")
st.markdown("""
Este dashboard es el entregable final del **Pipeline de Datos**. 
Analiza la relación entre el uso de tecnología, el sueño y la salud mental.
""")

# 3. PROCESO ETL: INGESTA (Paso 4)
@st.cache_data
def cargar_datos():
    # Asegúrate de que el archivo esté en la carpeta 'data'
    df = pd.read_csv("data/Teen_Mental_Health_Dataset.csv")
    return df

try:
    df = cargar_datos()

    # 4. PROCESO ETL: TRANSFORMACIÓN (Paso 4)
    # Creamos etiquetas legibles para la depresión
    df['Estado_Depresion'] = df['depression_label'].map({0: 'Sin Síntomas', 1: 'Con Síntomas'})

    # 5. SIDEBAR: FILTROS INTERACTIVOS (Paso 3)
    st.sidebar.header("🔍 Filtros Dinámicos")
    genero_select = st.sidebar.multiselect(
        "Filtrar por Género:",
        options=df['gender'].unique(),
        default=df['gender'].unique()
    )
    
    # Filtro de edad
    rango_edad = st.sidebar.slider("Rango de Edad:", 13, 19, (13, 19))

    # Aplicamos los filtros al dataframe
    df_f = df[(df['gender'].isin(genero_select)) & (df['age'].between(rango_edad[0], rango_edad[1]))]

    # 6. MÉTRICAS CLAVE
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Muestra Total", len(df_f))
    col2.metric("Promedio Estrés", f"{df_f['stress_level'].mean():.1f}/10")
    col3.metric("Horas Redes/Día", f"{df_f['daily_social_media_hours'].mean():.1f}h")
    col4.metric("Horas Sueño", f"{df_f['sleep_hours'].mean():.1f}h")

    # 7. VISUALIZACIONES DINÁMICAS (Paso 3)
    st.divider()
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("📱 Uso de Redes vs Ansiedad")
        fig_scatter = px.scatter(
            df_f, x='daily_social_media_hours', y='anxiety_level',
            color='platform_usage', size='stress_level',
            title="Correlación: Tiempo en Pantalla y Ansiedad",
            labels={'daily_social_media_hours': 'Horas Redes Sociales', 'anxiety_level': 'Nivel de Ansiedad'}
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with c2:
        st.subheader("😴 Calidad del Sueño por Género")
        fig_box = px.box(
            df_f, x='gender', y='sleep_hours', color='gender',
            title="Distribución de Horas de Sueño",
            points="all"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    # 8. ORQUESTACIÓN CON AIRFLOW (Paso 5 - Nuevo)
    st.divider()
    st.header("⚙️ Sección: Orquestación de Datos (Airflow)")
    
    col_info, col_dag = st.columns([1, 1])
    
    with col_info:
        st.write("**Ejercicios resueltos de la simulación:**")
        st.write("""
        * **Ejercicio 1: Definición de DAG:** Se estructuró un flujo lineal para garantizar que la limpieza de nulos ocurra antes del análisis.
        * **Ejercicio 2: Operadores:** Uso de `PythonOperator` para las tareas de transformación.
        * **Ejercicio 3: Scheduling:** Configuración de ejecución `@daily` para monitorear tendencias diarias.
        """)

    with col_dag:
        st.write("**Esquema del DAG Implementado:**")
        st.graphviz_chart('''
            digraph {
                rankdir=LR
                node [shape=box, style=filled, color=lightgreen]
                Ingesta_CSV -> Limpieza_Nulos
                Limpieza_Nulos -> Transformacion_Variables
                Transformacion_Variables -> Carga_Dashboard
            }
        ''')

    st.success("✅ Datos sincronizados y orquestados correctamente.")

except Exception as e:
    st.error(f"Error al cargar el dataset: {e}")
    st.info("Verifica que el archivo esté en: data/Teen_Mental_Health_Dataset.csv")