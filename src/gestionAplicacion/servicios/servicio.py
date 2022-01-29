class Servicio:
    _count = 0
    _Servicios = {}
    def __init__(self, precio:float, fecha_servicio:str, descripcion:str) -> None:
        """
        Args:
            precio (float): precio del servicio
            fecha_servicio (str): fecha del servicio
            descripcion (str):descripción del servicio
        """        

        self._precio = precio
        self._fecha_servicio = fecha_servicio
        self._descripcion = descripcion

        self._id = Servicio._count
        Servicio._count += 1
        Servicio._Servicios[self._id] = self

    #Métodos get
    def getPrecio(self)->float:
        return self._precio
    
    def getFechaServicio(self)->str:
        return self._fecha_servicio
    
    def getDescripcion(self)->str:
        return self._descripcion

    def getId(self)->int:
        return self._id
    
    @classmethod
    def  getServicios(cls)->dict:
        return cls._Servicios
    
    @classmethod
    def getCount(cls)->int:
        return cls._count

    #Métodos setters
    def setPrecio(self, precio:float)->None:
        self._precio = precio
    
    def setFechaServiio(self, fecha_servicio:str)->None:
        self._fecha_servicio = fecha_servicio
    
    def setDescripcion(self, descripcion:str)->None:
        self._descripcion = descripcion
    
    @classmethod
    def setServicios(cls, servicios)->None:
        cls._Servicios = servicios
    
    def __str__(self)->str:
        return  "id"                + str(self._id) + "\n" \
                + "precio: "        + str(self._precio) + "\n" \
                + "fecha de servicio: " + self._fecha_servicio + "\n" \
    