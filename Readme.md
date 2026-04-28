🌱 AI-Based Crop Disease Detection System

🚀 Overview

This project is a low-cost smart farming solution that detects crop diseases using an AI-powered system.
A camera captures plant images → sends them to an API → AI analyzes → results are displayed with alerts.

---

🎯 Features

- 📷 Image capture using camera
- 🤖 AI-based disease detection (mock/real model)
- 📟 OLED display for results
- 🔴🟢 LED + 🔊 buzzer alerts
- 🌐 API-based processing
- 🌍 Supports Hindi + English output

---

🧠 System Flow

1. Press button
2. Camera captures crop image
3. Image sent to API
4. AI processes image
5. Disease + solution returned
6. Result displayed on OLED + alert triggered

---

⚙️ Hardware Used

- Raspberry Pi Zero 2 W
- Camera Module (CSI)
- OLED Display (SSD1306, I2C)
- Push Button
- LEDs (Red & Green)
- Buzzer
- Power Supply

---

💻 Software Stack

- Python
- OpenCV
- FastAPI (Backend API)
- NumPy, Pillow
- RPi.GPIO
- luma.oled

---

📁 Project Structure

api.py        # Backend API
device.py     # Raspberry Pi device code
README.md     # Project documentation

---

🔧 Installation & Setup

1️⃣ Install Backend (API)

pip install fastapi uvicorn pillow numpy

Run API:

uvicorn api:app --host 0.0.0.0 --port 8000

Open in browser:

http://localhost:8000/docs

---

2️⃣ Setup Device (Raspberry Pi)

pip install opencv-python requests RPi.GPIO luma.oled pillow

---

🔗 Connect Device to API

Edit in "device.py":

API_URL = "http://<YOUR-IP>:8000/predict"

Find your IP:

ipconfig   # Windows
ifconfig   # Linux

👉 Make sure both devices are on same WiFi

---

▶️ Run Device

python device.py

---

🧪 API Response Example

{
  "disease": "Leaf Blight",
  "confidence": 92.0,
  "solution": "Use copper fungicide",
  "solution_hi": "कॉपर फंगीसाइड का उपयोग करें"
}

---

⚠️ Important Notes

- AI model is currently mock-based for demo
- Replace with trained model for real use
- Camera & I2C must be enabled in Raspberry Pi
- Ensure stable power supply

---

🔥 Future Improvements

- Real trained AI model (PlantVillage dataset)
- Offline AI (TensorFlow Lite)
- Mobile app integration
- Voice assistant for farmers
- Cloud deployment

---

🏆 Hackathon Value

- Solves real agricultural problem
- Low-cost & scalable
- Easy to use for farmers
- Combines IoT + AI

---

👨‍💻 Authors

- Vrishabh Deshmukh
- Team name- RUBICS

---

📌 Final Note

This is a working MVP designed for demonstration and further development into a real-world smart agriculture product.
