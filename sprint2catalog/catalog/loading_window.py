import threading
import requests
from tkinter import Tk
import tkinter as tk
from mainWindow import MainWindow

class LoadWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.finished = False
        self.json_data = []
        self.progress=0
        #Centrar ventana
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
        #Nuevo label a la hora de descargar los datos de GitHub
        self.label = tk.Label(self.root, text="Cargando datos....", font=("Robot Mono", 14))
        self.label.pack()
        
        label_bg_color = self.label.cget("bg")
        
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()
        
        #Creacion/actualizacion del circulo de carga
        self.draw_progress_circle(self.progress)
        

        self.thread = threading.Thread(target=self.fetch_json_data) #Guardamos datos en el thread
        self.thread.start() #Comenzamos el thread
        
        self.check_thread() #Comprobamos estado del thread
        
        self.update_progress_circle()
        
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()      



    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100)) 

        self.canvas.create_arc(10, 10, 40, 40,
                               start=0, extent=angle+10, tags="progress", outline='green', width=6, style=tk.ARC)

    def update_progress_circle(self):
        self.progress += 0.1 
             
        self.draw_progress_circle(self.progress)

        self.root.after(1, self.update_progress_circle)




    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/MartinAmor04/DWES/main/Ejercicio%202.1")       
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
            print(response.json())

    def launch_main_window(self,json_data):
        root=Tk()
        app=MainWindow(root,json_data)
        root.mainloop()    

    def check_thread(self):
        if (self.finished):
            self.root.destroy()
            self.launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)



 
   
        