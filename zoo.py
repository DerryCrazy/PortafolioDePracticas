class Zoo:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los animales del zoológico
        self.animales = []

    def agregar_animal(self, animal):
        # Agrega un animal a la lista de animales del zoológico
        self.animales.append(animal)

    def alimentar_animales(self):
        # Recorre la lista de animales y llama al método 'comer' de cada animal
        for animal in self.animales:
            animal.comer()