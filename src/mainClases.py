from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.compras.compra import Compra
from gestionAplicacion.compras.compra_productos import CompraProductos
from gestionAplicacion.compras.compra_servicios import CompraServicios

from gestionAplicacion.empleados.empleado import Empleado
from gestionAplicacion.empleados.tecnico import Tecnico
from gestionAplicacion.empleados.cajero import Cajero

from gestionAplicacion.productos.detalle_producto import DetalleProductos
from gestionAplicacion.productos.producto import Producto
from gestionAplicacion.productos.tipo_producto import TipoProducto

from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.servicios.tipo_servicio import TipoServicio

if __name__ == "__main__":
    
    cajero1 = Cajero(1001025017, "Jaime Andres Monsalve", 2500, 400, 4200)
    tecnico1 = Tecnico(2128833828, "Valentin Osorio", 3000, 500, 5)
    
    print(cajero1)
    print(tecnico1)
    empleados = Empleado.getEmpleados()
    
    print(empleados)
    #for key in range(empleados):
    #    print(empleados[key])


    compraProductos1 = CompraProductos("12-02-2022", False, "Bueno", 0.05)

    print(compraProductos1)
