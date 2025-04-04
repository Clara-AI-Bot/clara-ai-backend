from TTS.api import TTS
import os
from utils import download_if_missing

# Descargar modelo y config si no están
download_if_missing(
    url="https://github.com/Clara-AI-Bot/clara-ai-backend/releases/download/v1.0.0/model.pth",
    output_path="model/model.pth"
)

download_if_missing(
    url="https://github.com/Clara-AI-Bot/clara-ai-backend/releases/download/v1.0.0/config.json",
    output_path="model/config.json"
)

# Inicializar TTS
tts = TTS(
    config_path="model/config.json",
    model_path="model",
    gpu=True
)

# Ejecutar síntesis de voz
tts.tts_to_file(
    text="Hola, soy Clara, tu asistente de voz inteligente.",
    speaker_wav="voz_clara.wav",
    file_path="salida.wav",
    language="es"
)
