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
        result_det = {}

        # Recorrer cada matriz en el diccionario de matrices
        for index, matrix in self.matrices.items():
            
            matrix = np.asarray(matrix)

            # Verificar si la matriz es cuadrada
            if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
                result_det[index] = (f"La matriz {index} debe ser cuadrada para calcular su determinante.")
                continue

            # Calcular el determinante de la matriz
            result_det[index] = round(np.linalg.det(matrix), 10)
        
        return result_det
            
