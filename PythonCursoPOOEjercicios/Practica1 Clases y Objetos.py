class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f'Estás haciendo una llamada desde un: {self.modelo}')
        
    def colgar(self):
        print(f'Colgaste la llamada desde tu: {self.modelo}')
        
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 Pro","96MP")

celular2.llamar()
celular1.colgar()