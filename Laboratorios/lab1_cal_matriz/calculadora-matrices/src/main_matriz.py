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
    """Muestra el menú interactivo de la calculadora de matrices."""
    continuar = True
    while(continuar):
        
        typer.echo("Calculadora de matrices")
        typer.echo("1. Suma")
        typer.echo("2. Multiplicación")
        typer.echo("3. Inversa")
        typer.echo("4. Determinante")
        
        opcion = typer.prompt("Seleccione una operación")
        
        opciones = {
            "1": "suma",
            "2": "multiplicacion",
            "3": "inversa",
            "4": "determinante"
        }
        
        if opcion not in opciones:
            typer.echo("Error: Seleccione una opción válida.")
            return
        
        nombre_operacion = opciones[opcion]
        matrices = carga_matrices()
        resultado = calculadora_app.calcular(nombre_operacion, matrices["matrixA"], matrices["matrixB"])
        
        typer.echo(f"Resultado de {nombre_operacion}:")
        typer.echo(resultado)
        
        respuesta = typer.prompt("¿Desea realizar otra operación? (s/n)")
        if respuesta.lower() == "n":
            continuar = False

if __name__ == "__main__":
    app()