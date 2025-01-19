import cv2
import numpy as np
import pyautogui
import os
import subprocess  # Importa la biblioteca subprocess para ejecutar scripts externos

def perform_action_for_image(image_name):
    if image_name == "pruva.PNG":
        # Si la imagen encontrada es "pruva.PNG", ejecuta el script "pruva.py"
        subprocess.run(["python", "pruva.py"])
    else:
        # Capturar la pantalla
        screenshot = pyautogui.screenshot()

        # Convertir la captura en un formato compatible con OpenCV
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Inicializar variables de seguimiento
        found_match = False
        found_in_any_folder = False
        selected_folder_coordinates = None

        # Diccionario que asigna las carpetas a las coordenadas de clic correspondientes
        folder_coordinates = {
            "4-24": (1042, 500),
            "4-25": (425, 706),
            "4-26": (340, 710),
            "4-27": (1044, 351),
            "4-28": (430, 700),
            "5-24": (460, 35),
            "5-25": (1043, 329),
            "5-26": (58, 525),
            "5-27": (460, 710),
            "5-28": (55, 400),
            "6-24": (1042, 340),
            "6-25": (715, 715),
            "6-26": (478, 44),
            "6-27": (474, 54),
            "6-28": (60, 347),
            "7-24": (460, 35),
            "7-25": (1034, 606),
            "7-26": (52, 354),  # Agrega las coordenadas para 7-26
            "8-25": (462, 35),  # Agrega las coordenadas para 8-25
            "8-26": (55, 401),  # Agrega las coordenadas para 8-26
            "ENE": (1268, 705)
            # Define las coordenadas para cada carpeta aquí
        }

    # Iterar a través de las carpetas y las imágenes de referencia dentro de ellas
    for folder_name, click_coordinates in folder_coordinates.items():
        reference_images_directory = f"reference_images_{folder_name}"
        # Variable para rastrear si se encontró una coincidencia en la carpeta actual
        found_match_in_folder = False

        for filename in os.listdir(reference_images_directory):
            if filename.endswith(".PNG"):
                reference_image_path = os.path.join(
                    reference_images_directory, filename)
                reference_image = cv2.imread(reference_image_path)

                # Buscar coincidencias entre la captura de pantalla y la imagen de referencia
                result = cv2.matchTemplate(
                    screenshot_cv, reference_image, cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                locations = np.where(result >= threshold)

                # Si se encontró una coincidencia, realizar clic en la ubicación de la coincidencia
                if locations[0].size > 0:
                    print(
                        f"Coincidencia encontrada en {filename} de la carpeta {folder_name}. Realizando clic...")
                    # Realiza el clic donde se encontró la coincidencia
                    pyautogui.click(locations[1][0], locations[0][0])
                    found_match = True
                    found_match_in_folder = True
                    # Almacena las coordenadas de la carpeta encontrada
                    selected_folder_coordinates = click_coordinates
                    break  # Sal del bucle si se encuentra una coincidencia en la carpeta

        # # Si se encontró una coincidencia en la carpeta actual, no es necesario continuar buscando en otras carpetas
        # if found_match_in_folder:
        #     found_in_any_folder = True
        #     break

    # Si no se encontró ninguna coincidencia, realizar clic en coordenadas de la carpeta encontrada
    if not found_match:
        print(f"No se encontraron más coincidencias. Realizando clic en coordenadas de la carpeta encontrada...")
        # Obtén el nombre de la carpeta correspondiente a la imagen
        folder_name = image_name.split(".")[0]

        # Obtén las coordenadas de la carpeta
        click_coordinates = folder_coordinates[folder_name]
        # Realiza el clic
        pyautogui.click(*click_coordinates)
