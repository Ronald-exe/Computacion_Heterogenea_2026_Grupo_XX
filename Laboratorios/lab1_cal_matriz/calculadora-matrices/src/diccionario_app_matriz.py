

class Aplicacion():
    """Clase que define la aplicación para calcular matrices"""
    def __init__(self):
        """Se recibe el diccionario de operaciones, se inicializa vacío"""
        self.diccionario = {}
    
    def registrar_operacion(self, nombre, operacion):
        """Es el metodo para registrar una operacion en el diccionario"""
        self.diccionario[nombre] = operacion
    
    def obtener_operacion(self, nombre):
        """Es el metodo que obtiene la operación del diccionario"""
        return self.diccionario.get(nombre)
    
    def obtener_operaciones(self):
        """Este método obtiene todas las operaciones del diccionario, es un recorrido completo"""
        return self.diccionario.keys()