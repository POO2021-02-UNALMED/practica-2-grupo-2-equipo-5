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

from baseDatos.serializador import serializar
from baseDatos.deserializador import deserializar

if __name__ == "__main__":

    deserializar()

    ## CREACION OBJETOS DE PRUEBA

    # # compras de productos
    # compraProductos1 = CompraProductos(descripcion="Hello", descuento=0.05, 
    #                                    fecha_de_compra="30/01/2022")
    # compraProductos2 = CompraProductos(fecha_de_compra="22/02/2022", devolucion=True)
    # compraProductos3 = CompraProductos(descuento=0.02, fecha_de_compra="12/12/2021")
    # compraProductos4 = CompraProductos(descripcion="Es para un amigo", 
    #                                    fecha_de_compra="10/06/2021")

    # # compras de servicio
    # compraServicios1 = CompraServicios(tiempo_de_culminacion=4)
    # compraServicios2 = CompraServicios(descuento=0.04, tiempo_de_culminacion=24)
    # compraServicios3 = CompraServicios(descripcion="varios servicios de mantenimiento y reparacion",
    #                                    descuento=0.05, tiempo_de_culminacion=20)

    # # Tipos de servicio
    # tipoServicio1 = TipoServicio(nombre="Mantenimiento de PC")
    # tipoServicio2 = TipoServicio(nombre="Limpieza de PC")
    # tipoServicio3 = TipoServicio(nombre="Formateo de PC")
    # tipoServicio4 = TipoServicio(nombre="Mantenimiento de consolas")

    # # Servicios
    # servicio1 = Servicio(precio=10, fecha_servicio="12/01/2022", descripcion="Cambio de pasta termina",
    #                     tipoServicio=tipoServicio1, CompraServicios=compraServicios1)
    # tipoServicio1.agregarServicio(servicio1)
    # compraServicios1.agregarServicio(servicio1)

    # servicio2 = Servicio(precio=20, fecha_servicio="13/04/2020", descripcion="Repuesto de HDD y RAM",
    #                      tipoServicio=tipoServicio1, CompraServicios=compraServicios1)
    # tipoServicio1.agregarServicio(servicio2)
    # compraServicios1.agregarServicio(servicio2)

    # servicio3 = Servicio(precio=25, fecha_servicio="01/07/2021", descripcion="PS4 con lente sucio no reconoce CDs",
    #                     tipoServicio=tipoServicio4, CompraServicios=compraServicios2)
    # tipoServicio4.agregarServicio(servicio3)
    # compraServicios2.agregarServicio(servicio3)

    # servicio4 = Servicio(precio=43, fecha_servicio="01/04/2019", descripcion="Limpieza general pc",
    #                      tipoServicio=tipoServicio2, CompraServicios=compraServicios3)
    # tipoServicio2.agregarServicio(servicio4)
    # compraServicios3.agregarServicio(servicio4)

    # # Tipos de producto
    # tipoProducto1 = TipoProducto(nombre="Perifericos", impuesto= 0.1)
    # tipoProducto2 = TipoProducto(nombre="Consolas de videojuego", impuesto=0.15)
    # tipoProducto3 = TipoProducto(nombre="Accesorios", impuesto=0.05)
    # tipoProducto4 = TipoProducto(nombre="Drones", impuesto=0.02)

    # # Productos
    # producto1 = Producto(nombre="Mouse Logitech G502", fecha_ingreso="01/02/2019", precio=100)
    # producto2 = Producto(nombre="Diademas Razer Blackshark V2 X", fecha_ingreso="25/07/2020", precio=50)
    # producto3 = Producto(nombre="Playstation 5", fecha_ingreso="25/07/2020", precio = 599.99, descripcion="De fabrica")
    # producto4 = Producto(nombre="PS Plus 12 meses", fecha_ingreso="25/07/2020", precio=100, descripcion="Activar en tienda")

    # # Detalles de Producto
    # detalleProducto1 = DetalleProducto(garantia="2 anos", precio_garantia=60,
    #                                    producto=producto1, compraProductos=compraProductos1,esDevolucion=True)
    # producto1.agregarDetallesProducto(detalleProducto1)
    # compraProductos1.agregarDetallesProducto(detalleProducto1)

    # detalleProducto2 = DetalleProducto(garantia="5 anos", precio_garantia=200,
    #                                    producto=producto2, compraProductos=compraProductos1)
    # producto2.agregarDetallesProducto(detalleProducto2)
    # compraProductos1.agregarDetallesProducto(detalleProducto2)

    # detalleProducto3 = DetalleProducto(garantia="7 anos", precio_garantia=250,
    #                                    producto=producto4, compraProductos=compraProductos1)
    # producto4.agregarDetallesProducto(detalleProducto3)
    # compraProductos1.agregarDetallesProducto(detalleProducto3)

    # detalleProducto4 = DetalleProducto(producto=producto1, compraProductos=compraProductos2)
    # producto1.agregarDetallesProducto(detalleProducto4)
    # compraProductos2.agregarDetallesProducto(detalleProducto4)

    # detalleProducto5 = DetalleProducto(producto=producto3, compraProductos=compraProductos2)
    # producto3.agregarDetallesProducto(detalleProducto5)
    # compraProductos2.agregarDetallesProducto(detalleProducto5)

    # detalleProducto6 = DetalleProducto(producto=producto4, compraProductos=compraProductos3)
    # producto4.agregarDetallesProducto(detalleProducto6)
    # compraProductos3.agregarDetallesProducto(detalleProducto6)

    # detalleProducto7 = DetalleProducto(producto=producto1, compraProductos=compraProductos4)
    # producto1.agregarDetallesProducto(detalleProducto7)
    # compraProductos4.agregarDetallesProducto(detalleProducto7)

    # # Clientes
    # cliente1 = Cliente(nombre="Valentin Osorio",fecha_nacimiento="13/04/2000", 
    #                    direccion="Calle 30 #35-42", telefono= 3137865160)
    # cliente2 = Cliente(nombre="Andres Monsalve", fecha_nacimiento="24/05/2000")
    # cliente3 = Cliente(nombre="Fredy Orozco", fecha_nacimiento="08/6/2000", telefono=3212103863)

    # # Cajeros
    # cajero1 = Cajero(nombre="Alberto Guzman", sueldo=2500, comision = 0.0, 
    #                  correo="albergu@pjtech.com", cantidadEnVentas=3000, 
    #                  numeroContacto=32121)
    # cajero2 = Cajero(nombre="Pedro Jaramillo", sueldo=1000.8, comision= 0.05, 
    #                  correo="pjaramillo@pjtech.com", cantidadEnVentas=3000)
    # cajero3 = Cajero(nombre="Adrian Perez", sueldo=600, comision=0.02, 
    #                  cantidadEnVentas=0, numeroContacto=3457654423)

    # # Tecnicos
    # tecnico1 = Tecnico(nombre="Juan Gomez", sueldo=1500, comision = 0.0, experiencia=4)
    # tecnico2 = Tecnico(nombre= "Carlos Velez", sueldo=400, comision = 0.03, 
    #                    correo = "cvelez@pjtech.com", experiencia=1)

    # # Realizamos conexiones faltantes de los objetos
    # cliente1.agregarCompra(compraProductos1)
    # cliente1.agregarCompra(compraProductos2)
    # cliente2.agregarCompra(compraProductos3)
    # cliente3.agregarCompra(compraProductos4)

    # cajero1.agregarCompraProductos(compraProductos1)
    # cajero2.agregarCompraProductos(compraProductos4)
    # cajero2.agregarCompraProductos(compraProductos3)
    # cajero3.agregarCompraProductos(compraProductos2)

    # compraProductos1.setCliente(cliente1)
    # compraProductos1.setCajero(cajero1)
    # compraProductos2.setCliente(cliente1)
    # compraProductos2.setCajero(cajero3)
    # compraProductos3.setCliente(cliente2)
    # compraProductos3.setCajero(cajero2)
    # compraProductos4.setCliente(cliente3)
    # compraProductos4.setCajero(cajero2)

    # tecnico1.agregarTipoServicio(tipoServicio1)
    # tecnico1.agregarTipoServicio(tipoServicio4)
    # tecnico2.agregarTipoServicio(tipoServicio2)
    # tecnico2.agregarTipoServicio(tipoServicio3)

    # tipoServicio1.setTecnico(tecnico1)
    # tipoServicio2.setTecnico(tecnico2)
    # tipoServicio3.setTecnico(tecnico2)
    # tipoServicio4.setTecnico(tecnico1)

    # tipoProducto1.agregarProducto(producto1)
    # tipoProducto1.agregarProducto(producto2)
    # tipoProducto2.agregarProducto(producto3)
    
    # producto1.setTipoProducto(tipoProducto1)
    # producto2.setTipoProducto(tipoProducto1)
    # producto3.setTipoProducto(tipoProducto2)

    # PRUEBAS DE DATOS POR PANTALLA

    # Ver las compras de productos
    print("COMPRAS DE PRODUCTOS")
    for codigo, compraProductos in Compra.getCompras().items():
        if isinstance(compraProductos, CompraProductos):
            print(codigo)
            print(compraProductos)

    # Ver las compras de servicios
    print("COMPRAS DE SERVICIOS")
    for codigo, compraServicios in Compra.getCompras().items():
        if isinstance(compraServicios, CompraServicios):
            print(codigo)
            print(compraServicios)

    # Ver tipos de servicio
    print("TIPOS DE SERVICIO")
    for codigo, tipoServicio in TipoServicio.getTiposServicio().items():
        print(codigo)
        print(tipoServicio)

    # Ver los servicios
    print("SERVICIOS")
    for codigo, servicio in Servicio.getServicios().items():
        print(codigo)
        print(servicio.getTipoServicio().getNombre())
        print(servicio.getCompraServicios().getCodigoCompra())
        print(servicio)

    # Ver tipos de producto
    print("TIPOS DE PRODUCTO")
    for codigo, tipoProducto in TipoProducto.getTiposDeProductos().items():
        print(codigo)
        print(tipoProducto)

    # Ver los productos
    print("PRODUCTOS")
    for codigo, producto in Producto.getProductos().items():
        print(codigo)
        print(producto)

    # Ver los detalle de productos
    print("DETALLES DE PRODUCTOS")
    for codigo, detalleProducto in DetalleProducto.getDetallesProductos().items():
        print(codigo)
        print(detalleProducto.getProducto().getNombre())
        print(detalleProducto.getCompraProductos().getCodigoCompra())
        print(detalleProducto)

    # ver los clientes por consola
    print("CLIENTES")
    for cedula, cliente in Cliente.getClientes().items():
        print(cedula)
        print(cliente)

    # Ver los cajeros por consola
    print("CAJEROS")
    for cedula, cajero in Empleado.getEmpleados().items():
        if isinstance(cajero, Cajero):
            print(cedula)
            print(cajero)
    
    # Ver los tecnicos por consola
    print("TECNICOS")
    for cedula, tecnico in Empleado.getEmpleados().items():
        if isinstance(tecnico, Tecnico):
            print(cedula)
            print(tecnico)

    serializar()