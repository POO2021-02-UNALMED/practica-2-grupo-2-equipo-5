from gestionAplicacion.compras.cliente import Cliente
from gestionAplicacion.empleados.empleado import Empleado
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

def main():
    comision()

if __name__ == "__main__":
    deserializar()
    main()

