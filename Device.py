import cv2
import requests
import time
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

# ---------------- GPIO ----------------
BUTTON = 5
RED = 17
GREEN = 27
BUZZER = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

# ---------------- OLED ----------------
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

def show_text(text):
    img = Image.new("1", (128, 64))
    draw = ImageDraw.Draw(img)
    draw.text((5, 20), text, fill=255)
    device.display(img)

# ---------------- ALERT ----------------
def beep():
    GPIO.output(BUZZER, True)
    time.sleep(0.3)
    GPIO.output(BUZZER, False)

def success():
    GPIO.output(GREEN, True)
    GPIO.output(RED, False)
    beep()

def error():
    GPIO.output(RED, True)
    GPIO.output(GREEN, False)
    beep()

# ---------------- API ----------------
API_URL = "http://<YOUR-IP>:8000/predict"

# ---------------- CAMERA ----------------
camera = cv2.VideoCapture(0)

show_text("Ready")

while True:
    if GPIO.input(BUTTON):
        show_text("Capturing...")

        ret, frame = camera.read()
        if ret:
            cv2.imwrite("crop.jpg", frame)

            show_text("Sending...")

            try:
                files = {"file": open("crop.jpg", "rb")}
                res = requests.post(API_URL, files=files)
                data = res.json()

                disease = data["disease"]

                show_text(disease[:15])
                print(data)

                success()

            except:
                show_text("API Error")
                error()
        else:
            show_text("Camera Error")
            error()

        time.sleep(2)
