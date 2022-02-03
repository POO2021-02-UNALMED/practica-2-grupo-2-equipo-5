from tkinter import *
from interfaz.estilos.styles import *

class Lanzamiento(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._mostrarInformacion()
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Manual de Instrucciones e Información de la aplicación", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _mostrarInformacion(self):
        Label(self, text="¡En este momento estas en la pantalla principal del gestor de la tienda!", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG).pack(side=TOP, fill=BOTH, padx=10, pady=10)
        Label(self, text="¿Qué puedes hacer?", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG).pack(side=TOP, fill=BOTH, padx=10, pady=10)
        Label(self, text="En el menú superior podrás encontrar varios opciones interesantes, tales como", bg=BACKGROUND_CONTENEDOR, font=FONT3, fg=FG, justify=LEFT).pack(side=TOP, fill=BOTH, padx=10, pady=30)
        Label(self, text="1. (Archivo) Aquí encontraras información sobre PJ Tech y una opción para volver a la interfaz de inicio", bg=BACKGROUND_CONTENEDOR, font=FONT4, fg=FG, justify=LEFT).pack(side=TOP, fill=BOTH, padx=10, pady=10)
        Label(self, text="2. (Procesos y consultas) Aquí podrás utilizar las principales funcionalidades de la aplicación, entre ellas cálculos de comisiones, búsquedas, y otras funcionalidades de mucha utilidad para la tienda", bg=BACKGROUND_CONTENEDOR, font=FONT4, fg=FG, justify=LEFT).pack(side=TOP, fill=BOTH, padx=10, pady=10)
        Label(self, text="3.(Ayuda) Aquí encontraras los nombres de los desarrolladores, por si deseas contactarnos y saber más", bg=BACKGROUND_CONTENEDOR, font=FONT4, fg=FG, justify=LEFT).pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        
        
        
