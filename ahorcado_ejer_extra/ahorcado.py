import tkinter as tk
from tkinter import Tk, messagebox
import random

import requests

# Aquí debes cargar las palabras desde un archivo JSON en GitHub
# y realizar otras configuraciones necesarias

def fetch_json_data(self):
    response = requests.get("https://raw.githubusercontent.com/MartinAmor04/DWES/main/Ejercicio%202.1")       
    if response.status_code == 200:
        self.json_data = response.json()
        self.finished=True

def launch_main_window(self,json_data):
    root=Tk()
    app=JuegoAhorcado(root,json_data)
    root.mainloop()    


# Aquí debes cargar las imágenes desde GitHub y realizar otras configuraciones necesarias

class JuegoAhorcado:
    def __init__(self, master, dificultad):
        self.master = master
        self.dificultad = dificultad
        self.palabra_a_adivinar = self.obtener_palabra_aleatoria()
        self.palabra_adivinada = ['_' for _ in self.palabra_a_adivinar]
        self.letras_intentadas = []
        self.errores = 0
        self.construir_interfaz()

    def obtener_palabra_aleatoria(self):
        # Aquí deberías escribir el código para obtener una palabra aleatoria
        # según la dificultad elegida del archivo JSON en GitHub.
        palabras_faciles = ['sol', 'mar', 'rio', 'casa', 'mesa']
        palabras_normales = ['coche', 'guitarra', 'elefante', 'nube', 'manzana']
        palabras_dificiles = ['universidad', 'esternocleidomastoideo', 'electroencefalografista', 'hipopotomonstrosesquipedaliofobia', 'desoxirribonucleico']
        if self.dificultad == 'Facil':
            return random.choice(palabras_faciles)
        elif self.dificultad == 'Normal':
            return random.choice(palabras_normales)
        elif self.dificultad == 'Dificil':
            return random.choice(palabras_dificiles)

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