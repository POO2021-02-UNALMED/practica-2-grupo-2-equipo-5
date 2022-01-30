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

def deserializar():
    """ Método encargado de guardar los datos del
        sistema al cerrar la app"""

    datos = {
             "clientes": lambda x : Cliente.setClientes(x),
             "compras" : lambda x : Compra.setCompras(x),
             "empleados" : lambda x : Empleado.setEmpleados(x),
             "productos" : lambda x : Producto.setProductos(x),
             "tipo_productos" : lambda x : TipoProducto.seTiposDeProductos(x),
             "detalles_de_productos" : lambda x : DetalleProducto.setDetallesProductos(x),
             "servicios" : lambda x : Servicio.setServicios(x),
             "tipo_servicios" : lambda x : TipoServicio.setTiposServicio(x),
            }

    direccion_parcial = os.path.join("src", "baseDatos", "temp")

    for archivo, set in datos.items():
        picklefile = open(os.path.join(direccion_parcial, archivo), 'rb')
        dato = pickle.load(picklefile)
        set(dato)
        picklefile.close()