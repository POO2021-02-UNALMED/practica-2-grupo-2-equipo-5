from tkinter import *
from interfaz.estilos.styles import *

class Comision(Frame):
    
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
        self._mostrarBotonCalcular()
        self._mostrarComisionEmpleado()
        
    def _mostrarTitulo(self):
        # Label superior con el título de la pantalla
        self._titulo = Label(self, justify=CENTER, text="Calculo de Comisones", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        self._titulo.pack(side=TOP, fill=X, padx=10, pady=10)
        
    def _mostrarBotonCalcular(self):
        # Se crea el botón con el cuál  va a mostrar las comisiones de los empleados
        self._calculaComisiones = Button(self, text="Calcular", font=FONT)
        self._calculaComisiones.pack(side=TOP, fill=X, padx=400, pady=10)
        
    def _mostrarComisionEmpleado(self):
        # Frame anidado debajo en el cuál se van a mostrar las compras realizadas por un cliente de acuerdo al codigo pasado en el Entry de arriba
        self._frameMostrarComisiones = Frame(self, bg="white")
        self._frameMostrarComisiones.pack(side=TOP, fill=BOTH, expand=True, padx=30, pady=30)
        
        # Expandir los widgets dentro del contenedor
        self._frameMostrarComisiones.columnconfigure(1, weight=1)
        
  
