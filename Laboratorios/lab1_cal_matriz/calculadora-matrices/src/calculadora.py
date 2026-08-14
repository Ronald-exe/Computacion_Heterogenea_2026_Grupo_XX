from suma_matriz import suma_matriz
from multiplicacion_matriz import multiplicacion_matriz
from inversa_matriz import inversa_matriz
from determinante_matriz import determinante_matriz

class Calculadora:
    def __init__(self):
        """Inicializa el diccionario de operaciones disponibles."""
        self.operaciones = {
            "suma": suma_matriz,
            "multiplicacion": multiplicacion_matriz,
            "inversa": inversa_matriz,
            "determinante": determinante_matriz
        }

    def calcular(self, nombre_op, Matriz_A, Matriz_B):
        """Realiza la operación especificada en las matrices."""
        if nombre_op not in self.operaciones:
            return "No es posible hacer la operacion"
        else:
            op = self.operaciones[nombre_op]()
            op.SetMatrix("A", Matriz_A)
            op.SetMatrix("B", Matriz_B)

            return op.Compute()