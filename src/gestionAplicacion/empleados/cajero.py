from gestionAplicacion.empleados.empleado import Empleado

class Cajero(Empleado):

    # Se crea el contructor
    def __init__(self, cedula, nombre, sueldo, comision, cantidadEnVentas, correo=None, numeroContacto=None):
        # Se llama al contructor de la clase padre (Empleado)
        super().__init__(cedula, nombre, sueldo, comision)

        #Atributos
        self._cantidadEnVentas = cantidadEnVentas
        
        
    # Se implementan los métodos

    # Métodos Getters & Setters

    # Atributo cantidad en ventas
    def setCantidadEnVentas(self, cantidadEnVentas):
        self._cantidadEnVentas = cantidadEnVentas

    def getCantidadEnVentas(self):
        return self._cantidadEnVentas

    # Método toString
    def __str__(self):
        return "Codigo Empleado: " + str(self.getCodigoEmpleado()) + "\n" + \
            	"Nombre: " + self.getNombre() + "\n" +  \
          		"Cedula: " + str(self.getCedula()) + "\n" \
          		"Sueldo: " + str(self.getSueldo()) + "\n" \
            	"Comision: " + str(self.getComision()) + "\n" \
       			"Cantidad en Ventas: " + str(self._cantidadEnVentas) + "\n"
