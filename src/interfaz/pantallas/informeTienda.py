from tkinter import *
from interfaz.estilos.styles import *


class Informe(Frame):

    # Se crea el contructor de la clase dónde se le pasan como parámetros el padre o frame que lo contiene y la clase controlador que es Principal
    def __init__(self, padre, controlador):
        # Se llama inicializa el constructor padre de la clase
        super().__init__(padre)
        # Se configura el Frame
        self.configure(background=BACKGROUND_CONTENEDOR)
        #Atributos
        self._controlador = controlador

        # Se inicializan los widgets que van en la interfaz
        self._mostrarTitulo()
        self._mostrarBotonGenerarInfome()
        self._mostrarInforme()

    def _mostrarTitulo(self):
        # Label superior con el título de la pantalla
        self._titulo = Label(self, justify=CENTER, text="Informe Tienda PJ Tech", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        self._titulo.pack(side=TOP, fill=X, padx=100, pady=10)

    def _mostrarBotonGenerarInfome(self):
        # Se crea el botón con el cuál  va a mostrar el Informe de PJ Tech
        self._botonGenerarInforme = Button(self, text="Generar Informe", font=FONT)
        self._botonGenerarInforme.pack(side=TOP, fill=X, padx=400, pady=10)
        
    def _mostrarInforme(self):
        # Frame anidado debajo en el cuál se van a mostrar las compras realizadas por un cliente de acuerdo al codigo pasado en el Entry de arriba
        self._frameMostrarInforme = Frame(self, bg="white")
        self._frameMostrarInforme.pack( side=TOP, fill=BOTH, expand=True, padx=100, pady=30)

        # Label
        self._labelMostrarInforme = Label(self._frameMostrarInforme, text="", bg="white", font=FONT4, fg=FG2, justify=CENTER)
        self._labelMostrarInforme.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)
        
        # Adaptar 
        self._frameMostrarInforme.columnconfigure(1, weight=1)

