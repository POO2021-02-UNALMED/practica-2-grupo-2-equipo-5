# Se importan las librerías que vamos a utilizar
from tkinter import *
from interfaz.menus.menuPrincipal import MenuPrincipal
from interfaz.estilos.styles import *
from interfaz.pantallas.fieldFrame import Lanzamiento
from interfaz.pantallas.fieldFrame import FieldFrame

class Principal(Toplevel):
    
    # Se crea el contructor de la clase
    def __init__(self, padre):
        # Se llama al padre (Toplevel)
        super().__init__(padre)
        
        # Titulo
        self.title("PJ Tech")
        self.geometry("500x500")
        # Se agrega el menu
        menuPrincipal = MenuPrincipal(padre, self)
        self['menu'] = menuPrincipal
        
        # Inicio
        self._contenedor = Frame(self)
        self._contenedor.pack(side=TOP, fill=BOTH, expand=True)
        self._contenedor.configure(background=BACKGROUND_CONTENEDOR)
        self._contenedor.grid_columnconfigure(0, weight=1)
        self._contenedor.grid_rowconfigure(0, weight=1)
        
        
        self._frames = {}
        
        # for F in (Lanzamiento, FieldFrame):
        #     frame = F(contenedor, self)
        #     self._frames[F] = frame
        #     frame.grid(row=0, column=0, sticky=NSEW)
            
        #self.mostrarFrame(Lanzamiento)
        
    def mostrarFrame(self, values:dict):
        frame = FieldFrame(self._contenedor, self, **values)
        frame.grid(row=0, column=0, sticky=NSEW)
        frame.tkraise()

        


        
