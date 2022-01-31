import tkinter as tk

class MenuInicio(tk.Menu):
    
    def __init__(self, padre):
        super().__init__(padre)
        self._padre = padre
        inicio = tk.Menu(self)
        self.add_cascade(menu = inicio, label = "Inicio")
        inicio.add_command(label = "Descripcion del sistema")
        inicio.add_command(label = "Salir", command=self.salir)
        
    def salir(self):
        self._padre.destroy()