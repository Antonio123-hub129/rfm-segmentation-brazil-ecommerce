import pandas as pd
from sqlalchemy import create_engine
import os

# 1. LA CLAVE: Definimos la ruta exacta de tus archivos
# Usamos 'r' antes de las comillas para que Windows no se confunda con las barras \
ruta_base = r'C:\Users\Anthony\Desktop\Proyectos Analisis de datos'

# 2. Configura tu conexión a MySQL (Asegúrate de poner tu password real)
engine = create_engine('mysql+pymysql://root:Alejandra123@localhost/olist_db')

# 3. Lista de los 9 archivos
archivos = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_products_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
]

print("--- Iniciando carga de datos a MySQL ---")

# 4. Bucle inteligente
for archivo in archivos:
    # Unimos la carpeta con el nombre del archivo
    ruta_completa = os.path.join(ruta_base, archivo)
    
    # Nombre de la tabla (quitamos el .csv y el _dataset para que sea más limpio)
    nombre_tabla = archivo.replace('.csv', '').replace('_dataset', '')
    
    if os.path.exists(ruta_completa):
        print(f"Cargando {archivo}...")
        df = pd.read_csv(ruta_completa)
        df.to_sql(nombre_tabla, con=engine, if_exists='replace', index=False)
        print(f"✅ Tabla '{nombre_tabla}' creada con éxito.")
    else:
        print(f"❌ Error: El archivo {archivo} no está en la carpeta especificada.")

print("\n🚀 ¡Todo listo! Fase 1 de carga completada.")