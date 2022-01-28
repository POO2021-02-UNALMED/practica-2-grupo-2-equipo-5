import tkinter as tk
from estilos import styles as style

class Inicio(tk.Frame):

    VALUES  = [
        {"name": "Jaime Andrés Monsalve Ballesteros", "phone":"(+57) 300 724 2377", "email":"jmonsalveb@unal.edu.co" },
        {"name": "Fredy Alberto Orozco Loaiza", "phone":"(+57) 310 458 6939", "email":"frorozcol@unal.edu.co" },
        {"name":"Diego Valentin Osorio Marin", "phone":"(+57) 313 786 51 60", "email":"dosoriom@unal.edu.co"}
    ]

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background = style.BACKGROUND_CONTENEDOR)
        self.controlador = controlador
        self._numeroInicio = 0
        self.inicializarFrames()
        
    
    def imprimir(self, e=None):
        self._numeroInicio += 1
        self._numeroInicio %= 3
        nuevos_valores = self.VALUES[self._numeroInicio]

        self._nombre.config(text= nuevos_valores["name"])
        self._numeroPhone.config(text=nuevos_valores["phone"])
        self._correo.config(text=nuevos_valores["email"])

    def inicializarFrames(self):
        self._p1 = tk.Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
        
        self._p2 = tk.Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p3 = tk.Frame(self._p1, bg = style.BACKGROUND_P)
        self._p3.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p4 = tk.Frame(self._p1, bg = style.BACKGROUND_P)
        self._p4.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p5 = tk.Frame(self._p2, bg = style.BACKGROUND_P)
        self._p5.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p6 = tk.Frame(self._p2, bg = style.BACKGROUND_P)
        self._p6.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)


        self._p5.bind('<ButtonPress-1>', self.imprimir)
        
        self.inicializarWidgetsVentana1()
        self.inicializarWidgetsVentana2()
        self.inicializarWidgetsVentana3()
        self.inicializarWidgetsVentana4()
        
    def inicializarWidgetsVentana1(self):
        tk.Label(
            self._p3,
            **style.ESTILOS_LABEL_VENTANA_1
        ).pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
    
    def inicializarWidgetsVentana2(self):
        tk.Button(self._p4, text="Ingresar").grid(row = 1, column = 0)
    
    def inicializarWidgetsVentana3(self):
        self._nombre = tk.Label(
            self._p5,
            text = self.VALUES[self._numeroInicio]["name"],
            bg = "red" 
        )
        self._nombre.grid(row = 0, column = 0, columnspan = 2, sticky = tk.EW)

        contacto = tk.Label(self._p5, text = "Contacto")
        contacto.grid(row = 1, column = 0)

        self._numeroPhone = tk.Label(self._p5, text =self.VALUES[self._numeroInicio]["phone"] )
        self._numeroPhone.grid(row=1, column=1)

        email = tk.Label(self._p5, text="Email")
        email.grid(row=2, column=0)

        self._correo = tk.Label(self._p5, text=self.VALUES[self._numeroInicio]["email"])
        self._correo.grid(row=2, column=1)

        op = tk.Label(self._p5, text="Ocupacion")
        op.grid(row=3, column=0)

        self._ocupacion = tk.Label(self._p5, text="Estudiante de Ingenieria de Sistemas")
        self._ocupacion.grid(row=3, column=1)

        unal = tk.Label(self._p5, text="Universidad")
        unal.grid(row=4, column=0)
        self._universidad = tk.Label(self._p5, text="Unal").grid(row=4, column=1)

        self._numeroPhone.bind('<ButtonPress-1>', self.imprimir)
        self._correo.bind('<ButtonPress-1>', self.imprimir)
        self._ocupacion.bind('<ButtonPress-1>', self.imprimir)
        self._nombre.bind('<ButtonPress-1>', self.imprimir)

        contacto.bind('<ButtonPress-1>', self.imprimir)
        email.bind('<ButtonPress-1>', self.imprimir)
        unal.bind('<ButtonPress-1>', self.imprimir)
        contacto.bind('<ButtonPress-1>', self.imprimir)
        op.bind('<ButtonPress-1>', self.imprimir)
        
    
    def inicializarWidgetsVentana4(self):
        pass

