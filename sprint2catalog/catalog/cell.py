import tkinter as tk
from PIL import Image, ImageTk

class Cell:

 def __init__(self, name, description, image_url, image):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.image=image

    
     