"""Módulo que implementa la multiplicación de matrices."""

from operacion_matriz import Operacion


class MultiplicacionMatriz(Operacion):
    """Operación de multiplicación de matrices."""

    def compute(self):
        """Multiplica dos matrices si sus dimensiones son compatibles.

        Returns:
            La matriz resultante de la multiplicación o un mensaje de error.
        """
        A = self.matrices["A"]
        B = self.matrices["B"]

        if A.shape[1] == B.shape[0]:
            return A @ B

        return (
            "Solo se puede hacer multiplicación con el mismo número "
            "de columnas y filas"
        )
