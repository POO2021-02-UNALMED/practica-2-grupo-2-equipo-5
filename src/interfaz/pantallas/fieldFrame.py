from tkinter import *
from interfaz.estilos.styles import *

class FieldFrame(Frame):
    
    def __init__(self, padre, controlador, tituloCriterios = None, criterios = None, tituloValores = None, valores = None, habilitado = None, nombreProceso = None, descripcionProceso = None):
        # Se llama al padre (Menu), para que inicialice
        super().__init__(padre)
        
        # Atributos
        self._controlador = controlador
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        
        self.inicializarWidgets()
        
    def inicializatWidgets(self):
        labelNombreProceso = Label(self, justify=CENTER, text="Gestion Cliente", bg=BACKGROUND_CONTENEDOR, font=FONT, fg=FG)
        labelNombreProceso.pack(side=TOP, fill=X, padx=10, pady=10)
        
        labelDescripcionProceso = Label(self, justify=CENTER, text="Edita o consulta clientes", bg=BACKGROUND_CONTENEDOR, font=FONT, fg=FG)
        labelDescripcionProceso.pack(side=TOP, fill=X, padx=10, pady=10)
        
        frameCriterioValor = Frame(self, bg="white")
        frameCriterioValor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        
        
