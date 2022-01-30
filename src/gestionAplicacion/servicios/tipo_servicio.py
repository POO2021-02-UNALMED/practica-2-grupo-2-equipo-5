from gestionAplicacion.empleados.tecnico import Tecnico
from gestionAplicacion.servicios.servicio import Servicio


class TipoServicio():
    """
        Clase encargada de administrar toda la informacion
        y funcionalidades relacionadas con los tipos de 
        servicios de la tienda
    """

    # diccionario para guardar todos los tipos de servicios registrados en el sistema
    _tipos_de_servicios = {}

    # Indice para tener identificador unico
    _index_codigo = 0
    
    def __init__(self, nombre:str) -> None:
        """
            Constructor de la clase TipoServicio

            Args:
                nombre (str): nombre del tipo de servicio
        """

        #Atributos
        self._codigo = TipoServicio._index_codigo
        self._nombre = nombre

        # Relacion con tecnico
        self._tecnico = None

        # Relacion con servicio
        self._servicios = None

        # Aumentar el indice del identificador
        TipoServicio._index_codigo += 1

        # Se guarda el objeto en un diccionario con su identificador como llave
        TipoServicio._tipos_de_servicios[self._codigo] = self

    # Metodos get
    def getCodigo(self) -> int:
        return self._codigo

    def getNombre(self) -> str:
        return self._nombre

    def getTecnico(self) -> Tecnico:
        return self._tecnico

    def getServicios(self) -> dict:
        return self._servicios

    # Metodos set
    def setNombre(self, nombre) -> None:
        self._nombre = nombre

    def setTecnico(self, tecnico:Tecnico) -> None:
        self._tecnico = tecnico

    def agregarServicio(self, servicio:Servicio) -> None:
        """
            Metodo para asociar un tipo de servicio
            con un servicio
        """
        if self._servicios == None:
            self._servicios = {}
        if isinstance(servicio, Servicio):
            self._servicios[servicio.getId()] = servicio

    def __str__(self) -> str:
        """
            Método toString
        """
        return    "Codigo: " + str(self._codigo) + "\n" \
                + "Nombre: " + str(self._nombre) + "\n"