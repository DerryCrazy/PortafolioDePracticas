from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago
from ornitorrinco import Ornitorrinco

def main():
    #leon = Animal("Leon",5)
    #leon.hacer_sonido()

    perro = Perro("Willy", 6, "Boxer")
    perro.hacer_sonido()
    print(perro.es_cachorro())

    gato = Gato("Bartolo", 3, 3)
    gato.hacer_sonido()
    print("Vidas restantes: ", gato.vidas)
    print("Atropellado 🚌" if not gato.sobrevive() else "Vive 🐈")
    print("Vidas restantes: ", gato.vidas)
    print("Intoxicado ☣️" if not gato.sobrevive() else "Vive 🐈")
    print("Vidas restantes: ", gato.vidas)
    print("Electrocutado ⚡" if not gato.sobrevive() else "Vive 🐈")
    print("Vidas restantes: ", gato.vidas)
    #ave = Ave("KillerPollo", 1)
    #ave.hacer_sonido()

    #dracula=Murcielago("Dracula", 100, "Vampiro")
    #dracula.hacer_sonido()
    #dracula.soy_un()

    dracula = Murcielago(nombre="Drácula", especie="Vampiro", edad=500)
    dracula.comer()
    dracula.hacer_sonido()
    dracula.amamantar()
    dracula.dormir()
    dracula.volar()

    perry = Ornitorrinco("Ortitorrico", 5)
    perry.hacer_sonido()
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevo(s)")
    for i in range(3):
        perry.poner_huevo()
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevo(s)")
    pass
    print(f'{perry.especie}')

if __name__== '__main__':
    main()
