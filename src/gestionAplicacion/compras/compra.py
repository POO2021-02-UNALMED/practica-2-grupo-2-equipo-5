class Compra:

    # diccionario para guardar todas las compras registradas en el sistema
    _compras = {}

    #Indice para tener identificador unico de las compras
    _index_codigo_compra = 0

    def __init__(self, descripcion = None, descuento = None):

        # Atributos
        self._codigo_compra = Compra._index_codigo_compra
        self._descripcion = descripcion
        self._descuento = descuento

        # Relación con Cliente
        self._cliente = None

        # Aumentar el indice del identificador
        Compra._index_codigo_compra += 1

        # Se guarda el objeto en un diccionario con su identificador como llave
        Compra._compras[self._codigo_compra] = self

    # Método para asiganrle cliente a una compra
    def asignarCliente(self, cliente):
        self._cliente = cliente

    # Métodods get
    def getCodigoCompra(self):
        return self._codigo_compra

    def getDescripcion(self):
        return self._descripcion

    def getDescuento(self):
        return self._descuento

    # Métodos set
    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def setDescuento(self, descuento):
        self._descuento = descuento

    # Método de clase para obtener tas las compra registradss en el sistema
    @classmethod
    def getClientes(cls):
        return cls._compras

    # Método de clase para establecer todas las compras registradas en el sistema
    @classmethod
    def setClientes(cls, compras):
        cls._compras = compras

    # Método toString
    def __str__(self):
        return    "Codigo compra: " + str(self.getCodigoCompra()) + "\n" \
                + "Descripcion: "   + self.getDescripcion() + "\n" \
                + "Descuento: "     + self.getDescuento() + "\n"