import pickle
import os
from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.compras.compra import Compra
from gestionAplicacion.empleados.empleado import Empleado
from gestionAplicacion.productos.producto import Producto
from gestionAplicacion.productos.tipo_producto import TipoProducto
from gestionAplicacion.productos.detalle_producto import DetalleProducto
from gestionAplicacion.servicios.servicio import Servicio
from gestionAplicacion.servicios.tipo_servicio import TipoServicio

def serializar():
    """ Método encargado de guardar los datos del
        sistema al cerrar la app"""

    datos = {
             "clientes": Cliente.getClientes(),
             "compras" : Compra.getCompras(),
             "empleados" : Empleado.getEmpleados(),
             "productos" : Producto.getProductos(),
             "tipo_productos" : TipoProducto.getTiposDeProductos(),
             "detalles_de_productos" : DetalleProducto.getDetallesProductos(),
             "servicios" : Servicio.getServicios(),
             "tipo_servicios" : TipoServicio.getTiposServicio(),
            }

    direccion_parcial = os.path.join("src", "baseDatos", "temp")

    for archivo, dato in datos.items():
        picklefile = open(os.path.join(direccion_parcial, archivo), 'wb')
        pickle.dump(dato, picklefile)
        picklefile.close()
