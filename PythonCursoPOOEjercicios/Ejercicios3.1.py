class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.5)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
        
Goku = Personaje("Goku",100,100)
Vegeta = Personaje("Vegeta",99,99)
Jiren = Personaje("Jiren",130,140)
Gogeta = Goku + Vegeta
Jireta = Jiren + Gogeta

print(Goku)
print(Vegeta)
print(Jiren)
print(Gogeta)
print(Jireta)