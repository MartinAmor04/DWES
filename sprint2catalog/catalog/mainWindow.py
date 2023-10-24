<<<<<<< HEAD
from io import BytesIO
from tkinter import  ttk
import tkinter as tk
from tkinter.tix import IMAGETEXT
=======
from tkinter import  ttk
import tkinter as tk
>>>>>>> 0c6f7e85c236d0bb398b44c6941d32e1b1be55ba
from cell import Cell
from tkinter import messagebox
from PIL import Image, ImageTk
from detail_window import DetailWindow
<<<<<<< HEAD
import requests
import threading
import _thread

class MainWindow():
  
    def __init__(self, root,json_data):
        self.root=root
        #Inicializamos las imágenes
        
        for diccionario  in json_data:
            self.cells=Cell[json_data.get("name"),json_data.get("description"),json_data.get("image_url")]

       
=======

class MainWindow():
    #llamamos a la nueva ventana, y le enviamos la información
    def onButtonClicked(self, cell):
     detail_indow= DetailWindow (cell.title, cell.image_tk,cell.description)

        
        

    def __init__(self, root):
        self.root=root
#Inicializamos las imágenes
        self.cells=[
            Cell("Imagen 1", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\apocalypse-now-.jpg","Durante la guerra de Vietnam, al joven Capitán Willard, un oficial de los servicios de inteligencia del ejército estadounidense, se le ha encomendado entrar en Camboya con la peligrosa misión de eliminar a Kurtz, un coronel renegado que se ha vuelto loco. El capitán deberá ir navegar por el río hasta el corazón de la selva, donde parece ser que Kurtz reina como un buda despótico sobre los miembros de la tribu Montagnard, que le adoran como a un dios. "),
            Cell("Imagen 2", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\evangelion.jpg", "El mundo después de un gran cataclismo provocado por unas despiadadas criaturas. Gran parte de la Tierra ha quedado destruida, y los supervivientes deben luchar contra estos ataques de origen y naturaleza desconocida. Para proteger a los humanos de estos ataques, y debido a que las armas comunes no funcionan contra estos enemigos, la organización NERV ha creado los EVA, máquinas humanoides gigantes que se conectan al sistema nervioso y que solo pueden ser pilotadas por niños. Uno de ellos es el joven Shinji Ikari, que junto con Auska tratarán de frenar la llegada del Tercer Impacto."),
            Cell("Imagen 3", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\le haine.jpg", "Tras una noche de disturbios en un barrio marginal de las afueras de París, tres amigos adolescentes, Vinz, Saïd y Hubert (un judío, un árabe inmigrante y un boxeador amateur negro, respectivamente), son testigos de un hecho, en el que su amigo Abdel resulta herido por la policía. El deambular por la ciudad, la violencia entre bandas y los conflictos con la policía son las constantes en las 24 horas siguientes de la vida de estos jóvenes."),
            Cell("Imagen 4 ", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\the lighthouse.jpg", "Una remota y misteriosa isla de Nueva Inglaterra en la década de 1890. El veterano farero Thomas Wake (Willem Dafoe) y su joven ayudante Ephraim Winslow (Robert Pattinson) deberán convivir durante cuatro semanas. Su objetivo será mantener el faro en buenas condiciones hasta que llegue el relevo que les permita volver a tierra. Pero las cosas se complicarán cuando surjan conflictos por jerarquías de poder entre ambos"),
            Cell("Imagen 5", "C:\\msys64\\home\\marti\\DWES\\sprint1tkinter\\catalog\\data\\unedited\\the lobster.jpg", "En un futuro cercano los solteros no tienen cabida en la sociedad. Por esta razón, todos son arrestados y llevados a un hotel donde tienen 45 días para conocer a alguien y enamorarse de por vida. Si no lo consiguen, serán transformados en el animal que ellos escojan. David llega al hotel con su hermano, que se ha convertido en perro. El joven no encuentra una persona con quien empezar una relación y se escapa al bosque con un grupo de disidentes.")
        ]
>>>>>>> 0c6f7e85c236d0bb398b44c6941d32e1b1be55ba

        for i, cell in enumerate(self.cells):
            label= ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=0, column=i)
            label.bind("<Button-1>", lambda event, celda = cell: self.onButtonClicked(celda))


<<<<<<< HEAD
        self.thread=threading.Thread(target=self.fetch_json_data)
        self.thread.start()


    def load_image_from_url(self,url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img=IMAGETEXT.PhotoImage(img_data)
        Cell(img)
    
=======
   
        
>>>>>>> 0c6f7e85c236d0bb398b44c6941d32e1b1be55ba
