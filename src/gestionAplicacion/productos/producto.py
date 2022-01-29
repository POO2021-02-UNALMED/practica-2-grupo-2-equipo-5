from tipo_producto import TipoProducto
class Producto:
    _TodosProductos = {}
    def __init__(self, codigo:int, nombre:str, fecha_ingreso:str, precio:float, descripcion:str=None) -> None:
        """Inicializador de la clase Producto

        Args:
            codigo (int): Código del producto
            nombre (str): Nombre del producto
            fecha_ingreso (str): Fecha de ingreso del producto
            precio (float): Precio del producto
            descripcion (str, optional): Descripción del producto. Defaults to None.
        """
        self._codigo = codigo
        self._nombre = nombre
        self._fecha_ingreso = fecha_ingreso
        self._precio = precio
        self._descripcion = descripcion

        self._Productos = []
        self._TipoProducto = []
        Producto._TodosProductos[self._codigo] = self

        def getCodigo(self)->int:
            """Retorna el código del producto"""    
            return self._codigo     

        def setCodigo(self, codigo:int)->None:
            """Cambia el código del producto"""
            self._codigo = codigo
        
        def getFechaIngreso(self)->str:
            return self._fecha_ingreso
        
        def setFechaIngreso(self, fecha:str)->None:
            """Cambia la fecha 

            Args:
                fecha (str): Nueva fecha a cambiar
            """
            self._fecha_ingreso = fecha
        
        def getPrecio(self)->float:
            """Retorna el precio"""
            return self._precio
        
        def setPrecio(self, nuevo_precio:float)->None:
            """Cambia el precio del objecto

            Args:
                nuevo_precio (float): nuevo precio del objecto.
            """
            self._precio = nuevo_precio
        
        def getDescpricion(self)->str:
            """Retorna la descripción del proyecto"""
            return self._descripcion
        
        def setDescripcion(self, nueva_des:str)->None:
            """Cambia la descripción del producto 

            Args:
                nueva_des (str): Es la nueva descripcion del producto
            """
            self.__descripcion = nueva_des
        
        def getProductos(self)->list:
            """Retorna la lista de los productos"""
            return self._Productos 
        
        def setProductos(self, list_products:list)->None:
            """Cambia la lista de productos 

            Args:
                list_products (list): Nueva lista de los productos.
            """            
            self._Productos = list_products
        
        def getTipoProductos(self)->list:
            """Retorna la lista de productos"""            
            return self._TipoProducto
        
        def setTipoProducto(self, tipo_producto:list)->None:
            """Cambia el valor a la lista de productos.

            Args:
                tipo_producto (list): Nueva lista de productos que se va a poner.
            """            
            self._TipoProducto = tipo_producto
        
        @classmethod
        def getTodosProductos(cls)->dict:
            """Retorna un diccionario con todos los Productos creados, donde la llave es la cédula y la valor el objecto"""
            return cls._TodosProductos
        
        @classmethod
        def setTodosProductos(cls, dict_productos:dict)->None:
            """Cambia el atributo de clase, donde está guardado todos los productos

            Args:
                dict_productos (dict): Recibe un diccionario donde la llave es la cédulas y el valor es el objecto.
            """
            cls._TodosProductos = dict_productos
        
        def agregarProducto(self, producto:Producto)->None:
            """Agraga un nuevo producto, es muy apropiado para hacer combos 

            Args:
                producto (Producto): > Producto que componen los combos
            """            
            if isinstance(producto, Producto):
                self._Producto.append(producto)
        
        def agregarTipoProducto(self, tipo_producto:TipoProducto)->None:
            """Agrega un tipo producto a la lista que tiene producto

            Args:
                tipo_producto (TipoProducto): Este es el tipo producto a agregar
            """            
            if isinstance(tipo_producto,TipoProducto):
                self._TipoProducto.append(tipo_producto)
        
        def __str__(self)->str:
             return   "Codigo"                + str(self._codigo) + "\n" \
                    + "Nombre: "              + self._nombre + "\n" \
                    + "Precio: "              + self._precio + "\n" \
                    + "Fecha Ingreso: "       + str(self._fecha_ingreso) + "\n" \
        



        
        

        