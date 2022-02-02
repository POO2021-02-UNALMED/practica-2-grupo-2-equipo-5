from tkinter import *
from interfaz.estilos.styles import *

class Lanzamiento(Frame):
    
    def __init__(self, padre, controlador):
            super().__init__(padre)
            self.configure(background=BACKGROUND_CONTENEDOR)
            self._controlador = controlador
            
            labelInicial = Label(self, justify=CENTER, text="Manual", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
            labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    

class FieldFrame(Frame):
    
    def __init__(self, padre, controlador, tituloCriterios = None, criterios = None, tituloValores = None, valores = None, habilitado = None, nombreProceso = None, descripcionProceso = None):
        # Se llama al padre (Menu), para que inicialice
        super().__init__(padre)
        
        # Configuramos el frame para darle un fondo
        self.configure(background=BACKGROUND_CONTENEDOR)
        
        # Atributos
        self._controlador = controlador
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        
        # Inicializamos los widgets
        
        # Titulo (Gestion ....)
        labelNombreProceso = Label(self, justify=CENTER, text="Gestion Cliente", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelNombreProceso.pack(side=TOP, fill=X, padx=10, pady=10)
        
        # Descripción
        labelDescripcionProceso = Label(self, justify=CENTER, text="Edita o consulta clientes", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelDescripcionProceso.pack(side=TOP, fill=X, padx=10, pady=10)
        
        # Criterio valor se empaquetan todos los widgets dentro de un Frame y se usa grid para posicionar los elementos
        frameCriterioValor = Frame(self, bg="white")
        frameCriterioValor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=20)

        labelCriterios = Label(frameCriterioValor, text=self._tituloCriterios, bg=BACKGROUND_P, font=FONT, fg = FG, justify=CENTER)
        labelCriterios.grid(row=0, column=0, sticky=EW)

        labelValores = Label(frameCriterioValor, text=self._tituloValores, bg=BACKGROUND_P, font=FONT, fg = FG, justify=CENTER)
        labelValores.grid(row=0, column=1, sticky=EW)
        
        # Creamos los labels de acuerdo a los datos de entrada por el usuario
        numero_criterios = len(self._criterios)
        numero_valores = len(self._valores)
        
        for i in range(numero_criterios):
            Label(frameCriterioValor, text=self._criterios[i], bg="white", font=FONT2, fg=FG2, justify=CENTER, padx=50, pady=20).grid(row=i+1, column=0, sticky=EW)
            
        for i in range(numero_valores):
           Entry(frameCriterioValor, bg="white", font=FONT2, fg=FG2, justify=CENTER).grid(row=i+1, column=1, sticky=EW, padx=50, pady=20)
        
        # Expandimos los labels dentro del frame anidado 3
        frameCriterioValor.columnconfigure(1, weight=1)
        
        # Mensaje
        mensaje = Label(self, justify=CENTER, text="Gestion Cliente", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        mensaje.pack(side=TOP, fill=X, padx=10, pady=10)
        
        # Botones
        frameBotones = Frame(self, bg=BACKGROUND_FRAMES)
        frameBotones.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=20)
        
        aceptar = Button(frameBotones, text="Aceptar", padx=20, pady=20)
        aceptar.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        borrar = Button(frameBotones, text="Borrar", padx=20, pady=20)
        borrar.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        
        
