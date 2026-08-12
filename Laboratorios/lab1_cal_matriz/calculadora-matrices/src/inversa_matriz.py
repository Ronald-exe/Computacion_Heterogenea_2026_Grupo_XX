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

        result_inv = {}

        # Recorrer cada matriz en el diccionario de matrices
        for index, matrix in self.matrices.items():
            
            matrix = np.asarray(matrix)

            # Verificar si la matriz es cuadrada
            if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
                result_inv[index] = (f"La matriz {index} debe ser cuadrada para calcular su inversa.")
                continue

            try:
                # Calcular la inversa de la matriz
                inversa = np.linalg.inv(matrix)
                result_inv[index] = inversa
            
            except np.linalg.LinAlgError:
                result_inv[index] = "La matriz no es invertible."

        return result_inv
            
