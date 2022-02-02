from gestionAplicacion.compras.cliente import Cliente
from baseDatos.deserializador import deserializar

def clientesValiosos():

    lista = Cliente.clientesValiosos(101)
    for val in lista:
        print(val["cliente"])
        print(val["total"])
def main():
    clientesValiosos()

if __name__ == "__main__":
    deserializar()
    main()

