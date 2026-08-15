import numpy as np

from operacion_matriz import Operacion

class inversa_matriz(Operacion):
    """
    Clase para calcular la inversa de una matriz.
    """

    def Compute(self):
        """ 
        Calcula la inversa de las matrices A y B.

            - Se utiliza un bloque try-except para manejar el caso en que la matriz no sea invertible.
            - Si la matriz es invertible, se calcula su inversa utilizando np.linalg.inv().
            - Si la matriz no es invertible, se captura la excepción np.linalg.LinAlgError y se asigna un mensaje de error.
            
        """

        A = self.matrices["A"]
        B = self.matrices["B"]
        

        # Condición Matriz A
        if A.ndim == 2 and A.shape[0] == A.shape[1]:
            try:
                inv_A = f"Inversa de A:\n{np.linalg.inv(A)}"
            except np.linalg.LinAlgError:
                inv_A = "La matriz A no es invertible."
        else:   
            inv_A = "La matriz A no es cuadrada, no se puede calcular su inversa."
            

        # Condición Matriz B
        if B.ndim == 2 and B.shape[0] == B.shape[1]:
            try:
                inv_B = f"Inversa de B:\n{np.linalg.inv(B)}"
            except np.linalg.LinAlgError:
                inv_B = "La matriz B no es invertible."
        else:   
            inv_B = "La matriz B no es cuadrada, no se puede calcular su inversa."            

        return inv_A, inv_B
            
