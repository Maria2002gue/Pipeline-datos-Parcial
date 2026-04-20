# 🧠 Pipeline de Datos: Salud Mental y Redes Sociales
**Ingeniería de Datos**

Este repositorio contiene un flujo de trabajo **ETL** (Extract, Transform, Load) completo para analizar el impacto de los hábitos digitales en el bienestar de los adolescentes. El proyecto integra almacenamiento en GitHub, documentación técnica, visualización interactiva y lógica de orquestación.

## 🚀 Enlaces del Proyecto
* **Landing Page git hub pages (Documentación ):** [file:///C:/Users/rosam/OneDrive/Documents/Pipeline-Datos/index.html]
* **Dashboard Interactivo (Streamlit):** [https://pipeline-datos-parcial-dppb75x5w6oh7dsvnkcw23.streamlit.app/]
* **Repositorio (git hub):** [https://github.com/Maria2002gue/Pipeline-datos-Parcial]

---

## 🛠️ Estructura del Repositorio
* `data/`: Contiene el dataset original `Teen_Mental_Health_Dataset.csv`.
* `notebooks/`: Análisis Exploratorio de Datos (EDA) inicial en formato `.ipynb`.
* `app.py`: Código principal de la aplicación Streamlit y lógica de visualización.
* `index.html`: Documentación técnica desplegada vía GitHub Pages.
* `requirements.txt`: Librerías necesarias para el entorno de ejecución.

---

## ⚙️ Ingeniería de Datos (Pipeline ETL)

### 1. Ingesta (Extraction)
Los datos se extraen de un archivo CSV que contiene 1,200 registros de adolescentes, incluyendo métricas de uso de plataformas como TikTok e Instagram, horas de sueño y niveles de estrés/ansiedad.

### 2. Transformación (Transformation)
Utilizando la librería **Pandas**, se realizaron las siguientes operaciones:
* Limpieza y normalización de nombres de columnas.
* Manejo de tipos de datos para asegurar cálculos precisos.
* Creación de una variable categórica para clasificar los síntomas de depresión.
* Cálculo de métricas agregadas (promedios de estrés y ansiedad) filtradas dinámicamente.

### 3. Carga y Visualización (Load)
Los datos transformados se inyectan en un dashboard desarrollado con **Streamlit** y **Plotly**, permitiendo al usuario final filtrar la información por género y rango de edad en tiempo real.

---

## 🔗 Orquestación con Airflow
Se implementó una simulación de orquestación basada en los principios de **Apache Airflow**:
* **DAG:** Definición de un flujo acíclico dirigido para asegurar la secuencia Ingesta -> Limpieza -> Visualización.
* **Operadores:** Uso conceptual de `PythonOperator` para las tareas de transformación.
* **Scheduling:** Configuración de una frecuencia de actualización diaria (`@daily`) para mantener la integridad de los insights.

---

## 🏗️ Requisitos Técnicos
Para replicar este proyecto localmente:
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Ejecutar la app: `python -m streamlit run app.py`.
