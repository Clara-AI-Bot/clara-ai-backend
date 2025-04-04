# Clara AI - Backend de Inferencia por Voz

Este repositorio permite lanzar Clara AI en cuestión de minutos usando RunPod, Paperspace o Docker.

## 🚀 Cómo ejecutarlo

```bash
git clone https://github.com/TU_USUARIO/clara-ai-backend.git
cd clara-ai-backend
pip install -r requirements.txt
python app.py
```

## 🎤 Qué incluye

- `app.py`: script que genera voz a partir de texto.
- `voz_clara.wav`: muestra de voz clonada.
- `model/`: carpeta donde se descargarán `model.pth` y `config.json`.

## 📦 Uso con Docker

```bash
docker build -t clara-ai .
docker run --gpus all clara-ai
```

## ✅ Requisitos

- Python 3.10+
- GPU con soporte CUDA (si usas inferencia acelerada)
- Conexión a internet (para descargar el modelo si no está)