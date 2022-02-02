# Se importan las librería a utilizar
from distutils import command
from tkinter import *
from tkinter import messagebox
from interfaz.pantallas.fieldFrame import *

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
        menuProcesos.add_command(label="Gestionar Servicios", command=self._gestionarServicios)
        
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
        self._values["criterios"] = ["Nombre", "Dirección", "Teléfono", "Fecha Nacimiento"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar cliente"
        self._values["descripcionProceso"] = "Hola que haces"
        self._controlador.mostrarFrame(self._values)
    
    def _gestionarComprasProductos(self):
        self._values["criterios"] = ["Descripcion", "Descuento","Fecha de compra"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Compra-Productos"
        self._values["descripcionProceso"] = "Gueno"
        self._controlador.mostrarFrame(self._values)

    def _gestionarCompraServicio(self):
        self._values["criterios"] = ["Descripcion", "Descuento","Tiempo de culminación"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Compra-Servicios"
        self._values["descripcionProceso"] = "Que mas pues"
        self._controlador.mostrarFrame(self._values)
    
    def _gestionarCajeros(self):
        self._values["criterios"] = ["Nombre", "Sueldo", "Comision", "Corre", "Número de contacto", "Cantidad de ventas"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar empleados de cajeros"
        self._values["descripcionProceso"] = "Hello baby!!"
        self._controlador.mostrarFrame(self._values)
    
    def _gestionarTecnico(self):
        self._values["criterios"] = ["Nombre", "Sueldo", "Comision", "Corre", "Número de contacto", "Años de experiencias"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar empleados de servicio"
        self._values["descripcionProceso"] = "Jonichigua"
        self._controlador.mostrarFrame(self._values)
    
    def _gestionarProductos(self):
        self._values["criterios"] = ["Nombre", "Fecha de Ingreso", "Precio", "Descripción"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Productos"
        self._values["descripcionProceso"] = "Peguelo peguelo papi"
        self._controlador.mostrarFrame(self._values)
    
    def _gestionarServicios(self):
        self._values["criterios"] = ["Precio", "Fecha Servicio", "Descripción"]
        self._values["valores"] = [None]* len(self._values["criterios"])
        self._values["nombreProceso"] = "Gestionar Productos"
        self._values["descripcionProceso"] = "Peguelo peguelo papi"*2
        self._controlador.mostrarFrame(self._values)

        
        
        
    
