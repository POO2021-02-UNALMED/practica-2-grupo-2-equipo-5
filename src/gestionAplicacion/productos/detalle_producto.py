"""Este es el paquete producto"""
from producto import Producto
from compras import CompraProductos


class DatalleProductos:
    """Esta clase es la encarga de llevar en detalle el producto"""
    _detalles_productos = {}
    _contador = 0

    def __init__(self, garantia:str, precio_garantia:float, esDevolucion:bool=False) -> None:
        """
        Args:
            garantia (str): Esté es el código de la garantía
            precio_garantia (float): cual es el precio de la garantía
            esDevolucion (boolean, optional): se pregunta si es una devolución. Defaults to False.
        """
        self._garantias = garantia
        self._precio_garantia = precio_garantia
        self._esDevolucion = esDevolucion
        self._id = DatalleProductos._contador
        
    
        DatalleProductos._detalles_productos[self._id] = self
        DatalleProductos._contador =+ 1
        
    
    def getGatarantias(self)->str:
        """Método de get del atributo PrecioGarantia, retorna un str."""    
        return self._garantias
    
    def setGarantias(self, garantia:str )->None:
        """Método set de atributo Garantias"""        
        self._garantias = garantia
    
    def getPrecioGarantia(self)->float:
        """Método de get del atributo PrecioGarantia, es un float"""        
        return self._garantias
    
    def setPreciosGarantias(self, precio:float)->None:
        """Método set del atributo garantias

        Args:
            precio (float): nuevo precio por el cual se le va cambiar el valor
        """        
        self._precio_garantia = precio
    
    def getEsDevolucion(self)->bool:
        """Retorna un booleano del atributo devolución"""        
        return self._esDevolucion
    
    def setEsDevolucion(self, esDevolucion:bool)->None:
        """metodo set para el atributo esDevolucion

        Args:
            esDevolucion (bool): ¿El producto es una devolución?
        """        
        self._esDevolucion = esDevolucion
    
    def getId(self)->int:
        """Retorna el id del objecto """        
        return self._id

    def getCompraProducto(self)->list:
        """Retorna una lista de objectos de CompraProducto"""        
        return self._CompraProductos
    
    
    @classmethod
    def getDetallesCompra(cls)->dict:
        """Retorna un diccionario con todos los DetalleseCompra. La llave es un id y el valor el objecto
        """        
        return cls._detalles_productos
    
    @classmethod
    def setDetallesCompra(cls, detalle:dict)->None:
        """Metodo set para el atributo de clase detalle compra

        Args:
            detalle (dict): un diccionario donde sus llaves son un id y sus valores son objectos de la clase DetalleCompra
        """        
        cls._detalles_productos = detalle
    
    @classmethod
    def getContador(cls)->int:
        """Retorna el contadot de la clase"""     
        return cls._contador
        
    def __str__(self):
        return      "Id: "                  + str(self._id) + "\n" \
                    + "Garantia: "            + self._garantias + "\n" \
                    + "Precio garantia: "     + self._precio_garantia + "\n" \
                    + "Es Devolución: "       + str(self._esDevolucion) + "\n" \
                
    
    


    



    