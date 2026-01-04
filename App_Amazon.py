import streamlit as st
import pandas as pd

# Configuración visual de la App
st.set_page_config(page_title="Amazon Hunter v1.0", page_icon="💰")
st.title("🚀 Amazon Arbitrage Hunter")
st.write("Encuentra productos ganadores con baja competencia en segundos.")

# Panel de control para el usuario
categoria = st.selectbox("Selecciona Categoría", ["Hogar y Cocina", "Electrónica", "Juguetes", "Belleza"])
presupuesto = st.slider("Presupuesto máximo por unidad (€)", 10, 500, 50)

if st.button("Buscar Oportunidades"):
    st.info(f"Escaneando {categoria} buscando huecos de mercado...")
    
    # Aquí corre tu lógica (simulada con datos reales para el ejemplo)
    data = [
        {"Producto": "Lámpara LED Minimal", "Precio": 24.99, "Reseñas": 12, "Puntuación": 4.8, "ROI Est.": "35%"},
        {"Producto": "Set Cuchillos Cerámica", "Precio": 39.50, "Reseñas": 5, "Puntuación": 4.5, "ROI Est.": "42%"},
        {"Producto": "Organizador Bambú", "Precio": 19.99, "Reseñas": 21, "Puntuación": 4.7, "ROI Est.": "28%"}
    ]
    
    df = pd.DataFrame(data)
    st.table(df) # Muestra los datos de forma elegante
    
    # Botón para que el cliente se baje su Excel
    st.download_button(label="Descargar Reporte Excel", data=df.to_csv().encode('utf-8'), file_name='oportunidades.csv')
    st.success("¡Análisis completado!")