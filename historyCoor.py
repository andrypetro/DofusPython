import pyautogui
import time

def mostrar_coordenadas():
    try:
        while True:
            # Obtener las coordenadas actuales del mouse
            x, y = pyautogui.position()

            # Imprimir las coordenadas en la consola
            print(f"Coordenadas del mouse: X = {x}, Y = {y}")

            # Esperar un breve periodo de tiempo para evitar imprimir demasiado rápido
            time.sleep(0.5)
    except KeyboardInterrupt:
        # Manejar la interrupción del teclado (Ctrl+C) para salir del bucle
        print("¡Script detenido!")

# Llamar a la función para mostrar las coordenadas
mostrar_coordenadas()
