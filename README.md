# 📊 Customer Segmentation (RFM) - Brazilian E-Commerce
*Segmentación de Clientes (RFM) - E-Commerce Brasileño*
## 🎯 Objective / Objetivo
**[EN]** An end-to-end data analytics project applying ETL processes and RFM (Recency, Frequency, Monetary) segmentation to a Brazilian e-commerce dataset containing 93,000 unique customers. The goal is to identify high-value customer segments to optimize marketing strategies and resource allocation.
**[ES]** Un proyecto integral de análisis de datos aplicando procesos ETL y segmentación RFM a una base de datos de e-commerce de Brasil con 93,000 clientes únicos. El objetivo es identificar segmentos de alto valor para optimizar estrategias de marketing y asignación de recursos.

## 🛠️ Tech Stack / Tecnologías Utilizadas
* **Python (Pandas):** Data integration, initial cleaning, and handling missing values from raw CSV files. / *Integración de datos, limpieza inicial y manejo de valores nulos desde archivos CSV.*
* **PostgreSQL:** Advanced querying, filtering, and structuring the analytical database. / *Consultas avanzadas, filtrado y estructuración de la base de datos analítica.*
* **Power BI:** Data modeling, DAX measure creation, and interactive dashboard design. / *Modelado de datos, creación de medidas DAX y diseño del dashboard interactivo.*

## ⚙️ Process / Proceso
1.  **Data Extraction (Python):** Consolidated multiple transactional `.csv` files.
2.  **Transformation (SQL):** Cleaned financial data and calculated base RFM metrics.
3.  **Loading & Visualization (Power BI):** Clustered the 93k customers into 4 strategic segments (Champions, Loyal, At Risk, Lost) representing $15.42M in historical revenue.

## 📂 Repository Structure / Estructura del Repositorio
* `/scripts`: Contains the Python notebooks (`.ipynb`) and SQL scripts (`.sql`).
* `/dashboard`: Contains the Power BI file (`.pbix`).
* `/data`: Contains a sample of the raw dataset.

## 💡 Key Insights / Conclusiones Clave
**[EN]** The "Champions" segment represents the most significant portion of the active portfolio, requiring retention strategies, while the "At Risk" segment highlights a critical area for immediate re-engagement campaigns.
**[ES]** El segmento "Campeones" representa la porción más significativa de la cartera activa, requiriendo estrategias de retención, mientras que el segmento "En Riesgo" resalta un área crítica para campañas inmediatas de reactivación.
