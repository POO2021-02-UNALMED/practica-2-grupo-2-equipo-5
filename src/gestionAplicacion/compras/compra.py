class Compra:
    """
        Clase encargada de administrar toda la informacion
        y funcionalidades relacionadas con las compras
        de la tienda
    """

    # diccionario para guardar todas las compras registradas en el sistema
    _compras = {}

    #Indice para tener identificador unico de las compras
    _index_codigo_compra = 0

    def __init__(self, descripcion:str = None, descuento:float = None) -> None:
        """
            Constructor de la clase Compra

            Args:
                descripcion (str, opcional): Descripción de la compra. Defaults to None.
                descuento (float, opcional): Descuento aplicado a la compra. Defaults to None.
        """

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

    # Métodods get
    def getCodigoCompra(self) -> int:
        return self._codigo_compra

    def getDescripcion(self) -> str:
        return self._descripcion

    def getDescuento(self) -> float:
        return self._descuento

    def getCliente(self) :
        return self._cliente

    # Métodos set
    def setDescripcion(self, descripcion:str) -> None:
        self._descripcion = descripcion

    def setDescuento(self, descuento:float) -> None:
        self._descuento = descuento
    
    def setCliente(self, cliente) -> None:
        """
            Método para asiganrle cliente a una compra
        """
        self._cliente = cliente

    @classmethod
    def getCompras(cls) -> dict:
        """
            Método de clase para obtener todas 
            las compra registradss en el sistema
        """
        return cls._compras

    @classmethod
    def setCompras(cls, compras:dict) -> None:
        """
            Método de clase para establecer todas 
            las compras registradas en el sistema
        """
        cls._compras = compras

    def __str__(self) -> str:
        """
            Método toString
        """
        return    "Codigo compra: " + str(self.getCodigoCompra()) + "\n" \
                + "Descripcion: "   + str(self.getDescripcion()) + "\n" \
                + "Descuento: "     + str(self.getDescuento()) + "\n"