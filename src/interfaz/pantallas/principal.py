# Se importan las librerías que vamos a utilizar
from tkinter import *
from interfaz.menus.menuPrincipal import MenuPrincipal

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

        
