from tkinter import *

from pyparsing import col
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
        
        labelNombreProceso = Label(self, justify=CENTER, text="Gestion Cliente", bg=BACKGROUND_CONTENEDOR, font=FONT, fg=FG)
        labelNombreProceso.pack(side=TOP, fill=X, padx=10, pady=10)
        
        labelDescripcionProceso = Label(self, justify=CENTER, text="Edita o consulta clientes", bg=BACKGROUND_CONTENEDOR, font=FONT, fg=FG)
        labelDescripcionProceso.pack(side=TOP, fill=X, padx=10, pady=10)

        frameCriterioValor = Frame(self, bg="white")
        frameCriterioValor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

        labelCriterios = Label(frameCriterioValor, text=self._tituloCriterios, bg=BACKGROUND_CONTENEDOR, font=FONT, fg = FG)
        labelCriterios.grid(row=0, column=0)

        labelIntermedio = Label(frameCriterioValor, text="   ")
        labelIntermedio.grid(row=0, column=1)

        labelValores = Label(frameCriterioValor, text=self._tituloValores, bg=BACKGROUND_CONTENEDOR, font=FONT, fg = FG)
        labelValores.grid(row=0, column=2)

        
        
