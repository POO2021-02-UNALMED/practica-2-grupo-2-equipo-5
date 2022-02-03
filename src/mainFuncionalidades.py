from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.empleados.empleado import Empleado
from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.compras.compra_servicios import CompraServicios
from gestionAplicacion.compras.compra_productos import CompraProductos
from gestionAplicacion.empleados.cajero import Cajero
from baseDatos.deserializador import deserializar

def clientesValiosos():

    lista = Cliente.clientesValiosos(0)
    for val in lista:
        print(val["cliente"])
        print(val["total"])

def comision():
    result = Empleado.calcularComision()
    for v in result:
        print(v)

def createServicio():

    servicio1 = Servicio(precio=10, fecha_servicio="12/01/2022", descripcion="Cambio de pasta termina")
    compra_servicio = CompraServicios(tiempo_de_culminacion=4)
    hecho = CompraServicios.hacerCompraServicio(compra_servicio.getCodigoCompra(), servicio1.getId())
    assert True == hecho

def createProducto():
    cliente1 = Cliente(nombre="Valentin Osorio",fecha_nacimiento="13/04/2000", direccion="Calle 30 #35-42", telefono= 3137865160)
    compraProductos1 = CompraProductos(descripcion="Hello", descuento=0.05, fecha_de_compra="30/01/2022")
    cajero1 = Cajero(nombre="Alberto Guzman", sueldo=2500, comision = 0.0, correo="albergu@pjtech.com", cantidadEnVentas=3000, numeroContacto=32121)
    hecho = CompraProductos.hacerCompraProducto(cliente1.getCedula(), compraProductos1.getCodigoCompra(), cajero1.getCedula())
    assert hecho == True

def testfail1():
    servicio1 = Servicio(precio=10, fecha_servicio="12/01/2022", descripcion="Cambio de pasta termina")
    compraProductos1 = CompraProductos(descripcion="Hello", descuento=0.05, fecha_de_compra="30/01/2022")
    hecho = CompraServicios.hacerCompraServicio(compraProductos1.getCodigoCompra(), servicio1.getId())
    assert hecho == False

def testfail2():
    cliente1 = Cliente(nombre="Valentin Osorio",fecha_nacimiento="13/04/2000", direccion="Calle 30 #35-42", telefono= 3137865160)
    cajero1 = Cajero(nombre="Alberto Guzman", sueldo=2500, comision = 0.0, correo="albergu@pjtech.com", cantidadEnVentas=3000, numeroContacto=32121)
    compra_servicio = CompraServicios(tiempo_de_culminacion=4)
    hecho = CompraProductos.hacerCompraProducto(cliente1.getCedula(), compra_servicio.getCodigoCompra, cajero1.getCedula())
    assert hecho == False

if __name__ == "__main__":
    deserializar()
    createServicio()
    createProducto()
    testfail1()
    testfail2()

