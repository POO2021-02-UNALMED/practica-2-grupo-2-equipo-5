from tkinter import *
from interfaz.estilos.styles import *
from gestionAplicacion.empleados.empleado import Empleado

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
        self._titulo = Label(self, justify=CENTER, text="Calculo de Comisiones", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        self._titulo.pack(side=TOP, fill=X, padx=100, pady=10)
        
    def _mostrarBotonCalcular(self):
        # Se crea el botón con el cuál  va a mostrar las comisiones de los empleados
        self._calculaComisiones = Button(self, text="Calcular", font=FONT, command=self._calcularComision)
        self._calculaComisiones.pack(side=TOP, fill=X, padx=400, pady=10)
        
    def _mostrarComisionEmpleado(self):
        # Frame anidado debajo en el cuál se van a mostrar las compras realizadas por un cliente de acuerdo al codigo pasado en el Entry de arriba
        self._frameMostrarComisiones = Frame(self, bg="white")
        self._frameMostrarComisiones.pack(side=TOP, fill=BOTH, expand=True, padx=100, pady=30)
        
        # Label        
        self._labelMostrarComisiones = Label(self._frameMostrarComisiones, bg="white", font=FONT3, fg=FG2)
        self._labelMostrarComisiones.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)
        
         # Se crea un widget tipo Text 
        self._texto = Text(self._labelMostrarComisiones)
        self._texto.grid(row=0, column=0, sticky=EW, padx=100, pady=10)
        
        # Se crea un widget tipo Scrollbar
        self._scrollbar = Scrollbar(self._labelMostrarComisiones, command=self._texto.yview)
        
        # Se le asigna el comando al Text de que va a contener un scrollbar vertical
        self._texto.config(yscrollcommand=self._scrollbar.set)
        
        # Se empaqueta el scrollbar
        self._scrollbar.grid(row=0, column=1, sticky=NS, pady=10)
        
        self._frameMostrarComisiones.columnconfigure(1, weight=1)
        self._labelMostrarComisiones.columnconfigure(1, weight=1)
        
    def _calcularComision(self):
        comisiones = Empleado.calcularComision()
        self._showComisiones(comisiones)
        
    def _showComisiones(self, empleados):
        texto = ""
        
        for val in empleados:
            texto += "Comisiones totales: " + str(val["total"]) + "\n" + val["empleado"].__str__() + "\n"
            
        self._texto.insert(END, texto)
        
        
  
