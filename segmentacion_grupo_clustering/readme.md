# Segmentación de Clientes con Clustering (K-Means + PCA)

Proyecto de segmentación de clientes usando técnicas de clustering no supervisado sobre el dataset “Marketing Campaign” de Kaggle. El flujo incluye EDA, limpieza, selección y comparación de modelos, ensamblaje en un Pipeline y despliegue de una app en Hugging Face Spaces.

Demo (Hugging Face): añade aquí tu URL pública cuando la tengas activa.

## Estructura del proyecto

```text
segmentacion_grupo_clustering/
├─ readme.md
├─ data/
│  ├─ marketing_campaign.csv        # dataset original (Kaggle)
│  └─ clean_df.csv                  # dataset limpio generado por 01_exploracion_analisis
├─ models/
│  └─ final_pipe.joblib             # pipeline entrenado (scaler + PCA + KMeans)
├─ notebooks/
│  ├─ 01_exploracion_analisis.ipynb # EDA, limpieza y exportación de clean_df.csv
│  ├─ 02_prueba_modelos.ipynb       # comparación de KMeans/HC/DBSCAN con y sin PCA
│  └─ 03_pipline _final.ipynb       # entrenamiento del pipeline final y guardado del modelo
└─ Find_clinet/
   ├─ app.py                        # app (Gradio) para inferencia y demo
   ├─ final_pipe.joblib             # copia del modelo para la app
   ├─ clean_df.csv                  # referencia de columnas/formatos
   ├─ requirements.txt              # dependencias mínimas de la app
   └─ README.md
```

- Dataset original: [data/marketing_campaign.csv](segmentacion_grupo_clustering/data/marketing_campaign.csv)
- Dataset limpio: [data/clean_df.csv](segmentacion_grupo_clustering/data/clean_df.csv)
- Notebooks:
  - EDA y limpieza: [notebooks/01_exploracion_analisis.ipynb](segmentacion_grupo_clustering/notebooks/01_exploracion_analisis.ipynb)
  - Pruebas de modelos: [notebooks/02_prueba_modelos.ipynb](segmentacion_grupo_clustering/notebooks/02_prueba_modelos.ipynb)
  - Pipeline final: [notebooks/03_pipline _final.ipynb](segmentacion_grupo_clustering/notebooks/03_pipline _final.ipynb)
- Modelo entrenado: [models/final_pipe.joblib](segmentacion_grupo_clustering/models/final_pipe.joblib)
- App de demo: [Find_clinet/app.py](segmentacion_grupo_clustering/Find_clinet/app.py)

## Dataset y preparación

Fuente: “Marketing Campaign” (Kaggle).

Limpieza y transformaciones principales (ver [01_exploracion_analisis.ipynb](segmentacion_grupo_clustering/notebooks/01_exploracion_analisis.ipynb)):
- Drop de Dt_Customer.
- Imputación de Income nulo con la media.
- Reducción de asimetría con log1p en variables de gasto: Income, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds.
- Exportación de clean_df.csv.

## Comparación de modelos

En [02_prueba_modelos.ipynb](segmentacion_grupo_clustering/notebooks/02_prueba_modelos.ipynb) probé:
- K-Means sin/cons PCA (k en [2..14], Elbow + Silhouette).
- Agglomerative Clustering (dendrograma + Silhouette).
- DBSCAN (búsqueda en malla de eps y min_samples, con y sin PCA).

Conclusión: K-Means con PCA (2 componentes) ofrece el mejor compromiso (mejores curvas Elbow/Silhouette y clusters bien separados). Elegí k=2.

## Pipeline final

Entrené un pipeline con escalado, reducción dimensional y clustering (ver [03_pipline _final.ipynb](segmentacion_grupo_clustering/notebooks/03_pipline _final.ipynb)):

```python
# StandardScaler → PCA(2) → KMeans(n_clusters=2)
# Guardado en models/final_pipe.joblib
```

El pipeline se ajustó sobre X = clean_df sin columnas ['ID','Education','Marital_Status'].

## Requisitos e instalación

- Python 3.9+
- Instalar dependencias (desde la raíz del repo):

```bash
pip install -r requirements.txt
```

Para ejecutar solo la app:
```bash
cd segmentacion_grupo_clustering/Find_clinet
pip install -r requirements.txt
```

## Cómo reproducir

1) Ejecutar el EDA y limpieza para generar el dataset limpio:
- [notebooks/01_exploracion_analisis.ipynb](segmentacion_grupo_clustering/notebooks/01_exploracion_analisis.ipynb)

2) Explorar y comparar modelos de clustering:
- [notebooks/02_prueba_modelos.ipynb](segmentacion_grupo_clustering/notebooks/02_prueba_modelos.ipynb)

3) Entrenar y serializar el pipeline final:
- [notebooks/03_pipline _final.ipynb](segmentacion_grupo_clustering/notebooks/03_pipline _final.ipynb) genera [models/final_pipe.joblib](segmentacion_grupo_clustering/models/final_pipe.joblib)

## Uso del modelo (código mínimo)

Ejemplo para cargar el pipeline y predecir el cluster de un nuevo cliente (asegurando el mismo esquema de columnas que el entrenamiento):

```python
import joblib
import pandas as pd

pipe = joblib.load("segmentacion_grupo_clustering/models/final_pipe.joblib")

nuevo_cliente = pd.DataFrame([{
    "Year_Birth": 1985, "Income": 45000, "Kidhome": 1, "Teenhome": 0, "Recency": 20,
    "MntWines": 250, "MntFruits": 30, "MntMeatProducts": 120, "MntFishProducts": 40,
    "MntSweetProducts": 15, "MntGoldProds": 10, "NumDealsPurchases": 2, "NumWebPurchases": 3,
    "NumCatalogPurchases": 1, "NumStorePurchases": 5, "NumWebVisitsMonth": 4,
    "AcceptedCmp3": 0, "AcceptedCmp4": 1, "AcceptedCmp5": 0, "AcceptedCmp1": 0,
    "AcceptedCmp2": 0, "Complain": 0, "Z_CostContact": 3, "Z_Revenue": 11, "Response": 1
}])

cluster = pipe.predict(nuevo_cliente)[0]
print(f"Cluster asignado: {cluster}")
```

Nota: el modelo se entrenó con un dataset donde ciertas columnas de gasto y ‘Income’ fueron transformadas con log1p. Si vas a inferir con datos crudos (no transformados), considera aplicar las mismas transformaciones previas para mantener la coherencia con el entrenamiento.

## Ejecutar la app local

La app (Gradio) vive en [Find_clinet/app.py](segmentacion_grupo_clustering/Find_clinet/app.py) y usa el modelo [Find_clinet/final_pipe.joblib](segmentacion_grupo_clustering/Find_clinet/final_pipe.joblib).

```bash
cd segmentacion_grupo_clustering/Find_clinet
python app.py
```

## Despliegue en Hugging Face Spaces

Pasos generales:
- Crear un Space (SDK: Gradio).
- Subir archivos mínimos:
  - app.py (punto de entrada).
  - requirements.txt (dep. de la app).
  - final_pipe.joblib (modelo).
  - Opcional: clean_df.csv (para referencia de columnas/rangos).
- Configurar Entrypoint en el Space: app.py.
- Al hacer push, el Space instala dependencias y levanta la app automáticamente.


## Resultados y consideraciones

- Segmentación en 2 clusters con K-Means tras PCA(2) mostró mejor separación (curvas Elbow y puntuación Silhouette superiores frente a alternativas).
- PCA ayudó a:
  - Reducir ruido y colinealidad.
  - Acelerar el ajuste.
  - Mejorar la separabilidad de clusters.
- Limitaciones: clustering no supervisado requiere interpretación de negocio; conviene validar los grupos con métricas de valor/propensión y realizar perfiles por cluster.

## Archivos clave

- Limpieza y exportación: [notebooks/01_exploracion_analisis.ipynb](segmentacion_grupo_clustering/notebooks/01_exploracion_analisis.ipynb)
- Comparativa de modelos: [notebooks/02_prueba_modelos.ipynb](segmentacion_grupo_clustering/notebooks/02_prueba_modelos.ipynb)
- Pipeline y guardado: [notebooks/03_pipline _final.ipynb](segmentacion_grupo_clustering/notebooks/03_pipline _final.ipynb)
- Modelo final: [models/final_pipe.joblib](segmentacion_grupo_clustering/models/final_pipe.joblib)
- App (demo): [Find_clinet/app.py](segmentacion_grupo_clustering/Find_clinet/app.py)

## Licencia

Este repositorio incluye un archivo LICENSE en la raíz del proyecto. Revisa sus términos para el uso del código y los datos.

## Realizado por 
#### Juan Acevedo