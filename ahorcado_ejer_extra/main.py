import tkinter as tk
from ventana_juego import JuegoAhorcado
from ventana_carga import Ventana_carga
 


if __name__ == '__main__':
    root = tk.Tk()
    app = Ventana_carga(root)
    root.mainloop()