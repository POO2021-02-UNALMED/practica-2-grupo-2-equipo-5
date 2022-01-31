# Se importan las librerías que vamos a utilizar
from tkinter import *
from interfaz.menus.menuPrincipal import MenuPrincipal
from interfaz.estilos.styles import *
from interfaz.pantallas.fieldFrame import FieldFrame

class Principal(Toplevel):
    
    # Se crea el contructor de la clase
    def __init__(self, padre):
        # Se llama al padre (Toplevel)
        super().__init__(padre)
        
        # Titulo
        self.title("PJ Tech")
        
        # Se agrega el menu
        menuPrincipal = MenuPrincipal(self, padre)
        self['menu'] = menuPrincipal
        
        # Inicio
        contenedor = Frame(self)
        contenedor.pack(side=TOP, fill=BOTH, expand=True)
        contenedor.configure(background=BACKGROUND_CONTENEDOR)
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_rowconfigure(0, weight=1)
        
        self._ventanaPrincipal = FieldFrame(contenedor, self, tituloCriterios="Atributo", tituloValores="Valor")
        self._ventanaPrincipal.grid(row=0, column=0, sticky=NSEW)


        
