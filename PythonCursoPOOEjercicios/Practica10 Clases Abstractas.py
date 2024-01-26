from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,genero,actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,genero,actividad):
        super().__init__(nombre,edad,genero,actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy estudiando {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,genero,actividad):
        super().__init__(nombre,edad,genero,actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de {self.actividad}")
    
pedrito = Estudiante("Pedrito",25,"No Binario","programación")
lucas = Trabajador("Lucas",21,"Masculino","programación")

pedrito.presentarse()
pedrito.hacer_actividad()
print ("\n")
lucas.presentarse()
lucas.hacer_actividad()