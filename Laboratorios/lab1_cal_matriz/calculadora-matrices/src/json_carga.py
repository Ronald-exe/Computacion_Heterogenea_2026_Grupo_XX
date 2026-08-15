import json
from pathlib import Path


def cargar_json():
    """Carga un archivo JSON desde la ruta y retorna el contenido como un diccionario."""
    ruta_archivo = Path(__file__).parent.parent / "data" / "matrices.json"
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos 
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encuentra.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{ruta_archivo}' no contiene un formato JSON válido.")
        return None
