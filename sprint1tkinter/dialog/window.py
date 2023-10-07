from tkinter import ttk, Button
import tkinter as tk
from yes_window import yesWindow
from no_window import noWindow

class MainWindow:
    def __init__(self, root):
        self.root=root

        self.frame=ttk.Frame(self.root)
        self.frame.pack()

        self.label=ttk.Label(self.frame, text="¿Te gusta la saga Star Wars?")
        self.label.pack()

        self.button=ttk.Button(self.frame, text="Sí", command= yesWindow)
        self.button.pack(side="left")
        
        self.button=ttk.Button(self.frame, text="No", command= noWindow)
        self.button.pack(side="right")

        