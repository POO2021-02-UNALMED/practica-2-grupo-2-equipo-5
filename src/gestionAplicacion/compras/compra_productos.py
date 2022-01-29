from compra import Compra

class CompraProductos(Compra):

    def __init__(self, fecha_de_compra, devolucion = False, descripcion = None, descuento = None):
        super().__init__(descripcion, descuento)

        # Atributos
        self._fecha_de_compra = fecha_de_compra
        self._devolucion = devolucion

        # Relación con DetalleProducto
        self._detalles_productos = None

    # Método para agregarle Detalles de productos a una compra de productos
    def agregarDetalleProducto(self, detalle_producto):
        if self._detalles_productos == None:
            self._detalles_productos = []
        self._detalles_productos.append(detalle_producto)

    # Métodos get
    def getFechaDeCompra(self):
        return self._fecha_de_compra

    def getDevolucion(self):
        return self._devolucion

    # Métodos set
    def setFechaDeCompra(self, fecha_de_compra):
        self._fecha_de_compra = fecha_de_compra

    def setDevolucion(self, devolucion):
        self._devolucion = devolucion

    # Método toString
    def __str__(self):
        return   super().__str__() \
               + "Fecha de compra: " + self.getFechaDeCompra() + "\n" \
               + "Devolución: " + str(self.getDevolucion()) + "\n"

