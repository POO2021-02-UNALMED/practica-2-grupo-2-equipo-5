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
             "contador_clientes" : Cliente.getIndex(),
             "compras" : Compra.getCompras(),
             "contador_compras" : Compra.getIndex(),
             "empleados" : Empleado.getEmpleados(),
             "contador_empleados" : Empleado.getIndex(),
             "productos" : Producto.getProductos(),
             "contador_productos" : Producto.getIndex(),
             "tipo_productos" : TipoProducto.getTiposDeProductos(),
             "contador_tipo_producto" : TipoProducto.getIndex(),
             "detalles_de_productos" : DetalleProducto.getDetallesProductos(),
             "contador_detalles_producto" : DetalleProducto.getIndex(),
             "servicios" : Servicio.getServicios(),
             "contador_servicios" : Servicio.getIndex(),
             "tipo_servicios" : TipoServicio.getTiposServicio(),
             "contador_tipo_servicios" : TipoServicio.getIndex(),
            }

    direccion_parcial = os.path.join("src", "baseDatos", "temp")

    for archivo, dato in datos.items():
        picklefile = open(os.path.join(direccion_parcial, archivo), 'wb')
        pickle.dump(dato, picklefile)
        picklefile.close()
