class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(gato.sonido())

hacer_sonido(perro)



def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
lista1 = [1,2,3,4]
lista2 = "maquina"

recorrer(lista1)