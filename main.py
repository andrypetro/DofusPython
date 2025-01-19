# main.py
import cv2
import numpy as np
import pyautogui
import os
import time
# Importa la función desde actions.py
from actions import perform_action_for_image


def main():
    # Directorio que contiene las imágenes de referencia
    reference_images_directory = "reference_images"

    while True:
        # Capturar la pantalla
        screenshot = pyautogui.screenshot()

        # Convertir la captura en un formato compatible con OpenCV
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Recorrer todas las imágenes de referencia en el directorio
        for filename in os.listdir(reference_images_directory):
            # Asegúrate de que coincida con la extensión correcta
            if filename.endswith(".PNG"):
                # Construir la ruta completa de la imagen de referencia
                reference_image_path = os.path.join(
                    reference_images_directory, filename)

                # Cargar la imagen de referencia
                reference_image = cv2.imread(reference_image_path)

                # Realizar la comparación utilizando cv2.matchTemplate
                result = cv2.matchTemplate(
                    screenshot_cv, reference_image, cv2.TM_CCOEFF_NORMED)

                # Definir un umbral de coincidencia (puedes ajustarlo según tus necesidades)
                threshold = 0.8

                # Encontrar las ubicaciones donde la imagen de referencia coincide con la captura
                locations = np.where(result >= threshold)

                # Si se encontró una coincidencia, muestra el nombre de la imagen y realiza la acción correspondiente
                if locations[0].size > 0:
                    print(f"Coincidencia encontrada: {filename}")
                    # Llama a la función desde actions.py
                    perform_action_for_image(filename)

        # Pausa entre capturas (ajusta según tus necesidades)
        time.sleep(1)


if __name__ == "__main__":
    main()  # Llama a la función main sin el punto al fina
