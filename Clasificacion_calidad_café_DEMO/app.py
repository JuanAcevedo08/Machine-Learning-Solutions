import gradio as gr
from joblib import load

#Cargo el modelo previamente entrenado 
model = load('coffe_model.joblib')

def classify(acidity, aroma, body):
    prediction = model.predict([[acidity, aroma, body]])
    return f"☕ Este café es de tipo: {prediction[0]}"

# Interfaz con Gradio
demo = gr.Interface(
    fn=classify,
    inputs=[
        gr.Slider(1, 10, value=5, label="Acidez"),
        gr.Slider(1, 10, value=5, label="Aroma"),
        gr.Slider(1, 10, value=5, label="Cuerpo")
    ],
    outputs="text",
    title="Clasificador de Café ☕",
    description="Un modelo de Árbol de Decisión entrenado para clasificar café según sus características sensoriales."
)

if __name__ == "__main__":
    demo.launch()