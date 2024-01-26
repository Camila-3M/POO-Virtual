# class Diccionario:
#     def verificar_palabra(self,palabra):
#         # Implemantación de la lógica para verificar palabras
#         pass
    
# class CorrectorOrtográfico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self,texto):
#         # Usamos el diccionario para corregir el texto
#         pass
    
from abc import ABC, abstractmethod

class VerificadorOrtográfico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
        # Implemantación de la lógica para verificar palabras si estan en el diccionario
        pass

class ServicioOnline(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
        # Implemantación de la lógica para verificar palabras desde el servicio web
        pass
    
class CorrectorOrtográfico:
    def __init__(self,verificador):
        self.verificador = verificador
    
    def corregir_texto(self,texto):
        # Usamos el verificador para corregir texto
        pass
        
corrector = CorrectorOrtográfico(Diccionario())