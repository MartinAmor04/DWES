from io import BytesIO
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

import requests

# Aquí debes cargar las palabras desde un archivo JSON en GitHub
# y realizar otras configuraciones necesarias

def cargar_JSON_imagenes():
    try:
        response = requests.get("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/JSON_Imagenes")
        if response.status_code == 200:
            json_data_imagenes = json.loads(response.text)
            print("JSON de imágenes cargado con éxito.")
            return {int(item["errores"]): item["imagen_url"] for item in json_data_imagenes}
        else:
            print("Error al cargar el JSON de imágenes.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión al cargar el JSON de imágenes: {e}")
        return None


# Aquí debes cargar las imágenes desde GitHub y realizar otras configuraciones necesarias

class JuegoAhorcado:
    def __init__(self, master, dificultad):
        self.master = master
        self.dificultad = dificultad
        self.errores = 0
        self.json_data_imagenes = cargar_JSON_imagenes()
        self.imagenes_ahorcado = {
           0: self.load_and_resize_image("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/ahorcado_imagen_1.jpg", 200, 200),
            1: self.load_and_resize_image("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/ahorcado_imagen_2.jpg", 200, 200),
            2: self.load_and_resize_image("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/ahorcado_imagen_3.jpg", 200, 200),
            3: self.load_and_resize_image("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/ahorcado_imagen_4.jpg", 200, 200),
            4: self.load_and_resize_image("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/ahorcado_imagen_5.jpg", 200, 200),
            5: self.load_and_resize_image("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/ahorcado_imagen_6.jpg", 200, 200)
        }
        self.frame = tk.Frame(self.master)  # Crear el marco aquí
        self.frame.pack()
        self.imagen_label = tk.Label(self.frame)
        self.imagen_label.pack()
        self.actualizar_imagen()
        self.palabra_a_adivinar = self.obtener_palabra_aleatoria()
        self.palabra_adivinada = ['_' for _ in self.palabra_a_adivinar]
        self.letras_intentadas = []
        self.errores = 0
        self.construir_interfaz()

    def cargar_JSON_palabras():
        try:
            response = requests.get("https://raw.githubusercontent.com/MartinAmor04/DWES/main/ahorcado_ejer_extra/JSON_palabras")
            if response.status_code == 200:
                json_data_palabras = json.loads(response.text)
                print("JSON cargado con éxito.")
                return {item["dificultad"]: item["palabras"] for item in json_data_palabras}
            else:
                print("Error al cargar el JSON.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
            return None

    def obtener_palabra_aleatoria(self):
        json_data_palabras = JuegoAhorcado.cargar_JSON_palabras()
        if self.dificultad == 'Facil':
            palabras = json_data_palabras['Facil']
        elif self.dificultad == 'Normal':
            palabras = json_data_palabras['Normal']
        elif self.dificultad == 'Dificil':
            palabras = json_data_palabras['Dificil']
        else:
            raise ValueError("Dificultad no válida")
        return random.choice(palabras)

    def construir_interfaz(self):
        self.imagen_label = tk.Label(self.frame)
        self.imagen_label.pack()
        self.actualizar_imagen()
        self.label_palabra = tk.Label(self.frame, text=' '.join(self.palabra_adivinada), font=('Arial', 24))
        self.label_palabra.pack()

        self.label_intentos = tk.Label(self.frame, text=f'Intentos: {self.errores}/6', font=('Arial', 12))
        self.label_intentos.pack()

        self.label_letras_intentadas = tk.Label(self.frame, text='Letras intentadas:', font=('Arial', 12))
        self.label_letras_intentadas.pack()

        self.entry_letra = tk.Entry(self.frame, font=('Arial', 16), width=3)
        self.entry_letra.pack()

        self.boton_adivinar = tk.Button(self.frame, text='Adivinar', command=self.adivinar_letra, font=('Arial', 12))
        self.boton_adivinar.pack()

    def adivinar_letra(self):
        letra = self.entry_letra.get()
        self.entry_letra.delete(0, tk.END)
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letras_intentadas:
                messagebox.showinfo('Atención', 'Ya has intentado esta letra antes.')
            else:
                self.letras_intentadas.append(letra)
                if letra in self.palabra_a_adivinar:
                    for i in range(len(self.palabra_a_adivinar)):
                        if self.palabra_a_adivinar[i] == letra:
                            self.palabra_adivinada[i] = letra
                    self.label_palabra.config(text=' '.join(self.palabra_adivinada))
                else:
                    self.errores += 1
                    self.label_intentos.config(text=f'Intentos: {self.errores}/6')
                    # Aquí debes añadir la lógica para actualizar la imagen del ahorcado
                self.label_letras_intentadas.config(text=f'Letras intentadas: {", ".join(self.letras_intentadas)}')
                self.verificar_estado_juego()
        else:
            messagebox.showerror('Error', 'Ingresa una letra válida.')

    def verificar_estado_juego(self):
        if self.errores >= 6:
            messagebox.showinfo('Fin del juego', f'Has perdido. La palabra era {self.palabra_a_adivinar}.')
            self.reiniciar_juego()
        elif '_' not in self.palabra_adivinada:
            messagebox.showinfo('Fin del juego', '¡Has ganado!')
            self.reiniciar_juego()
    
    def actualizar_imagen(self):
        imagen_url = self.imagenes_ahorcado.get(self.errores)
        if imagen_url:
            imagen = self.load_and_resize_image(imagen_url, 200, 200)
            self.imagen_label.img = imagen  # Mantén una referencia a la imagen para evitar que se elimine de la memoria
            self.imagen_label.config(image=imagen)
    
    @staticmethod
    def load_and_resize_image(url, width, height):
        response = requests.get(url)
        image_data = Image.open(BytesIO(response.content))
        resized_image = image_data.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def reiniciar_juego(self):
        self.frame.destroy()
        self.__init__(self.master, self.dificultad)

def iniciar_juego(dificultad):
    root.withdraw()
    ventana_juego = tk.Tk()
    ventana_juego.title("Juego del Ahorcado")
    juego = JuegoAhorcado(ventana_juego, dificultad)
    ventana_juego.mainloop()
    root.deiconify()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Ventana de Selección")
    tk.Label(root, text="Seleccione la dificultad:", font=('Arial', 16)).pack()
    tk.Button(root, text="Fácil", command=lambda: iniciar_juego('Facil'), font=('Arial', 12)).pack()
    tk.Button(root, text="Normal", command=lambda: iniciar_juego('Normal'), font=('Arial', 12)).pack()
    tk.Button(root, text="Difícil", command=lambda: iniciar_juego('Dificil'), font=('Arial', 12)).pack()
    tk.Button(root, text="Salir", command=root.quit, font=('Arial', 12)).pack()
    root.mainloop()