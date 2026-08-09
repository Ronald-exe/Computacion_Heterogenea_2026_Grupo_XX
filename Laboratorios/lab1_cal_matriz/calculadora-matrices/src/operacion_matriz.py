from abc import ABC, abstractmethod

class Operacion(ABC):
    def __init__(self):
        self.matrices = {} # Diccionario para almacenar las matrices


    def SetMatrix(self, index, matrix): # Recibe la matriz con posición y le asigna el valor a la posición indicada 
        self.matrices[index] = matrix

    def Clear(self): # Reinicia el diccionario de matrices
        self.matrices = {}

    @abstractmethod # Compute es abstracto, no se puede dejar vacío, por lo que se llama a un abstractmethod para que se implemente en las clases hijas
    def Compute(self):
        pass