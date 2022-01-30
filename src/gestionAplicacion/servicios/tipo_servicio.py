class TipoServicio():
    
    # Se crea el contructor
    def __init__(self, nombre):
        #Atributos
        self._nombre = nombre
        
	# Se implementan los métodos

    # Métodos Getters & Setters

    # Atributo nombre
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre
    
    # Método toString
    def __str__(self):
        return "Nombre: " + self._nombre 
