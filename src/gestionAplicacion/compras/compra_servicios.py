from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.compras.compra import Compra
class CompraServicios(Compra):
    """
        Clase encargada de clasificar las compras en
        compras de servicios, esta clase herada de 
        la clase Compra
    """

    def __init__(self, tiempo_de_culminacion:float, descripcion:str = None, descuento:float = None):
        """
            Constructor de la clase CompraServicios

            Args:
                tiempo_de_culminacion (float) : Tiempo que tardan todos los servicios de la compra en terminarse (horas)
                descripcion (str, opcional): Descripción de la compra. Defaults to None.
                descuento (float, opcional): Descuento aplicado a la compra. Defaults to None.
        """
        # Se llama al contructor de la clase padre
        super().__init__(descripcion, descuento)

        # Atributos
        self._tiempo_de_culminacion = tiempo_de_culminacion

        # Relación con Servicio
        self._servicios = None

    # Métodos get
    def getTiempoDeCulminacion(self) -> float:
        return self._tiempo_de_culminacion

    # Métodos set
    def setTiempoDeCulminacion(self, tiempo_de_culminacion: float) -> None:
        self._tiempo_de_culminacion = tiempo_de_culminacion

    def agregarServicio(self, servicio) -> None:
        """
            Metodo para agregar servicio a 
            una compra de servicios
        """
        if self._servicios == None:
            self._servicios = {}
        self._servicios[servicio.getId()] = servicio
    
    def obtenerTotal(self)->float:
        """Obtiene el total de todos los productos vendidos

        Returns:
            float: Total de productos vendidos
        """
        #Aquí obtenemos todos los precios del servicio y lo sumamos
        total = sum([servicio.getPrecio() for servicio in self._servicios])
        return total

    def __str__(self) -> str:
        """
            Método toString
        """
        return   super().__str__() \
               + "Tiempo de culminacion: " + str(self.getTiempoDeCulminacion()) + "\n"
    
    @staticmethod
    def hacerCompraServicio(codigo_compra, codigo_servicio):
        """Asocia una compra de servicio a un servicio.

        Args:
            codigo_compra (int): Codigo de la compra
            codigo_servicio (int): Codigo del servicio

        Returns:
            bool: ¿La transacción se realizó?
        """        
        
        compra_servicio = Compra.getCompras().get(codigo_compra)
        servicio = Servicio.getServicios().get(codigo_servicio)

        if compra_servicio and servicio: #Existen?
            if isinstance(compra_servicio, CompraServicios):
                compra_servicio.agregarServicio(servicio)
                return True
        
        return False
