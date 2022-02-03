class ErrorAplicacion(Exception):

    def __init__(self, mensaje):
        self._error = "Manejo de errores de la aplicacion "+ mensaje
        super().__init(self._error)

class ExcepcionC1(ErrorAplicacion):

    def __init__(self, mensaje):
        self._error = "ExcepcionC1 " + mensaje
        super().__init__(self._error)

class ExcepcionC2(ErrorAplicacion):

    def __init__(self, mensaje):
        self._error = "ExcepcionC2 " + mensaje
        super().__init__(self._error)

class ExcepcionInventada1(ExcepcionC1):

    def __init__(self):
        super().__init__("ExcepcionInvetada1")

class ExcepcionInventada2(ExcepcionC1):

    def __init__(self):
        super().__init__("ExcepcionInvetada2")

class ExcepcionSugerida1(ExcepcionC1):

    def __init__(self):
        super().__init__("ExcepcionSugerida1")

class ExcepcionInventada3(ExcepcionC2):

    def __init__(self):
        super().__init__("ExcepcionInvetada3")

class ExcepcionInventada4(ExcepcionC2):

    def __init__(self):
        super().__init__("ExcepcionInvetada4")

class ExcepcionSugerida2(ExcepcionC2):

    def __init__(self):
        super().__init__("ExcepcionSugerida2")