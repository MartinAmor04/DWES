from tkinter import  ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow():
    
    def onButtonClicked(self, cell):
        message="Has hecho click  en la celda"+ cell.title
        messagebox.showinfo("Información"+ message) 

    def __init__(self, root):
        root.title("MainWindow")
        
        self.cells=[
            Cell("Imagen 1", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\edited\\apocalypse-now-(edited).jpg"),
            Cell("Imagen 2", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\edited\\evangelion(edited).jpg"),
            Cell("Imagen 3", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\edited\\le haine(edited).jpg"),
            Cell("Imagen 4 ", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\edited\\the lighthouse(edited).jpg"),
            Cell("Imagen 5", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\edited\\the lobster(edited).jpg")


        ]

        for i,cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))

   
        