# Predicción de Nota Final en la Materia de Portugués

## Estructura del Proyecto

```
Prediccion Nota Portugues/
├── data/
│   └── student-por.csv         # Dataset principal
├── notebooks/
│   ├── 01_exploracion_analisis_limpieza.ipynb   # Exploración y limpieza de datos
│   ├── 02_test_model.ipynb                      # Entrenamiento y validación de modelos
│   └── 03_pipline_final.ipynb                   # Pipeline final e interfaz interactiva
├── readme.md                  # Documentación del proyecto
├── requirements.txt           # Dependencias necesarias
```

Este proyecto tiene como objetivo predecir la nota final (G3) de estudiantes en la materia de portugués, utilizando técnicas de Machine Learning. El trabajo se realizó sobre el dataset `student-por.csv`, el cual contiene información detallada de estudiantes de secundaria en Portugal.

## Contexto del Dataset

El dataset proviene de la base de datos pública [Kaggle - Student Performance Data Set](https://www.kaggle.com/datasets/larsen0966/student-performance-data-set). Contiene datos de estudiantes de dos escuelas portuguesas, con variables demográficas, académicas, familiares y sociales. Cada fila representa un estudiante y su desempeño en la materia de portugués, incluyendo las notas de los tres periodos (G1, G2, G3).

- **Variables principales:**

  - `G1`, `G2`: Notas de los primeros dos periodos.
  - `G3`: Nota final (variable objetivo).
  - Variables sobre familia, hábitos, apoyo escolar, salud, ausencias, etc.

## Objetivo del Proyecto

El propósito es construir un modelo capaz de predecir la nota final (G3) de un estudiante, a partir de sus características y desempeño previo. Esto puede ayudar a identificar estudiantes en riesgo y orientar intervenciones educativas.

## Proceso Realizado

El proyecto se desarrolló en tres etapas principales, cada una documentada en un notebook:

### 1. Exploración, Análisis y Limpieza de Datos

- Se cargó el dataset y se revisaron los tipos de variables, valores nulos y duplicados.
- Se realizó análisis descriptivo y gráfico para entender la distribución y correlaciones entre variables.
- Se identificó que las notas de los periodos anteriores (`G1`, `G2`) y el número de materias reprobadas (`failures`) son las variables más correlacionadas con la nota final.

### 2. Entrenamiento y Validación de Modelos

- Se transformaron variables categóricas a numéricas (one-hot encoding).
- Se probaron modelos de regresión lineal y se evaluó el desempeño con todas las variables.
- Se aplicaron técnicas de selección de características (SelectKBest, árbol de decisión) para identificar las variables más relevantes.
- Se concluyó que el modelo funciona mejor utilizando solo `G2`, `G1` y `failures`.

### 3. Pipeline Final e Interactividad

- Se construyó un pipeline que integra la estandarización y el modelo de regresión lineal.
- Se validó el modelo en el conjunto de test, obteniendo métricas como MAE y R2.
- Se implementó una interfaz interactiva con `ipywidgets` para que el usuario pueda ingresar las notas de los periodos anteriores y el número de materias reprobadas, obteniendo la predicción de la nota final.

## Resultados Obtenidos

- El modelo logra predecir la nota final con un error promedio (MAE) cercano a 1 punto, y un buen ajuste (R2).
- Las variables más influyentes son las notas previas y el historial de materias reprobadas.
- El pipeline permite una predicción rápida y sencilla, útil para aplicaciones educativas.

## Uso del Proyecto

1. Instalar las dependencias listadas en `requirements.txt`.
2. Ejecutar los notebooks en la carpeta `notebooks/` para explorar el análisis, entrenamiento y probar la interfaz interactiva.
3. El usuario puede modificar los valores de entrada en el último notebook para obtener predicciones personalizadas.

## Conclusión

Este proyecto demuestra cómo, a partir de datos escolares, es posible construir modelos predictivos útiles para la educación. El análisis detallado y la selección de variables permitieron mejorar el desempeño del modelo y facilitar su uso práctico.

---
**Autor:** Juan Acevedo
