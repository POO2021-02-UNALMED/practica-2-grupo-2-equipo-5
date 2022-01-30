from gestionAplicacion.compras.compra import Compra

class CompraProductos(Compra):
    """
        Clase encargada de clasificar las compras en
        compras de productos, esta clase herada de 
        la clase Compra
    """

    def __init__(self, fecha_de_compra:str, devolucion:bool = False, descripcion:str = None, descuento:float = None) -> None:
        """
            Constructor de la clase CompraProductos

            Args:
                fecha_de_compra (str): Fecha en la que se efectuó la compra
                devolucion (bool, opcional): Define si en la compra de productos hay devoluciones o no. Defaults to False.
                descripcion (str, opcional): Descripción de la compra. Defaults to None.
                descuento (float, opcional): Descuento aplicado a la compra. Defaults to None.
        """
        # Se llama al contructor de la clase padre
        super().__init__(descripcion, descuento)

        # Atributos
        self._fecha_de_compra = fecha_de_compra
        self._devolucion = devolucion

        # Relación con DetalleProducto
        self._detalles_productos = None

        # Relacion con Cajero
        self._cajero = None

    # Métodos get
    def getFechaDeCompra(self) -> str:
        return self._fecha_de_compra

    def isDevolucion(self) -> bool:
        return self._devolucion

    def getDetallesProducto(self) -> dict:
        """
            Retorna los detalles de 
            los productos asociados a una compra de productos
        """
        return self._detalles_productos

    def getCajero(self):
        """
            Retorna el cajero asociado a esta compra,
            es decir quien fue el encargado de la venta
        """
        return self._cajero

    # Métodos set
    def setFechaDeCompra(self, fecha_de_compra:str) -> None:
        self._fecha_de_compra = fecha_de_compra

    def setDevolucion(self, devolucion:bool) -> None:
        self._devolucion = devolucion

    def agregarDetallesProducto(self, detalle_producto) -> None:
        """
            Metodo para agregar un detalle de 
            producto a una compra de productos
        """
        if self._detalles_productos == None:
            self._detalles_productos = {}
        self._detalles_productos[detalle_producto.getId()] = detalle_producto

    def setCajero(self, cajero) -> None:
        """
            Metodo para asiganr un 
            cajero a una compra 
        """
        self._cajero = cajero

    def __str__(self) -> str:
        """
            Método toString
        """
        return   super().__str__() \
               + "Fecha de compra: " + self.getFechaDeCompra() + "\n" \
               + "Devolución: " + str(self.isDevolucion()) + "\n"

