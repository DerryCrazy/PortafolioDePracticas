from animal import Animal

class Ave(Animal): #Las subclases estan obligadas a tener un constructor si la clase padre tiene un constructor
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)