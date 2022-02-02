class DetalleProducto:
    """
        Clase encargada de llevar la informacion especifica de un
        producto en una compra especifica
    """

    # diccionario para guardar todos los detalles de productos registradas en el sistema
    _detalles_productos = {}

    # Indice para tener identificador unico de los detalles de productos
    _contador = 0

    def __init__(self, producto, compraProductos, precio_garantia:float = 0.0, garantia:str= None, esDevolucion:bool=False) -> None:
        """
            Constructor de la clase DetalleProducto

            Args:
                garantia (str, opcional): Esté es el código de la garantía. Default to None.
                precio_garantia (float, opcional): cual es el precio de la garantía. Defaults to 0.0
                esDevolucion (boolean, optional): se pregunta si es una devolución. Defaults to False.
                producto (Producto): Prodcuto asociado
                compraProdcutos (CompraProductos): Compra asociada a ese detalle de producto
        """

        # Atributos
        self._id = DetalleProducto._contador
        self._garantia = garantia
        self._precio_garantia = precio_garantia
        self._esDevolucion = esDevolucion
        
        # Relacion con Producto
        self._producto = producto

        # Relacion con CompraProductos
        self._compra_productos = compraProductos

        # Se guarda el objeto en el diccionario de _detalles_productos con su identificador como llave
        DetalleProducto._detalles_productos[self._id] = self

        # Aumentar el indice del identificador
        DetalleProducto._contador += 1

    # Metodos get
    def getId(self) -> int:
        return self._id

    def getGatarantia(self) -> str:
        return self._garantia

    def getPrecioGarantia(self) -> float:
        return self._precio_garantia

    def getEsDevolucion(self) -> bool:
        return self._esDevolucion

    def getProducto(self):
        """
            Retorna el producto asociado a su 
            respectivo detalle
        """
        return self._producto

    def getCompraProductos(self):
        """
            Retorna la compra de productos a la 
            cual esta asociada el detalle de producto
        """
        return self._compra_productos

    # Metodos set
    def setGarantia(self, garantia:str) -> None: 
        self._garantia = garantia
    
    def setPreciosGarantias(self, precio:float) -> None:
        self._precio_garantia = precio
    
    def setEsDevolucion(self, esDevolucion:bool) -> None:
        self._esDevolucion = esDevolucion
    
    def setProducto(self, producto) -> None:
        """
            Metodo para asiganr un 
            producto a este detalle de producto
        """
        self._producto = producto

    def setCompraProdutos(self, compra_productos) -> None:
        """
            Metodo para asiganr una
            compra de productos a un detalle de productos
        """
        self._compra_productos = compra_productos
    
    
    @classmethod
    def getDetallesProductos(cls) -> dict:
        """
            Método de clase para obtener todos
            los detalles de productos registrados en el sistema
        """
        return cls._detalles_productos
    
    @classmethod
    def setDetallesProductos(cls, detalle:dict) -> None:
        """
            Método de clase para establecer todos
            los detalles de productos registrados en el sistema
        """
        cls._detalles_productos = detalle

    @classmethod
    def getIndex(cls) -> int:
        """
            Metodo de clase que nos devuelve el
            estado actual del contador id unico
        """
        return cls._contador

    @classmethod
    def setIndex(cls, indice:int) -> int:
        """
            Metodo de clase con el cual podemos
            restablcer el indice id unico al
            cargar de nuevo los datos
        """
        cls._contador = indice
        
    def __str__(self) -> str:
        """
            Método toString
        """
        return    "Id Detalle: "          + str(self._id) + "\n" \
                + "Garantia: "            + str(self._garantia) + "\n" \
                + "Precio garantia: "     + str(self._precio_garantia) + "\n" \
                + "Es Devolución: "       + str(self._esDevolucion) + "\n" 