from TTS.api import TTS
import os
from utils import download_if_missing

# Descargar modelo y config si no están
download_if_missing(
    url="https://huggingface.co/Willyromero/clara-ai-models/resolve/main/model.pth",
    output_path="model/model.pth"
)

download_if_missing(
    url="https://huggingface.co/Willyromero/clara-ai-models/resolve/main/config.json",
    output_path="model/config.json"
)

# Inicializar TTS
tts = TTS(
    config_path="model/config.json",
    model_path="model",
    gpu=True
)

# Ejecutar síntesis
tts.tts_to_file(
    text="Hola, soy Clara, tu asistente de voz inteligente.",
    speaker_wav="voz_clara.wav",
    file_path="salida.wav",
    language="es"
)