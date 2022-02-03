# Se importan las librerías que vamos a utilizar
from tkinter import *
from interfaz.menus.menuPrincipal import MenuPrincipal
from interfaz.estilos.styles import *
from interfaz.pantallas.lanzamiento import Lanzamiento
from interfaz.pantallas.fieldFrame import FieldFrame
from interfaz.pantallas.clientesValioso import ClienteValioso
from interfaz.pantallas.devolucion import Devolucion
from interfaz.pantallas.comision import Comision
from interfaz.pantallas.informeTienda import Informe
from interfaz.pantallas.consultaBDD import ConsultaBDD

class Principal(Toplevel):
    
    # Se crea el contructor de la clase
    def __init__(self, padre):
        # Se llama al padre (Toplevel)
        super().__init__(padre)
        
        # Titulo
        self.title("PJ Tech")
        self.geometry("1280x1080")
        # Se agrega el menu
        menuPrincipal = MenuPrincipal(self, padre)
        self['menu'] = menuPrincipal
        
        # Inicio
        self._contenedor = Frame(self)
        self._contenedor.pack(side=TOP, fill=BOTH, expand=True)
        self._contenedor.configure(background=BACKGROUND_CONTENEDOR)
        self._contenedor.grid_columnconfigure(0, weight=1)
        self._contenedor.grid_rowconfigure(0, weight=1)
        
        self._framesFuncionalidades = {}
        
        for F in (Lanzamiento, ClienteValioso, Devolucion, Comision, Informe, ConsultaBDD):
            self._frame =F(self._contenedor, self)
            self._framesFuncionalidades[F] = self._frame
            self._frame.grid(row=0, column=0, sticky=NSEW)
            
        self.mostrarFrameFuncionalidades(Lanzamiento)
        
        self._frame = Lanzamiento(self._contenedor, self)
        self._frame.grid(row=0, column=0, sticky=NSEW)
        
    def mostrarFieldFrame(self, values:dict):
        self._frame = FieldFrame(self._contenedor, self, **values)
        self._frame.grid(row=0, column=0, sticky=NSEW)
        self._frame.tkraise()

    def mostrarFrameFuncionalidades(self, contenedor):
        self._frame = self._framesFuncionalidades[contenedor]
        self._frame.tkraise()
