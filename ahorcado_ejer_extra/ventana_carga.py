import json
import tkinter as tk
import requests

from ventana_juego import JuegoAhorcado


class Ventana_carga:
    def __init__(self, root):
        self.cargar_JSON_palabras()
        self.cargar_JSON_imagenes()
        
    
    def cargar_JSON_palabras(self):
        try:
            response = requests.get("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/JSON_palabras")
            if response.status_code == 200:
                self.json_data_palabras = json.loads(response.text)
                print("JSON cargado con éxito.")
            else:
                print("Error al cargar el JSON.")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
    
    def cargar_JSON_imagenes(self):
        try:
            response = requests.get("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/JSON_Imagenes")
            if response.status_code == 200:
                self.json_data_imagenes = json.loads(response.text)
                print("JSON de imágenes cargado con éxito.")
            else:
                print("Error al cargar el JSON de imágenes.")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión al cargar el JSON de imágenes: {e}")
    
    def launch_ventana_juego(self,json_data_imagenes,json_data_palabras):
        root=tk.Tk()
     
        app=JuegoAhorcado(root,json_data_imagenes,json_data_palabras)
        root.mainloop()
    
    


