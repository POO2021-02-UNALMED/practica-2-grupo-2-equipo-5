from compra import Compra

class CompraServicios(Compra):

    def __init__(self, tiempo_de_culminacion, descripcion = None, descuento = None):
        super().__init__(descripcion, descuento)

        # Atributos
        self._tiempo_de_culminacion = tiempo_de_culminacion

        # Relación con Servicio
        self._servicios = None

    # Método para agregarle Detalles de productos a una compra de productos
    def agregarServicio(self, servicio):
        if self._servicios == None:
            self._servicios = []
        self._servicios.append(servicio)

    # Métodos get
    def getTiempoDeCulminacion(self):
        return self._tiempo_de_culminacion

    # Métodos set
    def setTiempoDeCulminacion(self, tiempo_de_culminacion):
        self._tiempo_de_culminacion = tiempo_de_culminacion

    # Método toString
    def __str__(self):
        return   super().__str__() \
               + "Tiempo de culminacion: " + self.getTiempoDeCulminacion() + "\n" 