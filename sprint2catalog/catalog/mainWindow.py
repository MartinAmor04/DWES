from tkinter import messagebox
import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk 
from cell import Cell
from detail_window import DetailWindow
from tkinter import Label, Menu


    
#Funcion que devuelve la imagen de cada item del json    
def load_image_from_url(url):
    response = requests.get(url)
    image_data = Image.open(BytesIO(response.content))
    image = ImageTk.PhotoImage(image_data)
    return image


class MainWindow():

    def on_button_clicked(self, name, description, image):
        detail_window = DetailWindow(self.root, name, description, image)
    
    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Soy yo")

    def __init__(self, root, json_data):
        
        #Variables
        self.root = root
        root.title("MainWindow")
        self.cells = []

        #Centrar la self.root
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2 
        self.root.geometry(f"+{int(x)}+{int(y)}")

        labels = []
        #Bucle para recorrer todos los items del JSON descargado y añadirlo a la celda
        for item in json_data:
            
            #Guardamos en variables cada elemento del item del JSON
            name = item["name"]
            description = item["description"]
            image_url = item["image_url"]
            image = load_image_from_url(image_url)

            #creamos una nueva variable celda con los datos de la variable de arriba y la añadimos al array donde estarán todas las celdas
            cell = Cell(name, description, image_url, image)
            self.cells.append(cell)


            label = Label(root, image=cell.image, text=name, compound=tk.BOTTOM) 
            label.grid(row=0, column=len(labels))
            label.bind("<Button-1>", lambda event, cell=cell, name=name, description=description, image=image: self.on_button_clicked(name, description, image))
            labels.append(label)
            
        # Crear un menú
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        # Crear el menú 'Ayuda' y su elemento 'Acerca de'
        menu_ayuda = Menu(menu_bar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
