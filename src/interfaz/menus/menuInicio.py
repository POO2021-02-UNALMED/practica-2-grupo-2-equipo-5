import tkinter as tk
from tkinter import messagebox

class MenuInicio(tk.Menu):
    
    def __init__(self, padre):
        super().__init__(padre)
        inicio = tk.Menu(self)
        self.add_cascade(menu = inicio, label = "Inicio")
        inicio.add_command(label = "Descripcion del sistema")
        inicio.add_command(label = "Salir")
        
        
    
