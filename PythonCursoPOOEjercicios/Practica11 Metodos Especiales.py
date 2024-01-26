class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

# Metodo str    
dalto = Persona("Lucas",21)
print(dalto)

lista = (1,2,3)
print(lista)

print("\n")

# Metodo repr
repre = repr(dalto)
resultado = eval(repre)
print(resultado)

print("\n")

# Metodo add
pedro = Persona("Pedro",30,)
maria = Persona("María",18)
nueva_persona = dalto + pedro
print(nueva_persona)

nueva_persona = dalto + pedro + maria
print(nueva_persona)