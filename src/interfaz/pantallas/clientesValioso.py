from tkinter import *
from interfaz.estilos.styles import *
from gestionAplicacion.compras.cliente import *

class ClienteValioso(Frame):
    
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
        self._ConsultarClientesValiosos()
        self._inicializarFrameClientesValiosos()
        
    def _mostrarTitulo(self):
        # Label superior con el título de la pantalla
        self._titulo = Label(self, justify=CENTER, text="Clientes Valiosos", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        self._titulo.pack(side=TOP, fill=X, padx=10, pady=10)
        
    def _ConsultarClientesValiosos(self):
        # Frame anidado debajo del título en el cuál se le van a agregar los widgets para hacer la consulta de los clientes valiosos
        self._frameIngresarValorValioso = Frame(self, bg=BACKGROUND_FRAMES)
        self._frameIngresarValorValioso.pack(side=TOP, fill=X, padx=100, pady=10)
        
        # Label con el título Ingrese Valor Valioso
        self._labelIngreseValorValioso = Label(self._frameIngresarValorValioso, text="Ingrese Valor Valioso", bg=BACKGROUND_FRAMES, font=FONT, fg=FG, justify=CENTER)
        self._labelIngreseValorValioso.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        # Entry para ingresar el valor por el cuál se quiere consultar un cliente valioso
        self._valorValioso = Entry(self._frameIngresarValorValioso, bg="white", font=FONT2, fg=FG2, justify=CENTER)
        self._valorValioso.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        # Botón de consulta
        self._botonValorValioso = Button(self._frameIngresarValorValioso, text="Buscar", font=FONT, command=self.buscarClientesValiosos)
        self._botonValorValioso.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        self._frameIngresarValorValioso.columnconfigure(1, weight=1)
        
        
    def _inicializarFrameClientesValiosos(self):
        # Frame anidado debajo en el cuál se van a mostrar los clientes valiosos de acuerdo al valor valioso pasado en el Entry de arriba
        self._frameMostrarClientesValiosos = Frame(self, bg="white")
        self._frameMostrarClientesValiosos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        
        self._mostrarClientesValiosos = Label(self._frameMostrarClientesValiosos, text="", bg="white", font=FONT3, fg=FG2, justify=CENTER)
        self._mostrarClientesValiosos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        
        self._frameMostrarClientesValiosos.columnconfigure(1, weight=1)
        
        
    def buscarClientesValiosos(self):
        valor = self._valorValioso.get()
        
        if len(valor) != 0:
            valor = float(valor)
            
            if valor >=  0:
                clientes_valiosos = Cliente.clientesValiosos(valor)
                self.mostrarClientesValiosos(clientes_valiosos)
            
            
    def mostrarClientesValiosos(self, clientes):
        texto = ""
        
        for val in clientes:
            texto += val["cliente"].__str__() + "Total: " + str(val["total"]) + "\n\n"
            
        self._mostrarClientesValiosos.config(text=texto)
        
        
