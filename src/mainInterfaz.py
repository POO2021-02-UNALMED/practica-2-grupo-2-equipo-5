from interfaz.manager import Manager
from tkinter import *
from interfaz.pantallas.principal import Principal
from baseDatos.deserializador import deserializar
from baseDatos.serializador import serializar

if __name__ == "__main__":
    app = Manager()
    deserializar()
    app.mainloop()
    serializar()