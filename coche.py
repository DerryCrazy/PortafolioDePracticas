class Coche:
    __velocidad =0
    __marcha=0
    __luces=False

    def __init__(self,luces = False):
        self.__luces=luces
        self.llantas = []

    def acelerar(self):
        self.__velocidad+=10

    def encender(self, motor):
        motor.encender()

    def agregarLlanta(self, llanta):
        if len(self.llantas) < 4:
            self.llantas.append(llanta)

    def frenar(self):
        self.__velocidad-=10

    def cambiarMarcha(self, marcha):
        self.__marcha=marcha

    def encenderLuces(self):
        self.__luces=True

    def __str__(self):
        return f"Velocidad: {self.__velocidad}, Marcha: {self.__marcha},Luces: {self.__luces}"

tsuru = Coche(True)
camaro = Coche()

print(tsuru)
tsuru.cambiarMarcha(2)

for i in range (1,9):
    tsuru.acelerar()

tsuru.cambiarMarcha(3)
tsuru.frenar()
print(f"{tsuru}")

print(camaro)

