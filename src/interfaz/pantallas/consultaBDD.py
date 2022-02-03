from tkinter import *
from interfaz.estilos.styles import *
from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.productos.producto import Producto
from gestionAplicacion.compras.compra import Compra
from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.empleados.empleado import Empleado
from gestionAplicacion.empleados.cajero import Cajero
from excepciones import *

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
                    
        self._labelConsulta = Label(self._frameSolicitarConsulta, text=texto, bg=BACKGROUND_FRAMES, font=FONT3, fg=FG, justify=CENTER)
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
        
        # Se crea Label en el cuál se mostrarán los resultados de la consulta implementando un Scrollbar
        self._mostrarResultadoConsulta = Label(self._frameMostrarResultadoConsulta, bg="white", font=FONT3, fg=FG2)
        self._mostrarResultadoConsulta.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        
        # Se crea un widget tipo Text 
        self._texto = Text(self._mostrarResultadoConsulta)
        self._texto.grid(row=0, column=0, sticky=EW, padx=100, pady=10)
        
        # Se crea un widget tipo Scrollbar
        self._scrollbar = Scrollbar(self._mostrarResultadoConsulta, command=self._texto.yview)
        
        # Se le asigna el comando al Text de que va a contener un scrollbar vertical
        self._texto.config(yscrollcommand=self._scrollbar.set)
        
        # Se empaqueta el scrollbar
        self._scrollbar.grid(row=0, column=1, sticky=NS, pady=10)

        self._frameMostrarResultadoConsulta.columnconfigure(1, weight=1)
        self._mostrarResultadoConsulta.columnconfigure(1, weight=1)

    def buscarConsulta(self):
        valor = self._entryConsulta.get()

        try:
            val = int(valor)
        except ValueError:
            raise ExcepcionTiposMissMatch().showMessage()
            return

        if int(valor) < 0 :
            try:
                raise ExcepcionNegativos()
            except ExcepcionNegativos as f:
                f.showMessage()
            return
        
        if len(valor) != 0:
            valor = int(valor)
            self._mostrarConsulta(valor)
        else:
            try:
                raise ExcepcionCamposNulos()
            except ExcepcionCamposNulos as f:
                f.showMessage()
            return
                
    def _mostrarConsulta(self, valor):
        texto = ""
        
        if valor == 1:

            if len(Producto.getProductos().values()) == 0:
                try:
                    raise ExcepcionConjuntoVacio()
                except ExcepcionConjuntoVacio as f:
                    f.showMessage()
                return

            for producto in Producto.getProductos().values():
                texto += producto.__str__() + "\n"
                
        elif valor == 2:

            if len(Servicio.getServicios().values()) == 0:
                try:
                    raise ExcepcionConjuntoVacio()
                except ExcepcionConjuntoVacio as f:
                    f.showMessage()
                return

            for servicio in Servicio.getServicios().values():
                texto += servicio.__str__() + "\n"
        
        elif valor == 3:

            if len(Empleado.getEmpleados().values()) == 0:
                try:
                    raise ExcepcionConjuntoVacio()
                except ExcepcionConjuntoVacio as f:
                    f.showMessage()
                return

            texto_cajero = "****CAJEROS****\n"
            texto_tecnico = "****TECNICOS****\n"

            for empleado in Empleado.getEmpleados().values():
                if isinstance(empleado, Cajero):
                    texto_cajero += empleado.__str__()
                else:
                    texto_tecnico += empleado.__str__()
            texto = texto_cajero + "\n" +texto_tecnico

        elif valor == 4:

            if len(Cliente.getClientes().values()) == 0:
                try:
                    raise ExcepcionConjuntoVacio()
                except ExcepcionConjuntoVacio as f:
                    f.showMessage()
                return

            for cliente in Cliente.getClientes().values():
                texto += cliente.__str__() + "\n"
                
        elif valor == 5:

            if len(Compra.getCompras().values()) == 0:
                try:
                    raise ExcepcionConjuntoVacio()
                except ExcepcionConjuntoVacio as f:
                    f.showMessage()
                return

            for compra in Compra.getCompras().values():
                texto += compra.__str__() + "\n"
                
        else: 
            try:
                raise ErrorAplicacion("Numero no valido")
            except ErrorAplicacion as f:
                f.showMessage()
            return
            
        self._texto.insert(END, texto)
