class Servicio:
    """
        Clase encargada de administrar toda la informacion
        y funcionalidades relacionadas con los servicios 
        de la tienda
    """

    # diccionario para guardar todos los servicios registrados en el sistema
    _servicios = {}

    # Indice para tener identificador unico
    _count = 0
    
    def __init__(self, precio:float, fecha_servicio:str, descripcion:str, tipoServicio, CompraServicios) -> None:
        """
            Constructor de la clase Servicio

            Args:
                precio (float): precio del servicio
                fecha_servicio (str): fecha del servicio
                descripcion (str): descripción del servicio
                tipoServicio (TipoServicio): tipo de servicio asociado
                CompraServicios (CompraServicios): compra de servicios asociada
        """

        # Atributos
        self._id = Servicio._count
        self._precio = precio
        self._fecha_servicio = fecha_servicio
        self._descripcion = descripcion

        # Relacion con CompraServicio
        self._compra_servicios = CompraServicios

        # Relacion con TipoServicio
        self._tipo_servicio = tipoServicio

        # Relacion con Tecnico que revisa
        self._tecnico_revisa = None

        # Aumentar el indice del identificador
        Servicio._count += 1

        # Se guarda el objeto en un diccionario con su identificador como llave
        Servicio._servicios[self._id] = self

    #Métodos get
    def getId(self) -> int:
        return self._id

    def getPrecio(self) -> float:
        return self._precio
    
    def getFechaServicio(self) -> str:
        return self._fecha_servicio
    
    def getDescripcion(self) -> str:
        return self._descripcion

    def getCompraServicios(self):
        return self._compra_servicios

    def getTipoServicio(self):
        return self._tipo_servicio

    def getTecnicoRevisa(self):
        return self._tecnico_revisa

    #Métodos set
    def setPrecio(self, precio:float) -> None:
        self._precio = precio
    
    def setFechaServiio(self, fecha_servicio:str) -> None:
        self._fecha_servicio = fecha_servicio
    
    def setDescripcion(self, descripcion:str) -> None:
        self._descripcion = descripcion

    def setCompraServicios(self, compra_servicios) -> None:
        self._compra_servicios = compra_servicios

    def setTipoServicio(self, tipo_servicio) -> None:
        self._tipo_servicio = tipo_servicio

    def setTecnicoRevisa(self, tecnico_revisa) -> None:
        self._tecnico_revisa = tecnico_revisa

    @classmethod
    def getServicios(cls) -> dict:
        """
            Método de clase para obtener todos
            los servicios registrados en el sistema
        """
        return cls._servicios
    
    @classmethod
    def setServicios(cls, servicios:dict) -> None:
        """
            Método de clase para establecer todos
            los servicios registrados en el sistema
        """
        cls._servicios = servicios
    
    def __str__(self) -> str:
        """
            Método toString
        """
        return    "Id Servicio: "       + str(self._id) + "\n" \
                + "Precio: "            + str(self._precio) + "\n" \
                + "Fecha de servicio: " + str(self._fecha_servicio) + "\n" \
                + "Descripción: "       + str(self._descripcion) + "\n"
    