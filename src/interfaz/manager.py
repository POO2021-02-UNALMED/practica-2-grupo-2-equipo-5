from tkinter import *
from interfaz.estilos.styles import *
from interfaz.pantallas.inicio import Inicio
from interfaz.menus.menuInicio import MenuInicio

class Manager(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inicio")
        self.option_add('*tearOff', False)
        contenedor = Frame(self)
        contenedor.pack(side = TOP, fill = BOTH, expand = True)
        contenedor.configure(background = BACKGROUND_CONTENEDOR)
        contenedor.grid_columnconfigure(0, weight = 1)
        contenedor.grid_rowconfigure(0, weight = 1)
        
        self._ventanaInicio = Inicio(contenedor, self)
        self._ventanaInicio.grid(row = 0, column = 0, sticky = NSEW)
        
        menuInicio = MenuInicio(self)
        self['menu'] = menuInicio
        

    
