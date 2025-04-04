# Clara AI – Backend de Inferencia por Voz (XTTS v2)

![Clara AI](https://img.shields.io/badge/voz-ultra%20natural-brightgreen)
![XTTSv2](https://img.shields.io/badge/modelo-XTTSv2-blue)
![Status](https://img.shields.io/badge/estado-produccion-orange)

Este repositorio permite lanzar la voz clonada de Clara AI en minutos, ideal para integraciones SaaS, pruebas B2B y despliegue en GPU vía RunPod, Paperspace o Docker.

---

## 🌟 Objetivo

Proveer un backend ligero y flexible para sintetizar voz ultra humana en español peninsular usando el modelo XTTS v2 y una muestra real de voz clonada.

Perfecto para:
- Llamadas automatizadas ultra naturales
- Demos de producto sin latencia
- Integraciones vía API

---

## 🚀 Cómo ejecutarlo (entorno local o cloud)

```bash
# 1. Clona el repositorio
 git clone https://github.com/Clara-AI-Bot/clara-ai-backend.git
 cd clara-ai-backend

# 2. Instala las dependencias
 pip install -r requirements.txt

# 3. Ejecuta el backend de voz
 python app.py
```

---

## 🔧 Estructura del proyecto

| Archivo / Carpeta      | Descripción |
|------------------------|-------------|
| `app.py`               | Backend principal: convierte texto a voz usando XTTS v2 |
| `voz_clara.wav`        | Muestra de voz clonada (16kHz, mono) usada como `speaker_wav` |
| `requirements.txt`     | Librerías necesarias para correr el sistema |
| `utils.py`             | Funciones auxiliares para descarga y setup |
| `model/`               | Carpeta vacía donde se descargan `model.pth` y `config.json` |
| `LICENSE.md`           | Licencia personalizada: uso privado, no comercial |
| `Dockerfile`           | Imagen base opcional para despliegue |

---

## 💪 Uso vía Docker (opcional)

```bash
# Construye la imagen
 docker build -t clara-ai .

# Lanza la inferencia por voz
 docker run -p 7860:7860 clara-ai
```

---

## 🤝 Integración con SaaS (vía API)

Este backend está listo para integrarse con:
- Latenode (webhooks HTTP)
- CRMs como GoHighLevel o Zapier
- Tu propia interfaz vía fetch, axios o curl

Puedes adaptarlo fácilmente usando FastAPI o Flask si deseas exponer endpoints REST.

---

## 🎤 Sobre la voz de Clara

Esta voz ha sido clonada a partir de audios grabados por una locutora profesional y refinados con ElevenLabs. Actualmente se usa un `.wav` limpio como entrada para XTTS v2, sin necesidad de embeddings ni entrenamiento adicional.

> Si deseas reentrenar la voz con múltiples audios, recomendamos usar otro repo paralelo y herramientas de `generate_embedding.py` + Coqui XTTS.

---

## © Licencia y uso

Este software está protegido por una licencia personalizada. No está permitido su uso comercial, reproducción o sublicencia sin autorización expresa.

Ver más en [`LICENSE.md`](./LICENSE.md)

---

## 🧱 Autor

Desarrollado por Willy Romero para Clara AI (Edommo).

Contacto: clara@edommo.com

