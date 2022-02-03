from tkinter import *
from interfaz.estilos import styles as style
from PIL import Image, ImageTk
from interfaz.pantallas.principal import Principal

class Inicio(Frame, Tk):
    """ Clase encargada de cargar los frames y widgets que utilizará la ventana de inicio
        """

    # Acá guardamos los datos de los desarrolladores para utilizarlos en la implementación
    VALUES  = [
        {"name": "Jaime Andrés Monsalve Ballesteros", "phone":"(+57) 300 724 2377", "email":"jmonsalveb@unal.edu.co"},
        {"name": "Fredy Alberto Orozco Loaiza", "phone":"(+57) 310 458 6939", "email":"frorozcol@unal.edu.co" },
        {"name":"Diego Valentin Osorio Marin", "phone":"(+57) 313 786 51 60", "email":"dosoriom@unal.edu.co"}
    ]

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background = style.BACKGROUND_CONTENEDOR)
        self.controlador = controlador
        # numer inicio para tener referencia y control de los datos de los desarrolladores
        self._numeroInicio = 0
        # numero para tener control de las imagenes que se muestran del sistema
        self._numeroImagenesSistema = 0
        self.inicializarFrames()
    
    def cambiarImagenesSistema(self, e=None):
        """ Función encargada de cambiar las imagenes que se muestran del sistema a momento de mover el mouse
            sobre las imagenes"""

        
        self._numeroImagenesSistema += 1
        # Como solo son 5 imagenes
        self._numeroImagenesSistema %= 5

        # Condiciones para mostrar cada una de las imagenes del sistema
        if self._numeroImagenesSistema == 0:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema1.png').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 1:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema2.png').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 2:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema3.png').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 3:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema4.png').resize((300,225), Image.ANTIALIAS))
        else :
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema5.png').resize((300,225), Image.ANTIALIAS))

        # cambiar la imagen en el label
        self.imagenesSistema.image = imagen_sistema
        self.imagenesSistema.configure(image = imagen_sistema)
    
    def cambiarInfoDesarrolladores(self, e=None):
        """ Funcion encargada de cambiar la infomacion y las imagenes de los desarroladors '
            cuando se da click en la información"""

        self._numeroInicio += 1
        # Como solo son 3 desarroladores para se repita en ciclo
        self._numeroInicio %= 3

        nuevos_valores = self.VALUES[self._numeroInicio]

        # Se cambian los label con los datos del respectivo desarrollador
        self._nombre.config(text= nuevos_valores["name"])
        self._numeroPhone.config(text=nuevos_valores["phone"])
        self._correo.config(text=nuevos_valores["email"])

        # Condicionales para configurar las 4 imagenes de cada desarrollador
        if self._numeroInicio == 0 :
            python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres2.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres3.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres4.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

        elif self._numeroInicio == 1:
            python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_fredy/fredy1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_fredy/fredy2.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_fredy/fredy3.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_fredy/fredy4.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

        elif self._numeroInicio == 2:
            python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_valentin/valentin1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_valentin/valentin2.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_valentin/valentin3.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_valentin/valentin4.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

    def inicializarFrames(self):
        """Funcion para inicializar los seis frames anidados en la ventana"""

        self._p1 = Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p1.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)
        
        self._p2 = Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p2.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p3 = Frame(self._p1, bg = style.BACKGROUND_FRAMES)
        self._p3.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p4 = Frame(self._p1, bg = style.BACKGROUND_FRAMES)
        self._p4.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p5 = Frame(self._p2, bg = style.BACKGROUND_FRAMES)
        self._p5.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p6 = Frame(self._p2, bg = style.BACKGROUND_FRAMES)
        self._p6.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        # Se captura el evento de el frame p5 para cambiar la informacion
        self._p5.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        
        # Se inicializan los demas widgets de las demas ventanas
        self.inicializarWidgetsVentana1()
        self.inicializarWidgetsVentana2()
        self.inicializarWidgetsVentana3()
        self.inicializarWidgetsVentana4()
        
    def inicializarWidgetsVentana1(self):
        """Se inicializa la ventana que da el mensaje de bienvenida"""

        Label(
            self._p3,
            **style.ESTILOS_LABEL_VENTANA_1
        ).pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)
    
    def entrarAVentanaPrincipal(self):
            """Función que ejecuta el botón Ingresar para entrar a la ventana principal"""
            principal = Principal(self.controlador)
            principal.grab_set()
            self.controlador.iconify()
        
    def inicializarWidgetsVentana2(self):
        """Funcion par inicializar los widgets con imagenes del sistema y el boton para ingresar al sistema"""

        imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema1.png').resize((300,225), Image.ANTIALIAS))
        
        self.imagenesSistema = Label(self._p4, pady=20)
        self.imagenesSistema.image = imagen_sistema
        self.imagenesSistema.configure(image = imagen_sistema)
        self.imagenesSistema.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)
        
        Button(self._p4, text="Ingresar", height=5, width=15, font=("Arial", 24), command=self.entrarAVentanaPrincipal).pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self.imagenesSistema.bind('<Enter>', self.cambiarImagenesSistema)
    
    def inicializarWidgetsVentana3(self):
        """ Inicializar frame con los datos de los desarrolladores"""
        
        labelgeneral = Label(self._p5, justify=CENTER)
        labelgeneral.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._nombre = Label(labelgeneral, text = self.VALUES[self._numeroInicio]["name"], bg = "gray", justify=CENTER)
        self._nombre.grid(row = 0, column = 0, columnspan = 2, sticky = EW)

        contacto = Label(labelgeneral, text = "Contacto", justify=CENTER)
        contacto.grid(row = 1, column = 0, sticky=EW)

        self._numeroPhone = Label(labelgeneral, text =self.VALUES[self._numeroInicio]["phone"], justify=LEFT)
        self._numeroPhone.grid(row=1, column=1, sticky=EW)

        email = Label(labelgeneral, text="Email", justify=CENTER)
        email.grid(row=2, column=0, sticky=EW)

        self._correo = Label(labelgeneral, text=self.VALUES[self._numeroInicio]["email"], justify=LEFT)
        self._correo.grid(row=2, column=1, sticky=EW)

        op = Label(labelgeneral, text="Ocupacion", justify=CENTER)
        op.grid(row=3, column=0, sticky=EW)

        self._ocupacion = Label(labelgeneral, text="Estudiante de Ingenieria de Sistemas", justify=LEFT)
        self._ocupacion.grid(row=3, column=1, sticky=EW)

        unal = Label(labelgeneral, text="Universidad", justify=CENTER)
        unal.grid(row=4, column=0, sticky=EW)
        self._universidad = Label(labelgeneral, text="Unal", justify=LEFT).grid(row=4, column=1, sticky=EW)
        
        # Expandimos los labels dentro del frame anidado 3
        labelgeneral.columnconfigure(0, weight=1)

        self._numeroPhone.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        self._correo.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        self._ocupacion.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        self._nombre.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)

        contacto.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        email.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        unal.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        contacto.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        op.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        
    
    def inicializarWidgetsVentana4(self):
        """ Se cargan las imagenes de los desarroladores"""
        
        labelgeneralImagenes = Label(self._p5, justify=CENTER)
        labelgeneralImagenes.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 30)
        
        python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres1.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen1 = Label(labelgeneralImagenes)
        self.imagen1.image = python_imagen1
        self.imagen1.configure(image = python_imagen1)
        self.imagen1.grid(row = 0, column=0, sticky=NSEW)

        python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres2.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen2 = Label(labelgeneralImagenes)
        self.imagen2.image = python_imagen2
        self.imagen2.configure(image = python_imagen2)
        self.imagen2.grid(row = 0, column=1, sticky=NSEW)

        python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres3.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen3 = Label(labelgeneralImagenes)
        self.imagen3.image = python_imagen3
        self.imagen3.configure(image = python_imagen3)
        self.imagen3.grid(row = 1, column=0, sticky=NSEW)

        python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/fotos_andres/andres4.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen4 = Label(labelgeneralImagenes)
        self.imagen4.image = python_imagen4
        self.imagen4.configure(image = python_imagen4)
        self.imagen4.grid(row = 1, column=1, sticky=NSEW)
        
        labelgeneralImagenes.columnconfigure(0, weight=1)
        labelgeneralImagenes.rowconfigure(0, weight=1)
        
