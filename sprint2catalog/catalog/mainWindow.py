from tkinter import Canvas, Frame, Grid, Scrollbar, messagebox
import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk 
from cell import Cell
from detail_window import DetailWindow
from tkinter import Label, Menu


    
#Funcion que devuelve la imagen de cada item del json    
def load_and_resize_image(url, width, height):
    response = requests.get(url)
    image_data = Image.open(BytesIO(response.content))
    resized_image = image_data.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


class MainWindow():

    def on_button_clicked(self, name, description, image):
        detail_window = DetailWindow(self.root, name, description, image)
    
    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Soy yo")
    
  

    def __init__(self, root, json_data):
        
        #Variables
        self.root = root
        self.root.resizable(False, False)
        root.title("MainWindow")
        self.cells = []
        
        #Centrar la self.root
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2 
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
        self.canvas = Canvas (self.root)
        self.scrollbar = Scrollbar (self.root, orient="vertical", command=self.canvas. yview)
        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas. configure(yscrollcommand=self.scrollbar.set)
        
        for cell in enumerate(self.cells):
            self.add_item (cell)
        
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar. grid(row=0, column=1, sticky="ns")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        def add_item(self, cell):
            frame = Frame (self.scrollable_frame)
            frame. pack (pady=10)
            label = Label (frame, image=cell.image_tk, text=cell.title, compound=tk. BOTTOM)
            label. grid (row=0, column=0)
            
            label. bind ("‹Button-1›", lambda event, clickedCell=cell: showDetail(clickedCell))
            label.bind("<Configure>", lambda e: label.place(x=(self.root.winfo_width() - label.winfo_reqwidth()) / 2, y=(self.root.winfo_height() - label.winfo_reqheight()) / 2))

        labels = []
        #Bucle para recorrer todos los items del JSON descargado y añadirlo a la celda
        for item in json_data:
            
            #Guardamos en variables cada elemento del item del JSON
            name = item["name"]
            description = item["description"]
            image_url = item["image_url"]
            image = load_and_resize_image(image_url, 300, 300)

    

            #creamos una nueva variable celda con los datos de la variable de arriba y la añadimos al array donde estarán todas las celdas
            cell = Cell(name, description, image_url, image)
            self.cells.append(cell)


            labels.append(Label(
                self.scrollable_frame, 
                image=cell.image, 
                text=name, 
                compound=tk.BOTTOM,
                width=250,  # Añadido: Fijar el ancho de la etiqueta
                height=500   # Añadido: Fijar el alto de la etiqueta
            ))
            labels[-1].bind("<Button-1>", lambda event, cell=cell, name=name, description=description, image=image: self.on_button_clicked(name, description, image))
            labels[-1].pack(pady=10)
        
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
       
            
        # Crear un menú
        menu_bar = Menu(root)
        root.config(menu=menu_bar)

        # Crear el menú 'Ayuda' y su elemento 'Acerca de'
        menu_ayuda = Menu(menu_bar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
