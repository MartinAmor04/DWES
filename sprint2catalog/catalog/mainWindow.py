from io import BytesIO
from tkinter import  ttk
import tkinter as tk
from tkinter.tix import IMAGETEXT
from cell import Cell
from tkinter import messagebox
from PIL import Image, ImageTk
from detail_window import DetailWindow
import requests
import threading
import _thread

class MainWindow():
  
    def __init__(self, root,json_data):
        self.root=root
        #Inicializamos las imágenes
        
        for diccionario  in json_data:
            self.cells=Cell[json_data.get("name"),json_data.get("description"),json_data.get("image_url")]

       

        for i, cell in enumerate(self.cells):
            label= ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, celda = cell: self.onButtonClicked(celda))


        self.thread=threading.Thread(target=self.fetch_json_data)
        self.thread.start()


    def load_image_from_url(self,url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img=IMAGETEXT.PhotoImage(img_data)
        Cell(img)
    