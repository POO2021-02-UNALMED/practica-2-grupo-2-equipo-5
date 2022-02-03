class Empleado():
    """
        Clase encargada de administrar toda la informacion
        y funcionalidades relacionadas con los empleados
        de la tienda
    """
    
    # diccionario para guardar todas las empleados registradas en el sistema
    _empleados = {}
    
    #Indice para tener identificador unico de los empleados
    _indexCodigoEmpleado = 0
    
    def __init__(self, nombre:str, sueldo:float, comision:float, correo:str=None, numeroContacto:int=None) -> None:
        """
            Constructor de la clase Empleado

            Args:
                cedula (int): Cedula del empleado
                nombre (str): Nombre del empleado
                sueldo (float): Cantidad de dinero mensual que se gana el empleado
                comision (float): Determina cuanto se gana de comision el empleado
                correo (str, opcional): E-mail del empleado. Defaults to None.
                nuemroContacto (int, opcional): numero telefonico del empleado. Defaults to None.
        """
        
        #Atributos
        self._cedula = Empleado._indexCodigoEmpleado
        self._nombre = nombre
        self._sueldo = sueldo
        self._comision = comision
        self._correo = correo
        self._numero_contacto = numeroContacto
        
        # Aumentar el indice del identificador
        Empleado._indexCodigoEmpleado += 1
        
        # Se guarda el objeto en el diccionario de empleados con su identificador como llave
        Empleado._empleados[self._cedula] = self	
    
    # Metodos get
    def getCedula(self) -> int:
        return self._cedula

    def getNombre(self) -> str:
        return self._nombre

    def getSueldo(self) -> float:
        return self._sueldo

    def getComision(self) -> float:
        return self._comision 

    def getCorreo(self) -> float:
        return self._correo

    def getNumeroContacto(self) -> int:
        return self._numero_contacto
    
    # Metodos set
    def setNombre(self, nombre:str) -> None:
        self._nombre = nombre

    def setSueldo(self, sueldo:float) -> None:
        self._sueldo = sueldo

    def setComision(self, comision:float) -> None:
        self._comision = comision

    def setCorreo(self, correo:float) -> None:
        self._correo = correo

    @classmethod
    def getEmpleados(cls) -> dict:
        """
            Método de clase para obtener todos
            los empleados registrados en el sistema
        """
        return cls._empleados

    @classmethod
    def setEmpleados(cls, empleados:dict) -> None:
        """
            Método de clase para establecer todos
            los empleados registrados en el sistema
        """
        cls._empleados = empleados

    @classmethod
    def getIndex(cls) -> int:
        """
            Metodo de clase que nos devuelve el
            estado actual del contador id unico
        """
        return cls._indexCodigoEmpleado

    @classmethod
    def setIndex(cls, indice:int) -> int:
        """
            Metodo de clase con el cual podemos
            restablcer el indice id unico al
            cargar de nuevo los datos
        """
        cls._indexCodigoEmpleado = indice
    
    @classmethod
    def calcularComision(cls)->list:
        """Calcula la comision de todos los empleados

        Returns:
            list: lista de diccionarios que devulve tres llaves
                -> empleado: Objecto empleado
                -> comision: comision del empleado
                -> total: total que se le debe pagar. Comisión + sueldo
        """

        informacion_empleados = []
        #Recorremos toda la lista de los empleados
        for empleado in cls._empleados.values():
            #Calculamos la comision del el empleado 
             comision = empleado.getComision() * empleado.getCantidadEnVentas()
             total = comision + empleado.getSueldo()
             #Rendereamos la información que se le va a mandar al fronted.
             data = {"empleado":empleado, "comision":comision, "total": total}
             informacion_empleados.append(data)
        
        return informacion_empleados


    def __str__(self) -> str:
        """
            Método toString
        """
        return    "Cédula: "          + str(self.getCedula())  + "\n" \
                + "Nombre: "          + str(self.getNombre())  + "\n" \
                + "Comision: "        + str(self.getComision())  + "\n"
