from abc import ABC, abstractmethod
import numpy as np

class Operacion(ABC):
    def __init__(self):
        """ Diccionario para almacenar las matrices """
        self.matrices = {} 
        

    def SetMatrix(self, index, matrix):
        """ Recibe la matriz con su key y le asigna el valor a la posición indicada """
        self.matrices[index] = np.array(matrix)

    def Clear(self):
        """ Reinicia el diccionario de matrices """
        self.matrices = {}

    @abstractmethod 
    
    def Compute(self):
        """ Compute es abstracto, no se puede dejar vacío, por lo que se llama a un abstractmethod para que se implemente en las clases hijas """
        pass