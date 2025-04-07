# Clara AI – Dockerfile de producción (XTTSv2 con speaker_wav)
FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

# 1. Instala librerías del sistema
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# 2. Establece directorio de trabajo
WORKDIR /app

# 3. Copia el backend completo
COPY . .

# 4. Instala Coqui TTS desde rama dev
RUN git clone https://github.com/coqui-ai/TTS.git && \
    cd TTS && git checkout dev && pip install -e . && cd ..

# 5. Instala dependencias del proyecto
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Expone el puerto de Gradio
EXPOSE 7860

# 7. Ejecuta la app
CMD ["python", "app.py"]
