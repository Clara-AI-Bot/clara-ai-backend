import os
from TTS.api import TTS
import gradio as gr

from utils import download_if_missing

# 1. Descargar modelo y config si no están
download_if_missing(
    url="https://github.com/Clara-AI-Bot/clara-ai-backend/releases/download/v1.0.0/model.pth",
    output_path="model/model.pth"
)

download_if_missing(
    url="https://github.com/Clara-AI-Bot/clara-ai-backend/releases/download/v1.0.0/config.json",
    output_path="model/config.json"
)

# 2. Inicializar TTS
tts = TTS(
    config_path="model/config.json",
    model_path="model/model.pth",
    gpu=True
)

# 3. Función para sintetizar
def synthesize(text):
    # generamos el audio temporalmente en 'salida.wav'
    tts.tts_to_file(
        text=text,
        speaker_wav="voz_clara.wav",
        file_path="salida.wav",
        language="es"
    )
    return "salida.wav"

# 4. Interfaz con Gradio
demo = gr.Interface(
    fn=synthesize,
    inputs="text",
    outputs="audio",
    title="Clara AI - Demo TTS",
    description="Escribe un texto y escucha la voz clonada de Clara."
)

if __name__ == "__main__":
    # Escucha en 0.0.0.0:7860
    demo.launch(server_name="0.0.0.0", server_port=7860)
