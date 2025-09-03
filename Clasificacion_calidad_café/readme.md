# Clasificación de Calidad de Café ☕️ (Pipeline + App)

Proyecto final de clasificación de calidad de café desarrollado por Juan Acevedo. El objetivo es predecir la categoría de calidad del café a partir de atributos sensoriales y de laboratorio, y exponer el modelo mediante una interfaz interactiva con Gradio. Además del entorno local, el proyecto fue desplegado en Hugging Face Spaces.

## Dataset

- Fuente: [Coffee Quality Data (CQI) — Kaggle](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi)
- Licencia/derechos: consultar la página del dataset en Kaggle.

Archivos de datos usados en este subproyecto (carpeta `data/`):

- `coffe_df.csv`: dataset base procesado para exploración.
- `df_ready.csv`: subconjunto final de variables listo para el pipeline/modelo.

## Variables y objetivo

El objetivo es clasificar la calidad del café (variable `Quality`, clases: “Medio - Alto” y “Alto”). Para la versión final del modelo y la app se emplean 6 características seleccionadas por importancia:

- Aftertaste
- Overall
- Body
- Aroma
- Flavor
- Moisture Percentage

Estas variables se seleccionaron tras la exploración y análisis de importancia de características.

## Flujo de trabajo

1. Exploración, limpieza y preparación (`notebooks/01_exploracion_analisis_train.ipynb`).
   - Depuración de variables irrelevantes (identificadores, textos, etc.).
   - Manejo de nulos, codificación, y partición train/test (estratificada).
   - Búsqueda de hiperparámetros con GridSearchCV (f1 macro) para Árbol de Decisión.
   - Definición de `Quality` a partir de “Total Cup Points”.
2. Selección de las 6 variables finales y exportación a `data/df_ready.csv`.
3. Entrenamiento del pipeline (`notebooks/02_pipline.ipynb`).
   - Pipeline: `StandardScaler` + `DecisionTreeClassifier` (parámetros fijados tras búsqueda).
   - Evaluación con métricas (accuracy, reporte de clasificación, matriz de confusión).
   - Serialización del modelo en `notebooks/coffe_model.joblib`.
4. Despliegue local con Gradio (`app.py`).
   - Interfaz con sliders para las 6 características.
   - Muestra etiqueta predicha y probabilidades por clase.

## Estructura relevante

- `notebooks/01_exploracion_analisis_train.ipynb`: EDA, preparación, selección de variables y tuning.
- `notebooks/02_pipline.ipynb`: Entrenamiento del pipeline y guardado del modelo (`coffe_model.joblib`).
- `app.py`: Interfaz Gradio que carga el modelo y permite inferencia interactiva.
- `requirements.txt`: Dependencias del subproyecto (Gradio, scikit-learn, pandas, etc.).

## Ejecutar localmente

Requisitos:

- Python 3.9+ recomendado.

Instalación (desde `Clasificacion_calidad_café/`):

```bash
pip install -r requirements.txt
```

Ejecución de la app (desde `Clasificacion_calidad_café/`):

```bash
python app.py
```

La aplicación:

- Carga el modelo desde `notebooks/coffe_model.joblib`.
- Expone sliders para: Aftertaste, Overall, Body, Aroma, Flavor y Moisture Percentage.
- Muestra la predicción y, cuando está disponible, las probabilidades por clase.

Si aparece un error de carga, confirma que `notebooks/coffe_model.joblib` existe y que las dependencias están instaladas.

## Despliegue en Hugging Face Spaces

El proyecto también se desplegó en Hugging Face Spaces con SDK Gradio.

Pasos generales para reproducir el despliegue:

1. Crear un Space nuevo en Hugging Face con SDK: Gradio.
2. Incluir en el Space (o conectar el repo) los archivos mínimos:
   - `app.py` (punto de entrada de Gradio).
   - `requirements.txt` (dependencias: gradio, scikit-learn, joblib, pandas, numpy, etc.).
   - `notebooks/coffe_model.joblib` (archivo del modelo entrenado).
   - Opcionalmente, `data/df_ready.csv` si se requiere trazabilidad del origen.
3. En la configuración del Space, definir:
   - SDK: Gradio
   - Entrypoint: `app.py`
4. Al hacer push, el Space instalará dependencias y levantará la app automáticamente.

Nota: Si usas una estructura alternativa (por ejemplo `coffee-quality-classifier/`), asegúrate de ajustar la ruta de carga del modelo dentro de `app.py` y de ubicar `coffe_model.joblib` donde el script lo espere.

> Si tienes un enlace público del Space, añádelo aquí para acceso rápido.

## Métricas y consideraciones

- El modelo (Árbol de Decisión + estandarización) logra métricas competitivas en un dataset relativamente pequeño, sin evidencias marcadas de sobreajuste según la validación interna.
- Limitaciones: tamaño muestral, sesgos del dataset original, y sensibilidad a los rangos de entrada.
- Recomendaciones: más datos, validación cruzada ampliada y explorar modelos adicionales (RandomForest, XGBoost, etc.).

## Autor

- Juan Acevedo — 2025

## Licencia y datos

Este repositorio incluye un archivo `LICENSE`. Revisa sus términos para el uso del código. El uso de los datos está sujeto a la licencia/condiciones del dataset en Kaggle.
