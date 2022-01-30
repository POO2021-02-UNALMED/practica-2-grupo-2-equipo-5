from gestionAplicacion.empleados.empleado import Empleado

class Tecnico(Empleado):
    """
        Clase encargada de clasificar los empleados
        en Tecnicos, esta clase hereda de Empleado
    """
    
    def __init__(self, nombre:str, sueldo:float, comision:float, experiencia:int, correo:str=None, numeroContacto:int=None) -> None:
        """
            Constructor de la clase Tecnico

            Args:
                cedula (int): Cedula del empleado
                nombre (str): Nombre del empleado
                sueldo (float): Cantidad de dinero mensual que se gana el empleado
                comision (float): Determina cuanto se gana de comision el empleado
                correo (str, opcional): E-mail del empleado. Defaults to None.
                nuemroContacto (int, opcional): numero telefonico del empleado. Defaults to None.
                experiencia (int): anos de experiencai del tecnico
        """
        # Se llama al contructor de la clase padre
        super().__init__(nombre, sueldo, comision, correo, numeroContacto)
        
        # Atributos
        self._experiencia = experiencia 

        # Relacion con TipoServicio
        self._tipos_de_servicio = None

        # Relacion con Servicio
        self._servicios_revisados = None

    # Metodos get
    def getExperiencia(self) -> int:
        return self._experiencia

    def getTiposDeServicio(self) -> dict:
        """
            Retorna el tipo de servicios
            que realiza el tecnico
        """
        return self._tipos_de_servicio

    def getServiciosRevisados(self) -> dict:
        """
            Retorna los servicios que el
            tecnico ha revisado
        """
        return self._servicios_revisados

    # Metodos set
    def setExperiencia(self, experiencia:int) -> None:
        self._experiencia = experiencia
    
    def agregarTipoServicio(self, tipo_servicio) -> None:
        """
            Metodo para agregarle un Tipo de Servicio al
            tecnico
        """
        if self._tipos_de_servicio == None:
            self._tipos_de_servicio = {}
        self._tipos_de_servicio[tipo_servicio.getCodigo()] = tipo_servicio

    def agregarServicioRevisado(self, servicio) -> None:
        """
            Metodo para agregarle un Servicio a 
            revisar a un tecnico
        """
        if self._servicios_revisados == None:
            self._servicios_revisados = {}
        self._servicios_revisados[servicio.getId()] = servicio

    def __str__(self) -> str:
        """
            Método toString
        """
        return   super().__str__() \
               + "Años de Experiencia: " + str(self._experiencia) + "\n" 
        
    
