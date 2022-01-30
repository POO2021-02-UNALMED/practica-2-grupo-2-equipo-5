from gestionAplicacion.productos.producto import Producto

class TipoProducto:
    _Tipo_Producto = {}
    def __init__(self, codigo:int, nombre:str, impuesto:float) -> None:
        """
        Args:
            codigo (int): Código del producto
            nombre (str): Nombre del producto
            impuesto (float): impuesto del producto
        """        
        self._codigo = codigo
        self._nombre = nombre
        self._impuesto = impuesto
        self._Productos = []

        TipoProducto._Tipo_Producto[self._codigo] = self

        def getCodigo(self)->int:
            """Retorna el código del tipo producto"""
            return self._codigo

        
        def getNombre(self)->str:
            """Retorna el nombre del tipo de producto"""
            return self._nombre
        
        def setNombre(self, nombre:str)->None:
            """Cambia en el nombre del objecto

            Args:
                nombre (str): cambia el nombre del producto
            """
            self._nombre = nombre
        
        def getImpuesto(self)->float:
            """Retorna el numero del impuesto"""
            return self._impuesto
        
        def setImpuesto(self, impuesto:float)->None:
            """Cambia el impuesto de los valores

            Args:
                impuesto (float): Nuevo impuesto por el que se va a cambiar
            """            
            self._impuesto = impuesto
        
        def getProductos(self)->list:
            """Retorna una lista con los productos asociado al tipo producto
            """            
            return self._Productos
         
        def setProductos(self, productos_list:list)->None:
            """Cambia el producto de la lista

            Args:
                productos_list (list): nueva lista de productos.
            """             
            self._Productos = productos_list
        
        @classmethod
        def getTipoProducto(cls)-> dict:
            """Retorna un diccionario con todos los valores de Tipo de Producto, donde la clave es codigo y el valor es el objecto"""
            return cls._Tipo_Producto
        
        @classmethod
        def setTipoProductos(cls, tipo_producto:dict):
            """Cambia el diccionario donde se va a guardar todos los Tipos Productos

            Args:
                tipo_producto (dict): Nuevo diccionario de tipo producto
            """            
            cls._TipoProducto = tipo_producto
        
        def agregarProducto(self, producto:Producto)->None:
            """Agrega un producto nuevo

            Args:
                producto (Producto): pruducto a agregar
            """            
            if isinstance(producto, Producto):
                self._Productos.append(producto)
        
        def __str__(self)->str:
             return   "Codigo"                + str(self._codigo) + "\n" \
                    + "Nombre: "              + self._nombre + "\n" \
                    + "Impuesto: "              + self.impuesto + "\n" \
        