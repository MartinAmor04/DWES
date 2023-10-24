import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    #Clase la cual contiene la estructuras de las celdas
    def __init__(self, title, img,description):
     self.title=title
     self.img = self.foto.resize((100, 100), Image.Resampling.LANCZOS)
     self.image_tk = ImageTk.PhotoImage(self.img)     
     self.description=description

     