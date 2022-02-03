from tkinter import *
from interfaz.estilos.styles import *
from gestionAplicacion.productos.detalle_producto import DetalleProducto
from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.empleados.empleado import Empleado

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
        self._botonGenerarInforme = Button(self, text="Generar Informe", font=FONT, command=self.generarInforme)
        self._botonGenerarInforme.pack(side=TOP, fill=X, padx=400, pady=10)
        
    def _mostrarInforme(self):
        # Frame anidado debajo en el cuál se van a mostrar las compras realizadas por un cliente de acuerdo al codigo pasado en el Entry de arriba
        self._frameMostrarInforme = Frame(self, bg="white")
        self._frameMostrarInforme.pack( side=TOP, fill=BOTH, expand=True, padx=100, pady=30)

        # Label
        self._labelMostrarInforme = Label(self._frameMostrarInforme, text="", bg="white", font=FONT, fg=FG2, justify=CENTER)
        self._labelMostrarInforme.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)
        
        # Adaptar 
        self._frameMostrarInforme.columnconfigure(1, weight=1)
        
        
    def generarInforme(self):
        # En este método se generará el informe a modo resumen de la tienda PJ Tech
        texto = "*******INFORME PJ TECH*******" + "\n" \
                    + "Ingresos Totales: " + str(self.getIngresosTotales()) + "\n" \
                    + "Egresos Totales: " + str(self.getEgresosTotales()) + "\n" \
                    + "Utilidades: " + str(self.getUtilidades()) + "\n" \
                        
        self._labelMostrarInforme.config(text=texto)
                        
    def getIngresosTotales(self):
        
        ingresoCompraProductos = 0
        for i in DetalleProducto.getDetallesProductos().values():
            precio = i.getProducto().getPrecio()
            ingresoCompraProductos += precio
            
        ingresoPorServicios = 0
        for i in Servicio.getServicios().values():
            precio = i.getPrecio()
            ingresoPorServicios += precio
            
        ingresosTotales = ingresoCompraProductos + ingresoPorServicios
        
        return ingresosTotales
    
    def getEgresosTotales(self):
        
        nomina = 0
        for i in Empleado.getEmpleados().values():
            sueldo = i.getSueldo()
            nomina += sueldo
            
        return nomina
            
    def getUtilidades(self):
        return self.getIngresosTotales() - self.getEgresosTotales()
        

