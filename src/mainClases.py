from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.compras.compra import Compra
from gestionAplicacion.compras.compra_productos import CompraProductos
from gestionAplicacion.compras.compra_servicios import CompraServicios

from gestionAplicacion.empleados.empleado import Empleado
from gestionAplicacion.empleados.tecnico import Tecnico
from gestionAplicacion.empleados.cajero import Cajero

from gestionAplicacion.productos.detalle_producto import DetalleProducto
from gestionAplicacion.productos.producto import Producto
from gestionAplicacion.productos.tipo_producto import TipoProducto

from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.servicios.tipo_servicio import TipoServicio

if __name__ == "__main__":

    #Creacion de instancias de prueba
    cliente1 = Cliente(nombre="Valentin Osorio",fecha_nacimiento="13/04/2000", 
                       direccion="Calle 30 #35-42", telefono= 3137865160)
    cajero1 = Cajero(nombre="Alberto Guzman", sueldo=2500, comision = 0.0, 
                     correo="albergu@unal.edu.co", cantidadEnVentas=3000, 
                     numeroContacto=32121)
    compra1 = CompraProductos(descripcion="Hello", descuento=0.05, 
                              fecha_de_compra="30/01/2022", devolucion=False)
    
    # Se hacen conexiones entre instancioas con los metodos definidos de las clases para ello
    cliente1.agregarCompra(compra1)
    compra1.setCliente(cliente1)
    cajero1.agregarCompraProductos(compra1)
    compra1.setCajero(cajero1)

    print(compra1)
    print(compra1.getCliente())
    print(compra1.getCajero())
