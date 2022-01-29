from itertools import product
from detalle_producto import DatalleProductos


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

        self._Detalle_Producto = []
        Producto._TodosProductos[self._codigo] = self

        def getCodigo(self)->int:
            """Retorna el código del producto"""    
            return self._codigo     

        
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
            self._descripcion = nueva_des
        
        def getProductos(self)->list:
            """Retorna la lista de los productos"""
            return self._Productos 
        
        def setProductos(self, list_products:list)->None:
            """Cambia la lista de productos 

            Args:
                list_products (list): Nueva lista de los productos.
            """            
            self._Productos = list_products
        
        def getDetalleProducto(self)->list:
            """Retorna una lista de productos asociados al objecto"""        
            return self._Deatalle_Producto
        
        def setDetalleProducto(self, productos:list)->None:
            """Se le asiga una lista de objectos tipo ProOk 
            Args:
                productos (list): [description]
            """        
            self._Deatalle_Producto = productos
        
        
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
        
        def agregarDetalleProductos(self, detalle_producto:DatalleProductos)->None:
            """Se agraga un tipo de detalle producto

            Args:
                detalle_producto (DatalleProductos): se agrega el nuevo producto, 
            """            
            if isinstance(detalle_producto, DatalleProductos):
                self._Detalle_Producto.append(detalle_producto)


        def __str__(self)->str:
             return   "Codigo"                + str(self._codigo) + "\n" \
                    + "Nombre: "              + self._nombre + "\n" \
                    + "Precio: "              + self._precio + "\n" \
                    + "Fecha Ingreso: "       + str(self._fecha_ingreso) + "\n" \
        



        
        

        