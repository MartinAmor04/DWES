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
            Cell("Imagen 1", "C:\\Users\marti\\Downloads\\c33cd6ec-a7b3-4289-95b5-ab614131fd2c.jpeg"),
            Cell("Imagen 2", "C:\\Users\marti\\Downloads\\c33cd6ec-a7b3-4289-95b5-ab614131fd2c.jpeg"),
            Cell("Imagen 3", "C:\\Users\marti\\Downloads\\c33cd6ec-a7b3-4289-95b5-ab614131fd2c.jpeg")
        ]

        for i,cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))

   
        