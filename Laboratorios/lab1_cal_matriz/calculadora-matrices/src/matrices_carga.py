import numpy as np
from json_carga import cargar_json

def carga_matrices():
    """Carga las matrices desde un archivo JSON y las convierte en arrays de NumPy."""
    matrices = {}
    datos = cargar_json()
    if datos is None:
        return "No existen los datos en la matriz.json"
    else:
        """Recorre el diccionario de datos y convierte cada matriz en un array de NumPy."""
        for mat1, mat2 in datos.items():
            matrices[mat1] = np.array(mat2["data"])
        return matrices