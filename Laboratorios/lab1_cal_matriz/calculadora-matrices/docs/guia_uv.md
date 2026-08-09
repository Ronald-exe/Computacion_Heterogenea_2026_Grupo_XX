## Guia de entorno Python UV

### Requerimientos

| Sistema Operativo | Sistema de Construcción |
| --- | --- |
| Linux | Python UV |

### Configuración de UV

1. Actualizar la información de los repositorios y actualizar los paquetes instalados

```bash
sudo apt update

sudo apt upgrade

```
2. Instalar ``uv``

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Verificar versión

```bash
uv --version
```

4.  Creación del proyecto 

```bash
uv init --no-package --python 3.12 .
```
    
Se creará un archivo ``main.py`` por defecto, para eliminarlo usar la siguiente instrucción:

```bash
rm main.py
```

5. Sincronización con el repositorio
    
Al clonar este repositorio, este contiene los archivos: 

    ├── .python-version
    ├── pyproject.toml
    ├── uv.lock

Por lo cual, solamente será necesario ejecutar la siguiente instrucción:

```bash
uv sync
```

Verificar la sincronización:

```bash
uv --version
ls .venv
```

En caso de que no se quiera hacer la sincronización o no se haya realizado con éxito, la siguiente instrucción instala las bibliotecas que se requieren.

```bash
uv add numpy typer
```

Para los pasos anteriores no se requiere activar el entorno ``uv``, todo desde terminal se correría de la siguiente forma:

```bash
uv run nombre_archivo.py
```

En caso de no querer usar ``uv run`` se puede activar el entorno de la siguiente forma:


1. Eliminar la carpeta ``.venv`` que se crea

```bash
rm -rf .venv
```

2. Crear el entorno, nuevamente se creará la carpeta ``.venv`` con nombre más corto.

```bash
uv venv --python 3.12 --prompt .venv
```

3. Sincroniza

```bash
uv sync
```

4. Activar el entorno

```bash
source .venv/bin/activate
```

Tambien se puede consultar la documentacion de __UV__ en [Documentación oficial de UV](https://docs.astral.sh/uv/)