from gestionAplicacion import empleados
from gestionAplicacion.empleados.empleado import Empleado

class Cajero(Empleado):
    """
        Clase encargada de clasificar los empleados
        en cajeros, esta clase hereda de Empleado
    """

    def __init__(self, nombre:str, sueldo:float, comision:float, cantidadEnVentas:float, correo:str=None, numeroContacto:int=None) -> None:
        """
            Constructor de la clase Cajero

            Args:
                cedula (int): Cedula del empleado
                nombre (str): Nombre del empleado
                sueldo (float): Cantidad de dinero mensual que se gana el empleado
                comision (float): Determina cuanto se gana de comision el empleado
                correo (str, opcional): E-mail del empleado. Defaults to None.
                nuemroContacto (int, opcional): numero telefonico del empleado. Defaults to None.
                cantidadEnVentas (float): cantidad vendidad por el cajero en todas sus compras
        """
        # Se llama al contructor de la clase padre
        super().__init__(nombre, sueldo, comision, correo, numeroContacto)

        # Atributos
        self._cantidadEnVentas = cantidadEnVentas

        # Relacion con CompraProductos
        self._compras_productos_vendidas = None
    
    # Metodos get
    def getCantidadEnVentas(self) -> float:
        return self._cantidadEnVentas

    def getComprasProductos(self) -> dict:
        """
            Retorna las compras de procutos 
            vendidas por este cajero
        """
        return self._compras_productos_vendidas

    # Metodos set
    def setCantidadEnVentas(self, cantidadEnVentas:float):
        self._cantidadEnVentas = cantidadEnVentas

    def agregarCompraProductos(self, compra_productos) -> None:
        """
            Metodo para agregarle una CompraProductos que fue
            vendidad por un cajero
        """
        if self._compras_productos_vendidas == None:
            self._compras_productos_vendidas = {}
        self._compras_productos_vendidas[compra_productos.getCodigoCompra()] = compra_productos

    def __str__(self) -> str:
        """
            Método toString
        """
        return   super().__str__() \
       	       + "Cantidad en Ventas: " + str(self._cantidadEnVentas) + "\n"
    
    @staticmethod
    def crearInterfaz(nombre:str, sueldo:str, comision:str, cantidadEnVentas:str, correo:str, numeroContacto:str):
        sueldo = float(sueldo)
        comision = float(comision)
        numeroContacto = int(numeroContacto)

        Cajero(nombre,sueldo,comision,cantidadEnVentas,correo,numeroContacto)
        return True
