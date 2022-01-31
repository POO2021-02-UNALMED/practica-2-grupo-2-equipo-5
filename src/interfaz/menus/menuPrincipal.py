# Se importan las librería a utilizar
from tkinter import *
from tkinter import messagebox

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
        
        # Se crean los opciones de cada submenu
        
        # Para el caso del submenu Archivos
        menuArchivos.add_command(label="Aplicacion", command=self.mostrarInfo)
        menuArchivos.add_command(label="Salir", command=self.salir)
        
        # Para el caso del submenu Procesos y Consultas
        menuProcesos.add_command(label="Gestionar Clientes")
        menuProcesos.add_command(label="Gestionar Compras")
        menuProcesos.add_command(label="Gestionar Empleados")
        menuProcesos.add_command(label="Gestionar Productos")
        menuProcesos.add_command(label="Gestionar Servicios")
        
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
        
        
        
    
