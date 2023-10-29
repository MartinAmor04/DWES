from io import BytesIO
import random
import tkinter as tk
import tkinter
from tkinter import  messagebox
from PIL import Image, ImageTk 


import requests

def load_and_resize_image(url, width, height):
    response = requests.get(url)
    image_data = Image.open(BytesIO(response.content))
    resized_image = image_data.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

class JuegoAhorcado:
    
    def __init__(self, json_data_palabras, image):
       
        self.json_data_palabras = json_data_palabras
        self.image = image
        self.palabra_a_adivinar = self.obtener_palabra_aleatoria(self.json_data_palabras[self.dificultad])
        self.palabra_adivinada = ['_'] * len(self.palabra_a_adivinar)
        self.letras_intentadas = []
        self.errores = 0
        self.construir_interfaz()

    def obtener_palabra_aleatoria(palabras):
        return random.choice(palabras)

    def construir_interfaz(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

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

    def reiniciar_juego(self):
        self.frame.destroy()
        self.__init__(self.master, self.dificultad)
    
    def iniciar_juego(self, dificultad):
        self.withdraw()
        JuegoAhorcado(self, dificultad)



    



