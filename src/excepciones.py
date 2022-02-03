from tkinter import messagebox

class ErrorAplicacion(Exception):

    def __init__(self, mensaje):
        self._error = "Manejo de errores de la aplicacion " + mensaje
        super().__init__(self._error)

    def showMessage(self):
        messagebox.showerror('Excepcion', self._error)

class ExcepcionCampos(ErrorAplicacion):

    def __init__(self, mensaje):
        self._error = "ExcepcionCampos " + mensaje
        super().__init__(self._error)

class ExcepcionRepetidos(ErrorAplicacion):

    def __init__(self, mensaje):
        self._error = "ExcepcionRepetidos " + mensaje
        super().__init__(self._error)

class ExcepcionCamposNulos(ExcepcionCampos):

    def __init__(self):
        super().__init__("Campo nulo, llene todos los espacios")

class ExcepcionNegativos(ExcepcionCampos):

    def __init__(self):
        super().__init__("No ingrese numero negativos")

class ExcepcionTiposMissMatch(ExcepcionCampos):

    def __init__(self):
        super().__init__("Los tipos de datos no coinciden")

class ExcepcionCodigoNoExite(ExcepcionRepetidos):

    def __init__(self):
        super().__init__("Esa entidad no existe, por favor verifique el codigo")

class ExcepcionConjuntoVacio(ExcepcionRepetidos):

    def __init__(self):
        super().__init__("No existen valores para la busqueda solicitada")
