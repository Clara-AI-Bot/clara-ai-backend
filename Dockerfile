# Clara AI – Dockerfile de producción (XTTSv2 con speaker_wav)
FROM python:3.10-slim

# Evita prompts en instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias básicas
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Crea directorio de trabajo
WORKDIR /app

# Copia los archivos del backend al contenedor
COPY . /app

# Instala TTS desde la rama dev de Coqui
RUN git clone https://github.com/coqui-ai/TTS.git && \
    cd TTS && \
    git checkout dev && \
    pip install -e .

# Instala dependencias adicionales
RUN pip install -r requirements.txt

# Expone el puerto para Gradio
EXPOSE 7860

# Comando de inicio
CMD ["python", "app.py"]
