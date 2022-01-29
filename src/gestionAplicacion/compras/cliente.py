class Cliente:

    # diccionario para guardar todos los clientes registrados en el sistema
    _clientes = {}

    #Indice para tener identificador unico de los clientes
    _index_cedula = 0

    def __init__(self, nombre, fecha_nacimiento, direccion = None, telefono = None):

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

    # Método para agregarle compras a un cliente
    def agregarCompra(self, compra):
        if self._compras == None:
            self._compras = []
        self._compras.append(compra)

    # Métodos get
    def getCedula(self):
        return self._cedula

    def getNombre(self):
        return self._nombre

    # Aca hace falta pones una excepcion cuando sean nulos
    def getDirección(self):
        return self._direccion

    # Aca hace falta pones una excepcion cuando sean nulos
    def getTelefono(self):
        return self._telefono

    def getFechaNacimiento(self):
        return self._fecha_nacimiento

    # Métodos set
    def setNombre(self, nombre):
        self._nombre = nombre

    def setDireccion(self, direccion):
        self._direccion = direccion

    def setTelefono(self, telefono):
        self._telefono = telefono

    def setFechaNacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    # Método de clase para obtener todos los clientes registrados en el sistema
    @classmethod
    def getClientes(cls):
        return cls._clientes

    # Método de clase para establecer todos los clientes registrados en el sistema
    @classmethod
    def setClientes(cls, clientes):
        cls._clientes = clientes

    # Método toString
    def __str__(self):
        return    "Cédula: "              + str(self.getCedula()) + "\n" \
                + "Nombre: "              + self.getNombre() + "\n" \
                + "Direccion: "           + self.getDirección() + "\n" \
                + "Telefono: "            + str(self.getTelefono()) + "\n" \
                + "Fecha de nacimiento: " + self.getFechaNacimiento() + "\n"
                