from tkinter import *
from interfaz.estilos.styles import *
from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.productos.producto import Producto
from gestionAplicacion.compras.compra import Compra
from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.empleados.empleado import Empleado

class ConsultaBDD(Frame):

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
        self._Consultar()
        self._inicializarFrameConsulta()

    def _mostrarTitulo(self):
        # Label superior con el título de la pantalla
        self._titulo = Label(self, justify=CENTER, text="Consulta Base de Datos", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        self._titulo.pack(side=TOP, fill=X, padx=100, pady=10)

    def _Consultar(self):
        # Frame anidado debajo del título en el cuál se le van a agregar los widgets para hacer la consulta 
        self._frameSolicitarConsulta = Frame(self, bg=BACKGROUND_FRAMES)
        self._frameSolicitarConsulta.pack(side=TOP, fill=X, padx=100, pady=10)

        # Label con el título Ingrese los datos a consultar
        texto = "Ingrese un número para seleccionar la tabla a buscar" + "\n" \
                    + "1. Productos" + "\n" \
                    + "2. Servicios" + "\n" \
                    + "3. Empleados" + "\n" \
                    + "4. Clientes" + "\n" \
                    + "5. Compras" + "\n"
                    
        self._labelConsulta = Label(self._frameSolicitarConsulta, text=texto, bg=BACKGROUND_FRAMES, font=FONT, fg=FG, justify=CENTER)
        self._labelConsulta.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        # Entry para ingresar el valor por el cuál se quiere consultar un cliente valioso
        self._entryConsulta = Entry(self._frameSolicitarConsulta, bg="white", font=FONT2, fg=FG2, justify=CENTER)
        self._entryConsulta.pack(side=LEFT, fill=BOTH,expand=True, padx=10, pady=10)

        # Botón de consulta
        self._botonConsulta = Button(self._frameSolicitarConsulta, text="Buscar", font=FONT, command=self.buscarConsulta)
        self._botonConsulta.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self._frameSolicitarConsulta.columnconfigure(1, weight=1)

    def _inicializarFrameConsulta(self):
        # Frame anidado debajo en el cuál se van a mostrar los clientes valiosos de acuerdo al valor valioso pasado en el Entry de arriba
        self._frameMostrarResultadoConsulta = Frame(self, bg="white")
        self._frameMostrarResultadoConsulta.pack(side=TOP, fill=BOTH, expand=True, padx=100, pady=10)

        self._mostrarResultadoConsulta = Label(self._frameMostrarResultadoConsulta, text="", bg="white", font=FONT3, fg=FG2, justify=CENTER)
        self._mostrarResultadoConsulta.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

        self._frameMostrarResultadoConsulta.columnconfigure(1, weight=1)

    def buscarConsulta(self):
        valor = self._entryConsulta.get()
        
        if len(valor) != 0:
            valor = int(valor)
            self._mostrarConsulta(valor)
                
    def _mostrarConsulta(self, valor):
        texto = ""
        
        if valor == 1:
            for producto in Producto.getProductos().values():
                texto += producto.__str__()
                
        elif valor == 2:
            for servicio in Servicio.getServicios().values():
                texto += servicio.__str__()
        
        elif valor == 3:
            for empleado in Empleado.getEmpleados().values():
                texto += empleado.__str__()

        elif valor == 4:
            for cliente in Cliente.getClientes().values():
                texto += cliente.__str__()
                
        elif valor == 5:
            for compra in Compra.getCompras().values():
                texto += compra.__str__()
                
        else: 
            texto += "Número no válido"
            
        self._mostrarResultadoConsulta.config(text=texto)