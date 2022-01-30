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

    def __str__(self) -> str:
        """
            Método toString
        """
        return   super().__str__() \
               + "Tiempo de culminacion: " + self.getTiempoDeCulminacion() + "\n" 