import tkinter as tk
from interfaz.estilos import styles as style
from interfaz.pantallas.inicio import Inicio
from interfaz.menus.menuInicio import MenuInicio

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inicio")
        self.option_add('*tearOff', False)
        contenedor = tk.Frame(self)
        contenedor.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        contenedor.configure(background = style.BACKGROUND_CONTENEDOR)
        contenedor.grid_columnconfigure(0, weight = 1)
        contenedor.grid_rowconfigure(0, weight = 1)
        
        self.ventanas = {}
        
        for F in (Inicio, ):
            ventana = F(contenedor, self)
            self.ventanas[F] = ventana
            ventana.grid(row = 0, column = 0, sticky = tk.NSEW)
        
        menuInicio = MenuInicio(self)
        self['menu'] = menuInicio
        
        self.mostrarFrame(Inicio)

    def mostrarFrame(self, contenedor):
        ventana =self.ventanas[contenedor]
        ventana.tkraise()
        