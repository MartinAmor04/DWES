from tkinter import Tk, Label
from PIL import Image,ImageTk

root=Tk()
root.title("Ejemplo de imagen")

imagen = ImageTk.PhotoImage(file="C:\\Users\\marti\\OneDrive\\Imágenes\\La haine (1995).jfif")
label = Label(root,image = imagen)
label.pack()

root.mainloop()
