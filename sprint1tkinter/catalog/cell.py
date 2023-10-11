import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    #Clase la cual contiene la estructuras de las celdas
    def __init__(self, title, path,description):
     self.title=title
     self.path=path
     self.foto = Image.open(self.path)
     self.img = self.foto.resize((100, 100), Image.Resampling.LANCZOS)
     self.image_tk = ImageTk.PhotoImage(self.img)     
     self.description=description

     