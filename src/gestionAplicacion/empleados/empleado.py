"""-------------------------------------------------"""
from tecnico import Tecnico
from cajero import Cajero

class Empleado():
    
    # diccionario para guardar todas las empleados registradas en el sistema
    _empleados = {}
    
    #Indice para tener identificador unico de los empleados
    _indexCodigoEmpleado = 0
    
    # Se crea el contructor
    def __init__(self, cedula, nombre, sueldo, comision, correo = None, numeroContacto = None):
        #Atributos
        self._cedula = cedula
        self._nombre = nombre
        self._sueldo = sueldo
        self._comision = comision
        self._codigoEmpleado = Empleado._indexCodigoEmpleado
        
        # Aumentar el indice del identificador
        Empleado._indexCodigoEmpleado += 1
        
        # Se guarda el objeto tipo Tecnico en el diccionario de empleados con su identificador como llave
        Empleado._empleados[self._codigoEmpleado] = self	
        
    # Se implementan los métodos 
    
    # Métodos Getters & Setters
    
    # Atributo cedula
    def setCedula(self, cedula):
        self._cedula = cedula
        
    def getCedula(self):
        return self._cedula
    
    # Atributo nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
    
    # Atributo sueldo
    def setSueldo(self, sueldo):
        self._sueldo = sueldo

    def getSueldo(self):
        return self._sueldo
    
    # Atributo comision
    def setComision(self, comision):
        self._comision = comision

    def getComision(self):
        return self._comision    
    
    # Atributo codigo de empleado
    def getCodigoEmpleado(self):
        return self._codigoEmpleado
    
    # Devuelve el diccionario de los empleados
    @classmethod
    def getEmpleados(cls):
        return cls._empleados
