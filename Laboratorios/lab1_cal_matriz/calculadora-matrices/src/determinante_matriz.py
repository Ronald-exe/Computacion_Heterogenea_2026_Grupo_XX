import numpy as np

from operacion_matriz import Operacion

class determinante_matriz(Operacion):
    """
    Operación para calcular el determinante de las matrices A y B.
    """

    def Compute(self):
        """
        Calcula el determinante para la matriz A y la matriz B.

        - Se hace una verificación para asegurarse de que la matriz sea cuadrada antes de calcular su determinante. 
        - Si la matriz no es cuadrada, se devuelve un mensaje de error correspondiente.
        - En caso de que la matriz sea cuadrada, se utiliza la función np.linalg.det() para calcular su determinante.
        """
        # Matrices A y B
        A = self.matrices["A"]
        B = self.matrices["B"]

        # Condición Matriz A
        if A.ndim == 2 and A.shape[0] == A.shape[1]:
            # Calcula el determinante de la matriz A
            det_A = np.linalg.det(A)
        
        else:
            det_A = "La matriz A no es cuadrada, no se puede calcular su determinante."
            

        # Condición Matriz B
        if B.ndim == 2 and B.shape[0] == B.shape[1]:
            # Calcula el determinante de la matriz B
            det_B = np.linalg.det(B) 
            
        else:
            det_B = "La matriz B no es cuadrada, no se puede calcular su determinante."
            
        return det_A, det_B
            
