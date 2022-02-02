from tkinter import *
from interfaz.estilos.styles import *

class Lanzamiento(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
            
        labelInicial = Label(self, justify=CENTER, text="Manual", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)