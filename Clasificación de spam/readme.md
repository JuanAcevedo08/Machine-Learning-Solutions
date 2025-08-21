# Clasificación de Spam con Machine Learning

Proyecto de clasificación binaria para detectar mensajes de texto (SMS) tipo spam. Incluye análisis exploratorio, entrenamiento con técnicas de vectorización y balanceo, empaquetado en un pipeline y una interfaz interactiva con ipywidgets.

## Estructura del proyecto

```text
Clasificación de spam/
├── data/
│   ├── spam.csv           # Dataset original (UCI)
│   └── spam_clean.csv     # Dataset limpio generado en el análisis
├── notebooks/
│   ├── 01_exploracion_analisis_limpieza.ipynb   # EDA, limpieza y guardado de spam_clean.csv
│   ├── 02_test_train_validation.ipynb           # Vectorización, split, modelo base, métricas y SMOTE
│   ├── 03_pipline_final.ipynb                   # Pipeline (TF-IDF + SMOTE + LR) y guardado del modelo
│   └── 04_interactividad_app.ipynb              # UI interactiva con ipywidgets para clasificar nuevos textos
└── readme.md
```

## Dataset

- Fuente: UCI Machine Learning Repository — SMS Spam Collection: [https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- Descripción: Colección de mensajes SMS etiquetados como "ham" (no spam) o "spam".
- Idioma: Inglés. Para mejores resultados, ingresa/convierte los textos a inglés.

## Objetivo

Construir un clasificador capaz de predecir si un mensaje es spam (1) o no (0), optimizando el desempeño en datos desbalanceados y facilitando su uso con una interfaz sencilla.

## Requisitos e instalación

- Python 3.9+ recomendado.
- Paquetes principales: pandas, scikit-learn, imbalanced-learn, ipywidgets, joblib.

Instalación sugerida (en un entorno virtual):

```bash
pip install -r requirements.txt
# Si no tienes requirements.txt específico, instala:
pip install pandas scikit-learn imbalanced-learn ipywidgets joblib ipykernel
```

Habilitar ipywidgets (en algunos entornos Jupyter podría ser necesario):

```bash
pip install ipywidgets
```

## Qué hace cada notebook

1. 01_exploracion_analisis_limpieza.ipynb
   
   - Carga el dataset `data/spam.csv` (encoding latin-1; separador `;`).
   - Verifica tipos, nulos, duplicados y balance de clases.
   - Analiza la longitud de mensajes por clase.
   - Elimina duplicados y guarda `data/spam_clean.csv`.

2. 02_test_train_validation.ipynb
   
   - Vectoriza los textos con TF-IDF:
     - lowercase, strip_accents, stop_words='english', ngram_range=(1,2), norm='l2'.
   - Divide en Train/Test (80/20) con estratificación.
   - Entrena un modelo base de Regresión Logística y evalúa métricas (accuracy, classification_report) y matriz de confusión.
   - Aborda el desbalance con SMOTE (oversampling) y reentrena, mejorando la detección de la clase "spam" (mayor recall) con posible ajuste en precisión.

3. 03_pipline_final.ipynb
   
   - Construye un Pipeline (imblearn) que integra: TF-IDF + SMOTE + LogisticRegression.
   - Entrena y revalida el desempeño.
   - Exporta el modelo en `spam_detect.pkl` con joblib para consumo directo.

4. 04_interactividad_app.ipynb
   
   - Carga robusta del modelo (`spam_detect.pkl`).
   - Interfaz con ipywidgets para escribir un mensaje y clasificarlo:
     - Checkbox para usar `predict_proba` si el modelo lo soporta.
     - Slider de umbral de decisión (threshold) para ajustar la sensibilidad.
     - Tarjeta de resultado con colores (verde/rojo), barra de probabilidad y vista previa.
     - Banner informativo (en verde) indicando:
       - El modelo puede equivocarse; revisar predicciones cercanas al umbral (±5 pp).
       - El modelo fue entrenado con textos en inglés; se recomienda ingresar/traducir el texto a inglés.

## Cómo reproducir paso a paso

1. Coloca `data/spam.csv` en la ruta indicada (formato UCI; ver enlace de la sección Dataset).
2. Ejecuta el notebook 01 para limpiar y generar `data/spam_clean.csv`.
3. Ejecuta el notebook 02 para entrenar y evaluar el modelo base y con SMOTE.
4. Ejecuta el notebook 03 para crear el pipeline final y guardar `spam_detect.pkl`.
5. Ejecuta el notebook 04 para usar la interfaz interactiva:
   - Corre las primeras celdas para cargar el modelo.
   - Escribe un mensaje (preferiblemente en inglés) y presiona "Clasificar".
   - Ajusta el umbral según tu tolerancia a falsos positivos/negativos.

## Notas y limitaciones

- Idioma: el dataset y el modelo están orientados a mensajes en inglés.
- Umbral: valores más bajos tienden a incrementar el recall de spam (más detecciones) a costa de mayor tasa de falsos positivos.
- Datos desbalanceados: se mitigó con SMOTE, pero el desempeño puede variar con otro dominio o distribución de datos.

---

Autor: Juan Acevedo
