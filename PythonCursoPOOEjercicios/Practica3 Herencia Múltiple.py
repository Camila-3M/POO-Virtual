class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola, soy {self.nombre} y estoy hablando")


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}"


class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print (f'Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

    
Roberto = EmpleadoArtista("Roberto",26,"colombiano","bailar",20000,"EMPER")

Roberto.presentarse()

herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)

instancia = isinstance(Roberto,Persona)
print(instancia)