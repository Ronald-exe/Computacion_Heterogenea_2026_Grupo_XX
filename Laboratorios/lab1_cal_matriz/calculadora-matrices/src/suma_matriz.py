"""Módulo que implementa la suma de matrices."""

from operacion_matriz import Operacion


class suma_matriz(Operacion):
    """Operación de suma de matrices."""

    def Compute(self):
        """Suma dos matrices si tienen las mismas dimensiones.

        Returns:
            La matriz resultante de la suma o un mensaje de error.
        """
        A = self.matrices["A"]
        B = self.matrices["B"]

        if A.shape == B.shape:
            return A + B

        return "Solo se puede hacer suma con matrices de mismas dimensiones"
