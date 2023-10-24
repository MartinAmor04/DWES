import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    #Clase la cual contiene la estructuras de las celdas
<<<<<<< HEAD
    def __init__(self, title, img,description):
     self.title=title
=======
    def __init__(self, title, path,description):
     self.title=title
     self.path=path
     self.foto = Image.open(self.path)
>>>>>>> 0c6f7e85c236d0bb398b44c6941d32e1b1be55ba
     self.img = self.foto.resize((100, 100), Image.Resampling.LANCZOS)
     self.image_tk = ImageTk.PhotoImage(self.img)     
     self.description=description

     