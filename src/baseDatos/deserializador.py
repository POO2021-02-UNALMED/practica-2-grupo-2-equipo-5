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
    """ Método encargado de carcar  los datos del
        sistema al abrir la app"""

    datos = {
             "clientes": lambda x : Cliente.setClientes(x),
             "contador_clientes" : lambda x : Cliente.setIndex(x),
             "compras" : lambda x : Compra.setCompras(x),
             "contador_compras" : lambda x : Compra.setIndex(x),
             "empleados" : lambda x : Empleado.setEmpleados(x),
             "contador_empleados" : lambda x : Empleado.setIndex(x),
             "productos" : lambda x : Producto.setProductos(x),
             "contador_productos" : lambda x : Producto.setIndex(x),
             "tipo_productos" : lambda x : TipoProducto.seTiposDeProductos(x),
             "contador_tipo_producto" : lambda x : TipoProducto.setIndex(x),
             "detalles_de_productos" : lambda x : DetalleProducto.setDetallesProductos(x),
             "contador_detalles_producto" : lambda x : DetalleProducto.setIndex(x),
             "servicios" : lambda x : Servicio.setServicios(x),
             "contador_servicios" : lambda x : Servicio.setIndex(x),
             "tipo_servicios" : lambda x : TipoServicio.setTiposServicio(x),
             "contador_tipo_servicios" : lambda x : TipoServicio.setIndex(x),
            }

    direccion_parcial = os.path.join("src", "baseDatos", "temp")

    for archivo, set in datos.items():
        picklefile = open(os.path.join(direccion_parcial, archivo), 'rb')
        dato = pickle.load(picklefile)
        set(dato)
        picklefile.close()