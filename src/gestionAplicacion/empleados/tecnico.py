from gestionAplicacion.empleados.empleado import Empleado

class Tecnico(Empleado):
    
    # Se crea el contructor
    def __init__(self, cedula, nombre, sueldo, comision, experiencia, correo=None, numeroContacto=None):
        # Se llama al contructor de la clase padre (Empleado)
        super().__init__(cedula, nombre, sueldo, comision)
        
        #Atributos
        self._experiencia = experiencia 
        
    # Se implementan los métodos

    # Métodos Getters & Setters

    # Atributo años de experiencia
    def setExperiencia(self, experiencia):
        self._experiencia = experiencia

    def getExperiencia(self):
        return self._experiencia
    
    # Método toString
    def __str__(self):
        return "Codigo Empleado: " + str(self.getCodigoEmpleado())+ "\n" + \
            		"Nombre: " + self.getNombre() + "\n" +  \
            		"Cedula: " + str(self.getCedula()) + "\n" \
            		"Sueldo: " + str(self.getSueldo()) + "\n" \
       				"Comision: " + str(self.getComision()) + "\n" \
					"Años de Experiencia: " + str(self._experiencia) + "\n" 
        
    
