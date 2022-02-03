class Producto:
    """
        Clase encargada de administrar toda la informacion
        y funcionalidades relacionadas con los productos
        de la tienda
    """

    # diccionario para guardar todos los productos registrados en el sistema
    _productos = {}

    # Indice para tener identificador unico de los productos
    _index_codigo = 0

    def __init__(self, nombre:str, fecha_ingreso:str, precio:float, descripcion:str=None) -> None:
        """
            Constructor de la clase Producto

            Args:
                nombre (str): Nombre del producto
                fecha_ingreso (str): Fecha de ingreso del producto
                precio (float): Precio del producto
                descripcion (str, opcional): Descripción del producto. Defaults to None.
        """

        # Atributos
        self._codigo = Producto._index_codigo
        self._nombre = nombre
        self._fecha_ingreso = fecha_ingreso
        self._precio = precio
        self._descripcion = descripcion

        # Relacion con DetalleProducto
        self._detalles_productos = None

        # Relacion con TipoProducto
        self._tipo_producto = None

        # Relacion con Productos (En caso de ser un combo)
        self._productos_combo = None

        # Aumentar el indice del identificador
        Producto._index_codigo += 1

        # Se guarda el objeto en un diccionario con su identificador como llave
        Producto._productos[self._codigo] = self
    
    # Metodos get
    def getCodigo(self) -> int:
        return self._codigo

    def getNombre(self) -> str:
        return self._nombre 

    def getFechaIngreso(self) -> str:
        return self._fecha_ingreso
    
    def getPrecio(self) -> float:
        return self._precio

    def getDescripcion(self) -> str:
        return self._descripcion

    def getDetallesProducto(self) -> dict:
        """
            Retorna los detalles de 
            los productos asociados a una compra
        """
        return self._detalles_productos

    def getTipoProducto(self):
        """
            Retorna el tipo de producto 
            asociado a ese producto
        """
        return self._tipo_producto

    def getProductos(self) -> dict:
        """
            Retorna los productos del combo, 
            en caso de ser un combo
        """
        return self._productos_combo 

    # Metodo set
    def setNombre(self, nombre:str) -> None:
        self._nombre = nombre

    def setFechaIngreso(self, fecha:str) -> None:
        self._fecha_ingreso = fecha

    def setPrecio(self, precio:float) -> None:
        self._precio = precio

    def setDescripcion(self, descripcion:str) -> None:
        self._descripcion = descripcion

    def agregarDetallesProducto(self, detalle_producto) -> None:
        """
            Metodo para agregar un detalle de 
            producto asociado a este producto
        """
        if self._detalles_productos == None:
            self._detalles_productos = {}
        self._detalles_productos[detalle_producto.getId()] = detalle_producto

    def setTipoProducto(self, tipo_producto) -> None:
        """
            Metodo para asiganr un 
            tipo de producto a este producto
        """
        self._tipo_producto = tipo_producto

    def agregarProductoCombo(self, producto) -> None:
        """
            Metodo para agregar un 
            producto en caso de formar combos
        """
        if self._productos_combo == None:
            self._productos_combo = {}
        if isinstance(producto, Producto):
            self._productos_combo[producto.getCodigo()] = producto

    @classmethod
    def getProductos(cls) -> dict:
        """
            Método de clase para obtener todos
            los productos registrados en el sistema
        """
        return cls._productos
    
    @classmethod
    def setProductos(cls, productos:dict) -> None:
        """
            Método de clase para establecer todos
            los productos registrados en el sistema
        """
        cls._productos = productos

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

    @staticmethod
    def crearInterfaz(nombre:str, fecha_ingreso:str, precio:float, descripcion:str):
        """Crea los valores de esta clase, que lo de la interfaz se inicializado por esta clase
        se pasa un booleano notificando que el valor está creado
        """        
        precio = float(precio)
        Producto(nombre, fecha_ingreso, precio, descripcion)
        return True

    def __str__(self)->str:
        """
            Método toString
        """
        return   "Codigo: "              + str(self._codigo) + "\n" \
               + "Nombre: "              + str(self._nombre) + "\n" \
               + "Fecha Ingreso: "       + str(self._fecha_ingreso) + "\n" \
               + "Precio: "              + str(self._precio) + "\n" \
               + "Descripcion: "         + str(self._descripcion) + "\n"