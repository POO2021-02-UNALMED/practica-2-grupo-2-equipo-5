import tkinter as tk
from estilos import styles as style

class Inicio(tk.Frame):

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background = style.BACKGROUND_CONTENEDOR)
        self.controlador = controlador
        self.inicializarFrames()
        
    def imprimir(e):
        print("Click en el frame", e)

    def inicializarFrames(self):
        p1 = tk.Frame(self, bg = style.BACKGROUND_FRAMES)
        p1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
        
        p2 = tk.Frame(self, bg = style.BACKGROUND_FRAMES)
        p2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        p3 = tk.Frame(p1, bg = style.BACKGROUND_P)
        p3.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        p4 = tk.Frame(p1, bg = style.BACKGROUND_P)
        p4.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        p5 = tk.Frame(p2, bg = style.BACKGROUND_P)
        p5.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        p6 = tk.Frame(p2, bg = style.BACKGROUND_P)
        p6.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)


        p5.bind('<ButtonPress-1>', Inicio.imprimir)
        
        self.inicializarWidgetsVentana1(p3)
        self.inicializarWidgetsVentana2(p4)
        self.inicializarWidgetsVentana3(p5)
        self.inicializarWidgetsVentana4(p6)
        
    def inicializarWidgetsVentana1(self, contenedor):
        tk.Label(
            contenedor,
            **style.ESTILOS_LABEL_VENTANA_1
        ).pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
    
    def inicializarWidgetsVentana2(self, contenedor):
        tk.Button(contenedor, text="Ingresar").grid(row = 1, column = 0)
    
    def inicializarWidgetsVentana3(self, contenedor):
        tk.Label(
            contenedor,
            text = "Jaime Andrés Monsalve Ballesteros",
            bg = "red" 
        ).grid(row = 0, column = 0, columnspan = 2, sticky = tk.EW)
        
        tk.Label(contenedor, text = "Contacto").grid(row = 1, column = 0)
        numero = tk.Label(contenedor, text = "(+57) 300 724 2377").grid(row=1, column=1)
        
        tk.Label(contenedor, text="Email").grid(row=2, column=0)
        correo = tk.Label(contenedor, text="jmonsalveb@unal.edu.co").grid(row=2, column=1)
        
        tk.Label(contenedor, text="Ocupacion").grid(row=3, column=0)
        ocupacion = tk.Label(contenedor, text="Estudiante de Ingenieria de Sistemas").grid(row=3, column=1)
        
        tk.Label(contenedor, text="Universidad").grid(row=4, column=0)
        universidad = tk.Label(contenedor, text="Unal").grid(row=4, column=1)\

        


        
    
    def inicializarWidgetsVentana4(self, contenedor):
        pass
