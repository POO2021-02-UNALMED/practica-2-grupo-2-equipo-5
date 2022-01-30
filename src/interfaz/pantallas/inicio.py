import tkinter as tk
from estilos import styles as style
from PIL import Image, ImageTk

class Inicio(tk.Frame, tk.Tk):
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
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema1.jfif').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 1:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema2.jfif').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 2:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema3.jfif').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 3:
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema4.jfif').resize((300,225), Image.ANTIALIAS))
        else :
            imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema5.jfif').resize((300,225), Image.ANTIALIAS))

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
            python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen1.png').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen2.png').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen3.png').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen4.png').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

        elif self._numeroInicio == 1:
            python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen5.png').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen6.png').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen7.png').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen8.png').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

        elif self._numeroInicio == 2:
            python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Bonfire.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/750335.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Bloodborne.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Got.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

    def inicializarFrames(self):
        """Funcion para inicializar los seis frames anidados en la ventana"""

        self._p1 = tk.Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
        
        self._p2 = tk.Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p3 = tk.Frame(self._p1, bg = style.BACKGROUND_FRAMES)
        self._p3.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p4 = tk.Frame(self._p1, bg = style.BACKGROUND_FRAMES)
        self._p4.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p5 = tk.Frame(self._p2, bg = style.BACKGROUND_FRAMES)
        self._p5.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._p6 = tk.Frame(self._p2, bg = style.BACKGROUND_FRAMES)
        self._p6.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        # Se captura el evento de el frame p5 para cambiar la informacion
        self._p5.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        
        # Se inicializan los demas widgets de las demas ventanas
        self.inicializarWidgetsVentana1()
        self.inicializarWidgetsVentana2()
        self.inicializarWidgetsVentana3()
        self.inicializarWidgetsVentana4()
        
    def inicializarWidgetsVentana1(self):
        """Se inicializa la ventana que da el mensaje de bienvenida"""

        tk.Label(
            self._p3,
            **style.ESTILOS_LABEL_VENTANA_1
        ).pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
    
    def inicializarWidgetsVentana2(self):
        """Funcion par inicializar los widgets con imagenes del sistema y el boton para ingresar al sistema"""

        imagen_sistema = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/capturas_sistema/sistema1.jfif').resize((300,225), Image.ANTIALIAS))
        
        self.imagenesSistema = tk.Label(self._p4, pady=20)
        self.imagenesSistema.image = imagen_sistema
        self.imagenesSistema.configure(image = imagen_sistema)
        self.imagenesSistema.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)
        
        tk.Button(self._p4, text="Ingresar", height=5, width=15, font=("Arial", 24)).pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self.imagenesSistema.bind('<Enter>', self.cambiarImagenesSistema)
    
    def inicializarWidgetsVentana3(self):
        """ Inicializar frame con los datos de los desarrolladores"""
        
        labelgeneral = tk.Label(self._p5, justify=tk.CENTER)
        labelgeneral.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 10)

        self._nombre = tk.Label(labelgeneral, text = self.VALUES[self._numeroInicio]["name"], bg = "gray", justify=tk.CENTER)
        self._nombre.grid(row = 0, column = 0, columnspan = 2, sticky = tk.EW)

        contacto = tk.Label(labelgeneral, text = "Contacto", justify=tk.CENTER)
        contacto.grid(row = 1, column = 0, sticky=tk.EW)

        self._numeroPhone = tk.Label(labelgeneral, text =self.VALUES[self._numeroInicio]["phone"], justify=tk.LEFT)
        self._numeroPhone.grid(row=1, column=1, sticky=tk.EW)

        email = tk.Label(labelgeneral, text="Email", justify=tk.CENTER)
        email.grid(row=2, column=0, sticky=tk.EW)

        self._correo = tk.Label(labelgeneral, text=self.VALUES[self._numeroInicio]["email"], justify=tk.LEFT)
        self._correo.grid(row=2, column=1, sticky=tk.EW)

        op = tk.Label(labelgeneral, text="Ocupacion", justify=tk.CENTER)
        op.grid(row=3, column=0, sticky=tk.EW)

        self._ocupacion = tk.Label(labelgeneral, text="Estudiante de Ingenieria de Sistemas", justify=tk.LEFT)
        self._ocupacion.grid(row=3, column=1, sticky=tk.EW)

        unal = tk.Label(labelgeneral, text="Universidad", justify=tk.CENTER)
        unal.grid(row=4, column=0, sticky=tk.EW)
        self._universidad = tk.Label(labelgeneral, text="Unal", justify=tk.LEFT).grid(row=4, column=1, sticky=tk.EW)
        
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
        
        labelgeneralImagenes = tk.Label(self._p5, justify=tk.CENTER)
        labelgeneralImagenes.pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 10, pady = 30)
        
        python_imagen1 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen1.png').resize((300,225), Image.ANTIALIAS))

        self.imagen1 = tk.Label(labelgeneralImagenes)
        self.imagen1.image = python_imagen1
        self.imagen1.configure(image = python_imagen1)
        self.imagen1.grid(row = 0, column=0, sticky=tk.NSEW)

        python_imagen2 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen2.png').resize((300,225), Image.ANTIALIAS))

        self.imagen2 = tk.Label(labelgeneralImagenes)
        self.imagen2.image = python_imagen2
        self.imagen2.configure(image = python_imagen2)
        self.imagen2.grid(row = 0, column=1, sticky=tk.NSEW)

        python_imagen3 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen3.png').resize((300,225), Image.ANTIALIAS))

        self.imagen3 = tk.Label(labelgeneralImagenes)
        self.imagen3.image = python_imagen3
        self.imagen3.configure(image = python_imagen3)
        self.imagen3.grid(row = 1, column=0, sticky=tk.NSEW)

        python_imagen4 = ImageTk.PhotoImage(Image.open('./src/interfaz/Imagenes/Imagen4.png').resize((300,225), Image.ANTIALIAS))

        self.imagen4 = tk.Label(labelgeneralImagenes)
        self.imagen4.image = python_imagen4
        self.imagen4.configure(image = python_imagen4)
        self.imagen4.grid(row = 1, column=1, sticky=tk.NSEW)
        
        labelgeneralImagenes.columnconfigure(0, weight=1)
        labelgeneralImagenes.rowconfigure(0, weight=1)
