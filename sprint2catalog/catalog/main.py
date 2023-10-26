from tkinter import Image, Tk
from loading_window import LoadWindow


class main:
   #Clase principal
    if __name__ == "__main__":
        root = Tk()
        app = LoadWindow(root)
        root.mainloop()