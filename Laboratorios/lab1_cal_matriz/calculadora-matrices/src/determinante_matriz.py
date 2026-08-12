import numpy as np

from operacion_matriz import Operacion

class determinante_matriz(Operacion):
    """
    Clase para calcular el determinante de una matriz.
    """

    def Compute(self):
        """
        Calcula el determinante de la matriz.
        """
        # Verificar si la matriz es cuadrada
        if self.matriz.shape[0] != self.matriz.shape[1]:
            return "La matriz debe ser cuadrada para calcular su determinante."

        # Calcular el determinante de la matriz
        determinante = np.linalg.det(self.matriz)
        return determinante
            
