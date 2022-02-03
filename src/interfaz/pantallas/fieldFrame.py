from tkinter import *

from pytest import Instance
from interfaz.estilos.styles import *
from excepciones import *


class FieldFrame(Frame):
    
    def __init__(self, padre, controlador, objeto, atributos, tituloCriterios = None, criterios = None, tituloValores = None, valores = None, habilitado = None, nombreProceso = None, descripcionProceso = None):
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
        self._nombreProceso = nombreProceso
        self._descripcionProceso = descripcionProceso
        self._objeto = objeto
        self._atributos = atributos
        
        # Inicializamos los widgets
        
        # Titulo (Gestion ....)
        labelNombreProceso = Label(self, justify=CENTER, text=self._nombreProceso, bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelNombreProceso.pack(side=TOP, fill=X, padx=10, pady=10)
        
        # Descripción
        labelDescripcionProceso = Label(self, justify=CENTER, text=self._descripcionProceso, bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
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
            Label(frameCriterioValor, text=self._criterios[i], bg="white", font=FONT2, fg=FG2, justify=CENTER).grid(row=i+1, column=0, sticky=EW,  padx=50, pady=10)
            
        self.entrys = {}

        for i in range(numero_valores):
            
            if self._criterios[i] in self._habilitado:
                self.entry = Entry(frameCriterioValor, bg="white", font=FONT2, fg=FG2, justify=CENTER, state=DISABLED)
                self.entrys[self._atributos[i]] = self.entry
                self.entry.grid(row=i+1, column=1, sticky=EW, padx=50, pady=10)
                
            else:
                self.entry = Entry(frameCriterioValor, bg="white", font=FONT2, fg=FG2, justify=CENTER)
                self.entrys[self._atributos[i]] = self.entry
                self.entry.grid(row=i+1, column=1, sticky=EW, padx=50, pady=10)
        
        # Expandimos los labels dentro del frame anidado 3
        frameCriterioValor.columnconfigure(1, weight=1)
        
        # Mensaje
        self.mensaje = Label(self, justify=CENTER, text="", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        self.mensaje.pack(side=TOP, fill=X, padx=10, pady=10)
        
        # Botones
        frameBotones = Frame(self, bg=BACKGROUND_FRAMES)
        frameBotones.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=20)
        
        aceptar = Button(frameBotones, text="Aceptar", command=self.guardarObjeto, font=FONT)
        aceptar.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        borrar = Button(frameBotones, text="Borrar", command = self.borrarCampos, font=FONT)
        borrar.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

    def guardarObjeto(self):
        
        valores = {k:v.get() for k, v in self.entrys.items()}

        for key,entrada in valores.items():
            if len(entrada) == 0 and key != "id":
                try:
                    raise ExcepcionCamposNulos()
                except ExcepcionCamposNulos as f:
                    f.showMessage()
                return


        
        valores.pop("id")
        esta_guardo = self._objeto.crearInterfaz(**valores)
        if esta_guardo:
            self.mensaje.config(text="Fue Exitosó la operación")
        else:
            self.mensaje.config(text="Hay un error en los códigos ó revisa el tipo de dato")



        [item.delete(0, END) for item in self.entrys.values()]

    def borrarCampos(self):
        [item.delete(0, END) for item in self.entrys.values()]
