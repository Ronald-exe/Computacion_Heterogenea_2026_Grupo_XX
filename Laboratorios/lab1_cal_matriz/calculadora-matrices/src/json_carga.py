import json

def cargar_json(ruta_archivo):
    """Carga un archivo JSON desde la ruta y retorna el contenido como un diccionario."""
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