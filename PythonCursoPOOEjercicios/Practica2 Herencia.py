class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola, soy {self.nombre} y estoy hablando")
        
      
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad


Roberto = Empleado("Roberto",26,"colombiano","Programador",20000)

Sara = Estudiante("Sara",27,"ecuatoriana",18,"ESPE")

Roberto.hablar()

Sara.hablar()