class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

Pedro = Estudiante("Pedro",17,3)

print(Pedro.nombre)
print(Pedro.edad)
print(Pedro.grado)