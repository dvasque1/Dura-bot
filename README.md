
# DURA Bot 🤖📦

Este es el bot oficial del modelo D.U.R.A. (Disciplina, Última milla, Responsabilidad y Atención), diseñado para funcionar en WhatsApp a través de Twilio y desplegado fácilmente en Render.

---

## 🚀 ¿Qué incluye este repositorio?

- `app.py` – Lógica principal del bot (Flask)
- `requirements.txt` – Dependencias necesarias
- `Procfile` – Archivo para despliegue en Render
- `render.yaml` – Configuración para despliegue automático

---

## 📦 ¿Cómo desplegar el bot en Render?

1. **Sube estos archivos a un nuevo repositorio en GitHub**
2. Entra a [https://render.com](https://render.com)
3. Crea un **nuevo Web Service**
4. Conecta tu repositorio y selecciona:
   - **Start command**: `python app.py`
5. Render generará una URL del tipo:
   ```
   https://dura-bot.onrender.com/webhook
   ```

---

## 💬 Conectar con Twilio WhatsApp

1. Ve a [Twilio Sandbox for WhatsApp](https://www.twilio.com/console/sms/whatsapp/sandbox)
2. Pega la URL de Render en el campo:
   ```
   WHEN A MESSAGE COMES IN
   ```
3. Ejemplo:
   ```
   https://dura-bot.onrender.com/webhook
   ```

4. Haz clic en **Save**
5. Luego desde WhatsApp, envía un mensaje al número sandbox de Twilio (+1 415 523 8886)

---

## 📞 Migrar a número real

Para salir del sandbox y usar un número propio de WhatsApp:
- Habilita la API oficial de WhatsApp Business
- Verifica tu empresa en Meta Business Manager
- Asocia tu número real y conéctalo desde Twilio Console

---

## 📌 Contacto

Este proyecto fue creado por el equipo de DURA Bot con propósito educativo y de soporte logístico en operaciones de reparto.
