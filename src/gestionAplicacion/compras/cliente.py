from gestionAplicacion.compras.compra import Compra

class Cliente:
    """
        Clase encargade de administrar toda la informacion
        y funcionalidades relacionadas con los clientes de 
        la tienda
    """

    # diccionario para guardar todos los clientes registrados en el sistema
    _clientes = {}

    # Indice para tener identificador unico de los clientes
    _index_cedula = 0

    def __init__(self, nombre:str, fecha_nacimiento:str, direccion:str = None, telefono:int = None) -> None:
        """
            Constructor de la clase Cliente

            Args:
                nombre (str): Nombre del cliente
                fecha_nacimiento (str, opcional): Fecha de nacimiento cliente
                direccion (str, opcional): Direccion del cliente. Defaults to None.
                telefono (int, opcional): Teefono del cliente. Defaults to None.
        """
        
        # Atributos
        self._cedula = Cliente._index_cedula
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._fecha_nacimiento = fecha_nacimiento

        # Relación con Compra
        self._compras = None

        # Aumentar el indice del identificador
        Cliente._index_cedula += 1

        # Se guarda el objeto en un diccionario con su identificador como llave
        Cliente._clientes[self._cedula] = self

    # Métodos get
    def getCedula(self) -> int:
        return self._cedula

    def getNombre(self) -> str:
        return self._nombre

    def getDirección(self) -> str:
        return self._direccion

    def getTelefono(self) -> int:
        return self._telefono

    def getFechaNacimiento(self) -> str:
        return self._fecha_nacimiento

    def getCompras(self) -> dict:
        """
            Metodo para devolver un diccionario con 
            las compras de un cliente
        """
        return self._compras

    # Métodos set
    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre

    def setDireccion(self, direccion:str) -> None:
        self._direccion = direccion

    def setTelefono(self, telefono:int) -> None:
        self._telefono = telefono

    def setFechaNacimiento(self, fecha_nacimiento:str) -> None:
        self._fecha_nacimiento = fecha_nacimiento

    def agregarCompra(self, compra:Compra) -> None:
        """
            Metodo para agregarle una compra a un cliente
        """
        if self._compras == None:
            self._compras = {}
        if isinstance(compra, Compra):
            self._compras[compra.getCodigoCompra()] = compra

    @classmethod
    def getClientes(cls) -> dict:
        """
            Método de clase para obtener todos
            los clientes registrados en el sistema
        """
        return cls._clientes

    @classmethod
    def setClientes(cls, clientes:dict) -> None:
        """
            Método de clase para establecer todos
            los clientes registrados en el sistema
        """
        cls._clientes = clientes

    def __str__(self) -> str:
        """
            Método toString
        """
        return    "Cédula: "              + str(self.getCedula()) + "\n" \
                + "Nombre: "              + self.getNombre() + "\n" \
                + "Direccion: "           + self.getDirección() + "\n" \
                + "Telefono: "            + str(self.getTelefono()) + "\n" \
                + "Fecha de nacimiento: " + self.getFechaNacimiento() + "\n"