
import tkinter as tk


class LoadWindow:
    def __init__(self,root):
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False,False)


        self.label = tk.Label(self.root, text="Cargando datos...", font=("Ariel",14))
        self.label.pack(side = tk.TOP,pady=10)

        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root,width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0 

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

    #    self.thread = threading.Thread(target=self.fetch_json_data)
    #    self.thread.start()


    def draw_progress_circle(self,progress):
        self.canvas.delete("progress")
        angle = int(360*(progress / 100))

        self.canvas.create_arc(10,10,35,35,
                                   start=0,extent=angle,tags="progress",outline='green',width=4,style=tk.ARC)
    
    def update_progress_circle(self):
        if self.progress <= 100:
            self.progress +=0.1
        else:
            self.progress=0

       
        
        

        self.draw_progress_circle(self.progress)
        self.root.after(1,self.update_progress_circle)