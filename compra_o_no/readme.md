# Compra o No — Predicción de Compras Online

## Descripción general

- Objetivo: predecir si un usuario realizará una compra en un sitio de e‑commerce a partir de su comportamiento de navegación y características de la sesión.
- Carpeta: `compra_o_no/`
- Dataset: `data/online_shoppers.csv` (fuente habitual: Online Shoppers Purchasing Intention Dataset). Se genera un dataset limpio `data/online_shoppers_cln.csv` al final de la exploración.

## Fuente de datos

- UCI Machine Learning Repository — Online Shoppers Purchasing Intention Dataset: [enlace](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset)
- Este proyecto utiliza dicho dataset como base para el análisis y modelado.

## Estructura de trabajo

- `notebooks/01_exploración.ipynb`: EDA, limpieza, tratamiento de duplicados/outliers, transformaciones.
- `notebooks/02_train_test.ipynb`: partición de datos, preparación y evaluación preliminar.
- `notebooks/03_pipline_final.ipynb`: pipeline final de modelado y exportación.
- `models/final_pipe.pkl`: pipeline/modelo entrenado para inferencia.

### Estructura (árbol) y rutas clave

```text
compra_o_no/
├─ readme.md
├─ data/
│  ├─ online_shoppers.csv              # dataset original (UCI)
│  └─ online_shoppers_cln.csv          # dataset limpio generado por 01_exploración
├─ models/
│  └─ final_pipe.pkl                   # pipeline/modelo entrenado
 └─ notebooks/
	 ├─ 01_exploración.ipynb             # EDA y limpieza
	 ├─ 02_train_test.ipynb              # split y evaluación preliminar
	 └─ 03_pipline_final.ipynb           # pipeline final y exportación
```

- Desde los notebooks (ubicados en `compra_o_no/notebooks/`), las rutas relativas a datos se acceden como `../data/online_shoppers.csv` y `../data/online_shoppers_cln.csv`.

## Exploración y limpieza (01_exploración.ipynb)

### Carga y revisión inicial

- Vista general con `head`, `shape`, `info` y `describe` para validar tipos y rangos.

### Duplicados y nulos

- Conteo y muestra de duplicados; se eliminan con `drop_duplicates`.
- Revisión de nulos con `isna().sum()`; no se detectan nulos críticos.

### Outliers

- Se definen variables numéricas y se resume la cantidad de outliers por IQR (Q1−1.5·IQR, Q3+1.5·IQR).
- Se inspeccionan columnas con más outliers para distinguir si representan tiempos o conteos.

### Transformaciones

- `PageValues`: transformación logarítmica `np.log1p` para reducir asimetría de valores altos.
- Nota: la winsorización de duraciones y conteos susceptibles (p.ej., `Administrative_Duration`, `Informational_Duration`, `ProductRelated_Duration` y sus conteos) se plantea para el set de entrenamiento, evitando alterar la distribución del conjunto completo antes del split.

### Visualizaciones

- Histogramas con KDE de todas las variables numéricas para evaluar forma (asimetría, colas pesadas), dispersión y presencia de valores extremos.

### Exportación

- Se guarda el dataset limpio en `data/online_shoppers_cln.csv` para etapas posteriores.

## Modelado

- División train/test y validación de métricas básicas en `02_train_test.ipynb`.
- Construcción de pipeline en `03_pipline_final.ipynb` integrando preprocesamiento (transformaciones numéricas/categóricas) y el estimador.
- Serialización del pipeline final en `models/final_pipe.pkl`.

## Resultados y hallazgos clave del EDA

- Distribuciones sesgadas a la derecha en duraciones y en `PageValues`, indicando sesiones cortas frecuentes y pocas muy largas; la `log1p` estabiliza la escala de `PageValues`.
- Conteos (p.ej., `Administrative`, `Informational`, `ProductRelated`) con muchos ceros y baja media: sugieren comportamiento esporádico en ciertas secciones.
- La presencia de outliers es consistente con sesiones anómalas (usuarios que dejan la pestaña abierta o interacciones extremadamente breves). Se recomienda winsorizar estas variables solo dentro del pipeline de entrenamiento.

## Cómo reproducir

### Requisitos

- Python 3.9+ recomendado.
- Instalar dependencias desde la raíz del repo o carpeta local:

```bash
pip install -r requirements.txt
```

### Ejecutar notebooks en orden

- `notebooks/01_exploración.ipynb` → genera `data/online_shoppers_cln.csv`.
- `notebooks/02_train_test.ipynb` → partición y evaluación inicial.
- `notebooks/03_pipline_final.ipynb` → pipeline final y guardado del modelo.

## Notas

- La winsorización propuesta debe implementarse en el pipeline para aplicarse exclusivamente a datos de entrenamiento (y parámetros aprendidos), evitando fuga de información.
- Ajustar la semilla aleatoria para reproducibilidad y documentar versiones de librerías si se requiere replicación exacta.
