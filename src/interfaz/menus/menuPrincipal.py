# Se importan las librería a utilizar
from distutils import command
from tkinter import *
from tkinter import messagebox
from interfaz.pantallas.fieldFrame import *
from interfaz.pantallas.clientesValioso import ClienteValioso
from interfaz.pantallas.devolucion import Devolucion
from interfaz.pantallas.comision import Comision
from interfaz.pantallas.informeTienda import Informe
from interfaz.pantallas.consultaBDD import ConsultaBDD

class MenuPrincipal(Menu):
    
    #Se crea el método constructor
    def __init__(self, padre, controlador):
        # Se llama al padre (Menu), para que inicialice
        super().__init__(padre)
        
        # Atributos
        self._padre = padre
        self._controlador = controlador
        
        # Se crea la barra del menu con los submenus
        menuArchivos = Menu(self, tearoff=0)
        menuProcesos = Menu(self, tearoff=0)
        menuAyuda = Menu(self, tearoff=0)
        
        # se añaden los submenus a la barra del menu
        self.add_cascade(label="Archivo", menu=menuArchivos)
        self.add_cascade(label="Procesos y Consultas", menu=menuProcesos)
        self.add_cascade(label="Ayuda", menu=menuAyuda)
        
        self._values = {"tituloCriterios":"Atributos", "tituloValores":"Valores"}
        # Se crean los opciones de cada submenu
        
        # Para el caso del submenu Archivos
        menuArchivos.add_command(label="Aplicacion", command=self.mostrarInfo)
        menuArchivos.add_command(label="Salir", command=self.salir)
        
        # Para el caso del submenu Procesos y Consultas
        menuProcesos.add_command(label="Gestionar Clientes", command=self._gestionarCliente)
        menuProcesos.add_command(label="Gestionar Compra-Productos", command = self._gestionarComprasProductos)
        menuProcesos.add_command(label="Gestionar Compra-Servicios", command=self._gestionarCompraServicio)
        menuProcesos.add_command(label="Gestionar Cajeros", command = self._gestionarCajeros)
        menuProcesos.add_command(label="Gestionar Técnicos", command=self._gestionarTecnico)
        menuProcesos.add_command(label="Gestionar Productos", command=self._gestionarProductos)
        menuProcesos.add_command(label="Consulta Base de Datos", command=self._consultaBaseDeDatos)
        menuProcesos.add_command(label="Ver clientes valiosos", command=self._verClientesValiosos)
        menuProcesos.add_command(label="Devolucion compra productos", command=self._verDevolucionCompraProductos)
        menuProcesos.add_command(label="Calcular comisiones empleados", command=self._calcularComision)
        menuProcesos.add_command(label="Generar informe estado de tienda", command=self._generarInforme)
        
        # Para el caso del submenu Ayuda
        menuAyuda.add_command(label="Acerca de", command=self.quienesSomos)
        
    def salir(self):
        self._controlador.deiconify()
        self._padre.destroy()
        
    def mostrarInfo(self):
        messagebox.showinfo(
                title="Información Básica",
                message="PJ Tech es una tienda que ofrece gran variedad de productos y servicios, orientada a aficionados de la tecnología. Entre los productos que ofrecemos tenemos: computadores, periféricos, componentes (memorias, CPUs, GPUs, discos duros), videojuegos, etc.. Ofrecemos servicios de mantenimiento y reparación tanto de consolas como PCs"
            )
        
    def quienesSomos(self):
        messagebox.showinfo(
                title="Autores",
                message="Diego Valentín Osorio Marín \nFredy Alberto Orozco Loaiza \nJaime Andrés Monsalve Ballesteros" 
            )
        
    def _gestionarCliente(self):
        self._values["criterios"] = ["ID", "Nombre", "Fecha Nacimiento", "Dirección", "Teléfono"]
        self._values["habilitado"] = ["ID"]
        self._values["nombreProceso"] = "Gestionar cliente"
        self._values["descripcionProceso"] = "Guarda la informacion de un nuevo cliente"
        from gestionAplicacion.compras.cliente import Cliente
        self._values["objeto"] = Cliente
        self._values["valores"] = [Cliente.getIndex()] + [None]*(len(self._values["criterios"]) - len(self._values['habilitado']))
        self._values["atributos"] = ['id', 'nombre', 'fecha_nacimiento', 'direccion', 'telefono']
        self._padre.mostrarFieldFrame(self._values)
    
    def _gestionarComprasProductos(self):
        self._values["criterios"] = ["ID", "Descripcion", "Descuento", "Fecha de compra", "Codigo Cliente", "Codigo Cajero"]
        self._values["habilitado"] = ["ID"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Compra-Productos"
        self._values["descripcionProceso"] = "Registra la informacion de una nueva compra de productos en el sistema"
        from gestionAplicacion.compras.compra_productos import CompraProductos
        self._values["objeto"] = CompraProductos
        self._values["atributos"] = ['id', 'descripcion', 'descuento', 'fecha_de_compra', 'codigo_cliente', 'codigo_cajero']
        self._padre.mostrarFieldFrame(self._values)

    def _gestionarCompraServicio(self):
        self._values["criterios"] = ["ID", "Descripcion", "Descuento", "Tiempo de culminación", "Codigo Tipo Servicio"]
        self._values["habilitado"] = ["ID"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Compra-Servicios"
        self._values["descripcionProceso"] = "Registra la informacion de una nueva compra de servicios en el sistema"
        from gestionAplicacion.compras.compra_servicios import CompraServicios
        self._values["objeto"] = CompraServicios
        self._values["atributos"] = ['id', 'descripcion', 'descuento', 'tiempo_de_culminacion', 'codigo_tipo_servicio']
        self._padre.mostrarFieldFrame(self._values)
    
    def _gestionarCajeros(self):
        self._values["criterios"] = ["ID", "Nombre", "Sueldo", "Comision", "Correo", "Número de contacto", "Cantidad de ventas"]
        self._values["habilitado"] = ["ID"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar empleados de cajeros"
        self._values["descripcionProceso"] = "Registra la informacion de un nuevo empleado cajero en el sitema"
        from gestionAplicacion.empleados.cajero import Cajero
        self._values["objeto"] = Cajero
        self._values["atributos"] = ['id', 'nombre', 'sueldo', 'comision', 'correo', 'numeroContacto', 'cantidadEnVentas']
        self._padre.mostrarFieldFrame(self._values)
    
    def _gestionarTecnico(self):
        self._values["criterios"] = ["ID", "Nombre", "Sueldo", "Comision", "Correo", "Número de contacto", "Años de experiencias"]
        self._values["habilitado"] = ["ID"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar empleados tecnicos"
        self._values["descripcionProceso"] = "Registra la informacion de un nuevos empleado tecnico"
        from gestionAplicacion.empleados.tecnico import Tecnico
        self._values["objeto"] = Tecnico
        self._values["atributos"] = ['id', 'nombre', 'sueldo', 'comision', 'correo', 'numeroContacto', 'experiencia']
        self._padre.mostrarFieldFrame(self._values)
    
    def _gestionarProductos(self):
        self._values["criterios"] = ["ID", "Nombre", "Fecha de Ingreso", "Precio", "Descripción"]
        self._values["habilitado"] = ["ID"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Productos"
        self._values["descripcionProceso"] = "Registra la informacion de un nuevo producto"
        from gestionAplicacion.productos.producto import Producto
        self._values["objeto"] = Producto
        self._values["atributos"] = ['id', 'nombre', 'fecha_ingreso', 'precio', 'descripcion']
        self._padre.mostrarFieldFrame(self._values)
    
    def _verClientesValiosos(self):
        self._padre.mostrarFrameFuncionalidades(ClienteValioso)

    def _verDevolucionCompraProductos(self):
        self._padre.mostrarFrameFuncionalidades(Devolucion)

    def _calcularComision(self):
        self._padre.mostrarFrameFuncionalidades(Comision)

    def _generarInforme(self):
        self._padre.mostrarFrameFuncionalidades(Informe)

    def _consultaBaseDeDatos(self):
        self._padre.mostrarFrameFuncionalidades(ConsultaBDD)
