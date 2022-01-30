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

    ## CREACION OBJETOS DE PRUEBA

    # Clientes
    cliente1 = Cliente(nombre="Valentin Osorio",fecha_nacimiento="13/04/2000", 
                       direccion="Calle 30 #35-42", telefono= 3137865160)
    cliente2 = Cliente(nombre="Andres Monsalve", fecha_nacimiento="24/05/2000")
    cliente3 = Cliente(nombre="Fredy Orozco", fecha_nacimiento="08/6/2000", telefono=3212103863)

    # ver los clientes por consola
    for cedula, cliente in Cliente.getClientes().items():
        print(cedula)
        print(cliente)

    # Cajeros
    cajero1 = Cajero(nombre="Alberto Guzman", sueldo=2500, comision = 0.0, 
                     correo="albergu@pjtech.com", cantidadEnVentas=3000, 
                     numeroContacto=32121)
    cajero2 = Cajero(nombre="Pedro Jaramillo", sueldo=1000.8, comision= 0.05, 
                     correo="pjaramillo@pjtech.com", cantidadEnVentas=3000)
    cajero3 = Cajero(nombre="Adrian Perez", sueldo=600, comision=0.02, 
                     cantidadEnVentas=0, numeroContacto=3457654423)

    # Tecnicos
    tecnico1 = Tecnico(nombre="Juan Gomez", sueldo=1500, comision = 0.0, experiencia=4)
    tecnico2 = Tecnico()


    # ver los cajeros por consola
    compra1 = CompraProductos(descripcion="Hello", descuento=0.05, 
                              fecha_de_compra="30/01/2022", devolucion=False)
    
    # Se hacen conexiones entre instancioas con los metodos definidos de las clases para ello
    cliente1.agregarCompra(compra1)
    compra1.setCliente(cliente1)
    cajero1.agregarCompraProductos(compra1)
    compra1.setCajero(cajero1)