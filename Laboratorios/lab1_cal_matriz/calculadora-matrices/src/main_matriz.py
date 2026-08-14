from matrices_carga import carga_matrices
from calculadora import Calculadora
import typer

app = typer.Typer()

calculadora_app = Calculadora()

@app.command()
def sumar():
    """Realiza compute y calcula la suma de matrices."""
    matrices = carga_matrices()
    resultado = calculadora_app.calcular("suma", matrices["matrixA"], matrices["matrixB"])
    typer.echo("Resultado de la suma:")
    typer.echo(resultado)

@app.command()
def multiplicar():
    """Realiza compute y calcula la multiplicación de matrices."""
    matrices = carga_matrices()
    resultado = calculadora_app.calcular("multiplicacion", matrices["matrixA"], matrices["matrixB"])
    typer.echo("Resultado de la multiplicación:")
    typer.echo(resultado)   

@app.command()
def inversa():
    """Realiza compute y calcula la inversa de la matriz."""
    matrices = carga_matrices()
    resultado = calculadora_app.calcular("inversa", matrices["matrixA"], matrices["matrixB"])
    typer.echo("Resultado de la inversa:")
    typer.echo(resultado)

@app.command()
def determinante():
    """Realiza compute y calcula el determinante de la matriz."""
    matrices = carga_matrices()
    resultado = calculadora_app.calcular("determinante", matrices["matrixA"], matrices["matrixB"])
    typer.echo("Resultado del determinante:")
    typer.echo(resultado)

@app.command()
def calculadora():
    """Muestra las operaciones disponibles en la calculadora de matrices."""
    operaciones = calculadora_app.operaciones
    for operacion in operaciones:
        typer.echo(f"Operación: {operacion}")

if __name__ == "__main__":
    app()