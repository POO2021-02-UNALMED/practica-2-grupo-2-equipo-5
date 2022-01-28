from sqlalchemy import desc


class Compra:

    #Indice para tener identificador unico de las compras
    _index_codigo_compra = 0

    def __init__(self, descripcion = None, descuento = None):

        # Atributos
        self._codigo_compra = Compra._index_codigo_compra
        self._descripcion = descripcion
        self._descuento = descuento

        # Relación con Cliente
        self._cliente = None

        Compra._index_codigo_compra += 1

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