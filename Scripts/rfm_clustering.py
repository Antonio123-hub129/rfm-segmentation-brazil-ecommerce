import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

print("--- Iniciando Fase 2: Clustering con K-Means ---")

# 1. Conectar a MySQL y extraer la tabla maestra
# RECUERDA: Cambia 'tu_password' por tu contraseña real
engine = create_engine('mysql+pymysql://root:Alejandra123@127.0.0.1:3306/olist_db')

print("Extrayendo datos de SQL...")
query = "SELECT * FROM rfm_segmentation"
df_rfm = pd.read_sql(query, con=engine)

# Limpieza rápida por si hay valores nulos generados en los joins
df_rfm = df_rfm.dropna()

# 2. Preprocesamiento (Escalado de variables)
# Como el dinero (Monetary) tiene números grandes y la frecuencia (Frequency) números pequeños,
# debemos "escalarlos" para que el algoritmo no le dé más importancia solo al dinero.
print("Estandarizando variables estadísticas...")
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(df_rfm[['recency', 'frequency', 'monetary']])

# 3. Aplicar el Algoritmo K-Means
# Elegimos 4 clústeres para representar: Campeones, Leales, En Riesgo y Perdidos
print("Entrenando algoritmo K-Means...")
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df_rfm['cluster'] = kmeans.fit_predict(rfm_scaled)

# 4. Análisis de Negocio: Ver el perfil promedio de cada grupo
segment_profile = df_rfm.groupby('cluster').agg({
    'recency': 'mean',
    'frequency': 'mean',
    'monetary': ['mean', 'count']
}).round(1)

print("\n📊 Perfil de los Segmentos de Clientes (Promedios):")
print(segment_profile)

# 5. Exportar el resultado para Power BI
# Guardamos este dataframe enriquecido en tu escritorio
ruta_salida = r'C:\Users\Anthony\Desktop\Proyectos Analisis de datos\rfm_clusters_final.csv'
df_rfm.to_csv(ruta_salida, index=False)

print(f"\n✅ ¡Éxito! Archivo guardado en: {ruta_salida}")