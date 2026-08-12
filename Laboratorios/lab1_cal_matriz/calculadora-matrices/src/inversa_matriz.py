import numpy as np

from operacion_matriz import Operacion

class inversa_matriz(Operacion):
    """
    Clase para calcular la inversa de una matriz.
    """

    def Compute(self):
        """
        Calcula la inversa de la matriz.
        """
        # Verificar si la matriz es cuadrada
        if self.matriz.shape[0] != self.matriz.shape[1]:
            return "La matriz debe ser cuadrada para calcular su inversa."
        try:
            # Calcular la inversa de la matriz
            inversa = np.linalg.inv(self.matriz)
            return inversa
            
        # Capturar la excepción si la matriz no es invertible    
        except np.linalg.LinAlgError:
            return "La matriz no es invertible."
