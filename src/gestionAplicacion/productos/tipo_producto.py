from gestionAplicacion.productos.producto import Producto

class TipoProducto:
    """
        Clase encargada de administrar toda la informacion
        y funcionalidades relacionadas con los tipos de 
        productos de la tienda
    """

    # diccionario para guardar todos los tipos productos registrados en el sistema
    _tipos_de_productos = {}

    # Indice para tener identificador unico de los tipos de poroductos
    _index_codigo = 0

    def __init__(self, nombre:str, impuesto:float) -> None:
        """
            Constructor de la clase TipoProducto

            Args:
                nombre (str): Nombre del producto
                impuesto (float): impuesto del producto
        """

        # Atributos
        self._codigo = TipoProducto._index_codigo
        self._nombre = nombre
        self._impuesto = impuesto

        # Relacion con Producto
        self._productos = None

        # Aumentar el indice del identificador
        TipoProducto._index_codigo += 1

        # Se guarda el objeto en un diccionario con su identificador como llave
        TipoProducto._tipos_de_productos[self._codigo] = self

    # Metodos get
    def getCodigo(self) -> int:
        return self._codigo

    def getNombre(self) -> str:
        return self._nombre

    def getImpuesto(self) -> float:
        return self._impuesto

    def getProductos(self) -> dict:
        """
            Retorna los productos asociados a
            este tipo de producto
        """
        return self._productos
    
    # Metodos set
    def setNombre(self, nombre:str) -> None:
        self._nombre = nombre
    
    def setImpuesto(self, impuesto:float) -> None:
        self._impuesto = impuesto
    
    def agregarProducto(self, producto:Producto) -> None:
        """
            Metodo para agregar un Producto
            asociado a este tipo de producto
        """
        if self._productos == None:
            self._productos = {}
        if isinstance(producto, Producto):
            self._productos[producto.getCodigo()] = producto

    @classmethod
    def getTiposDeProductos(cls) -> dict:
        """
            M??todo de clase para obtener todos
            los tipos de productos registrados en el sistema
        """
        return cls._tipos_de_productos
    
    @classmethod
    def seTiposDeProductos(cls, tipos_de_productos:dict) -> None:
        """
            M??todo de clase para establecer todos
            los tipos de productos registrados en el sistema
        """
        cls._tipos_de_productos = tipos_de_productos

    @classmethod
    def getIndex(cls) -> int:
        """
            Metodo de clase que nos devuelve el
            estado actual del contador id unico
        """
        return cls._index_codigo

    @classmethod
    def setIndex(cls, indice:int) -> int:
        """
            Metodo de clase con el cual podemos
            restablcer el indice id unico al
            cargar de nuevo los datos
        """
        cls._index_codigo = indice
    
    def __str__(self) -> str:
        """
            M??todo toString
        """
        return   "Codigo"      + str(self._codigo) + "\n" \
               + "Nombre: "    + str(self._nombre) + "\n" \
               + "Impuesto: "  + str(self._impuesto) + "\n" 