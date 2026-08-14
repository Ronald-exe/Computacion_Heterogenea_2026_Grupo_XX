from matrices_carga import carga_matrices
from calculadora import Aplicacion
from suma_matriz import suma_matriz
from multiplicacion_matriz import multiplicacion_matriz
from inversa_matriz import inversa_matriz
from determinante_matriz import determinante_matriz
import typer

app = typer.Typer()

#Inicializa la aplicación y registra las operaciones.
aplicacion = Aplicacion()
suma = suma_matriz()
multiplicacion = multiplicacion_matriz()
inversa = inversa_matriz()
determinante = determinante_matriz()

#Registra las operaciones en la app para su uso posterior 
aplicacion.registrar_operacion("suma", suma)
aplicacion.registrar_operacion("multiplicacion", multiplicacion)
aplicacion.registrar_operacion("inversa", inversa)
aplicacion.registrar_operacion("determinante", determinante)


def cargar_operaciones_con_matrices():
    """Carga las matrices en cada operación registrada en la aplicación."""
    matrices = carga_matrices()
    for nombre in aplicacion.obtener_operaciones():
        operacion = aplicacion.obtener_operacion(nombre)
        operacion.SetMatrix("A", matrices["matrixA"])
        operacion.SetMatrix("B", matrices["matrixB"])
#Los siguientes @app son comandos de Typer para ejecución desde CLI
@app.command()
def sumar():
    """Realiza compute y calcula la suma de matrices."""
    cargar_operaciones_con_matrices()
    resultado = aplicacion.obtener_operacion("suma").Compute()
    typer.echo("Resultado de la suma:")
    typer.echo(resultado)

@app.command()
def multiplicar():
    """Realiza compute y calcula la multiplicación de matrices."""
    cargar_operaciones_con_matrices()
    resultado = aplicacion.obtener_operacion("multiplicacion").Compute()
    typer.echo("Resultado de la multiplicación:")
    typer.echo(resultado)   

@app.command()
def inversa():
    """Realiza compute y calcula la inversa de la matriz."""
    cargar_operaciones_con_matrices()
    resultado = aplicacion.obtener_operacion("inversa").Compute()
    typer.echo("Resultado de la inversa:")
    typer.echo(resultado)

@app.command()
def determinante():
    """Realiza compute y calcula el determinante de la matriz."""
    cargar_operaciones_con_matrices()
    resultado = aplicacion.obtener_operacion("determinante").Compute()
    typer.echo("Resultado del determinante:")
    typer.echo(resultado)

@app.command()
def calculadora():
    """Muestra las operaciones disponibles en la calculadora de matrices."""
    operaciones = aplicacion.obtener_operaciones()
    for operacion in operaciones:
        typer.echo(f"Operación: {operacion}")

if __name__ == "__main__":
    app()