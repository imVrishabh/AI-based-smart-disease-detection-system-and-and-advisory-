from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np

app = FastAPI()

# ---------------- FAKE AI MODEL ----------------
def predict_disease(image):
    img = Image.open(image).resize((224, 224))
    img = np.array(img)

    # Simple mock logic (replace later)
    avg = np.mean(img)

    if avg < 100:
        return "Leaf Blight", 0.92
    elif avg < 150:
        return "Rust", 0.85
    else:
        return "Healthy", 0.95

# ---------------- SOLUTIONS ----------------
solutions = {
    "Leaf Blight": "Use copper fungicide",
    "Rust": "Use sulfur spray",
    "Healthy": "No action needed"
}

solutions_hi = {
    "Leaf Blight": "कॉपर फंगीसाइड का उपयोग करें",
    "Rust": "सल्फर स्प्रे का उपयोग करें",
    "Healthy": "कोई समस्या नहीं"
}

# ---------------- API ----------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    disease, confidence = predict_disease(file.file)

    return {
        "disease": disease,
        "confidence": round(confidence * 100, 2),
        "solution": solutions[disease],
        "solution_hi": solutions_hi[disease]
    }
