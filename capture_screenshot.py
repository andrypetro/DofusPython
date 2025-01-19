#capturescreenshot.py
import cv2
import pyautogui
import numpy as np

def capture_screenshot():
    # Capturar la pantalla
    screenshot = pyautogui.screenshot()

    # Convertir la captura en un formato compatible con OpenCV
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    return screenshot_cv