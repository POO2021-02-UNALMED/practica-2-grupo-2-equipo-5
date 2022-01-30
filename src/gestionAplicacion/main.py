from .empleados.empleado import Empleado
from .empleados.tecnico import Tecnico
from .empleados.cajero import Cajero

if __name__ == "__main__":
    
    cajero1 = Cajero(1001025017, "Jaime Andres Monsalve", 2500, 400, 4200)
    tecnico1 = Tecnico(2128833828, "Valentin Osorio", 3000, 500, 5)
    
    print(cajero1)
    print(tecnico1)
    empleados = Empleado.getEmpleados()
    
    print(empleados)
    #for key in range(empleados):
    #    print(empleados[key])
