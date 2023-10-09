from tkinter import  ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from PIL import Image, ImageTk

class MainWindow():
    
    def onButtonClicked(self, cell):
        message="Has hecho click  en la celda"+ cell.title
        messagebox.showinfo("Información"+ message) 

    def __init__(self, root):
        root.title("Peliculas")

        self.cells=[
            Cell("Imagen 1", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\apocalypse-now-.jpg"),
            Cell("Imagen 2", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\evangelion.jpg"),
            Cell("Imagen 3", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\le haine.jpg"),
            Cell("Imagen 4 ", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\the lighthouse.jpg"),
            Cell("Imagen 5", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\the lobster.jpg")
        ]

        for i, cell in enumerate(self.cells):
            foto = Image.open(cell.path)
            img = foto.resize((100, 100), Image.Resampling.LANCZOS)

            cell.image_tk = ImageTk.PhotoImage(img)

            label= ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, celda = cell: self.onButtonClicked(cell))


   
        