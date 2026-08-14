# Calculadora Matricial CLI

## Descripción del Proyecto

La **Calculadora Matricial** es una aplicación de línea de comandos (CLI) desarrollada en Python que realiza operaciones aritméticas y algebraicas sobre matrices definidas en formato JSON. 

El sistema implementa una arquitectura basada en el patrón de diseño **Interfaz-Adaptador** y sigue un **enfoque modular**, donde cada clase e interfaz relevante se encuentra desacoplada en su propio módulo. Esta modularidad facilita el mantenimiento a largo plazo, la escalabilidad del sistema y optimiza el proceso de depuración de errores (*debugging*).

### Arquitectura de Clases y Módulos

La estructura lógica y los componentes principales del diseño se dividen de la siguiente manera:

* **Clase Abstracta `Operacion` (`operaciones.py`):** Define la interfaz base con los métodos abstractos `SetMatrix`, `Compute` y `Clear`. Actúa como la clase padre de la cual heredan todos los módulos de operaciones concretas.
* **`Suma` y `Multiplicacion`:** Operaciones binarias que requieren dos matrices como entrada. Hacen uso de la librería **NumPy** para realizar los cálculos de manera eficiente, validando las restricciones algebraicas correspondientes (p. ej., compatibilidad de dimensiones $m \times n$).
* **`Inversa` y `Determinante`:** Operaciones unarias que se aplican sobre una única matriz cuadrada, utilizando las rutinas de álgebra lineal de NumPy y gestionando las restricciones de diseño (p. ej., matrices no singulares con determinante distinto de cero).
* **Clase `Calculadora` (`calculadora.py`):** Gestiona el registro de operaciones mediante un diccionario de soporte. Contiene la lógica para validar si una operación solicitada está disponible y ejecutar el cálculo correspondiente.
* **Módulo `json_carga`:** Encargado del parseo y lectura de archivos `.json`, almacenando la información estructurada en memoria para su posterior manipulación.
* **Módulo `matrices_carga`:** Filtra e instancia los datos obtenidos por `json_carga`, transformándolos en los objetos matriciales requeridos por el módulo de operaciones.
* **Archivo `matrices.json`:** Estructura de datos persistente donde se definen y almacenan las matrices de entrada.
* **Punto de Entrada `Main_matriz` (`main.py`):** Corresponde a la capa de abstracción más alta. Integra la CLI construida con **Typer**, ofreciendo una interfaz intuitiva, clara y amigable para el usuario final.

---

## Diagrama de Diseño

A continuación se presenta el esquema de arquitectura y flujo de datos del sistema:

![Diagrama de Arquitectura](./img/UML_diagram.png)

> **Nota:** El diagrama fue elaborado utilizando herramientas de modelado vectorial (Draw.io / Lucidchart). Puede consultar o editar el archivo fuente directamente en la carpeta `docs/` del repositorio.

---

## Instrucciones de Instalación

Siga estos pasos para configurar el entorno de ejecución localmente:

### Requisitos Previos
* **Sistema Operativo:** Linux (Ubuntu/Pop!_OS o similar)
* **Lenguaje:** Python 3.10 o superior
* **Gestor de paquetes:** `uv` (o `pip`)
* **Control de versiones:** Git

## Instrucciones de Utilización
Para la utilziacion de este progama se tiene las siguientes ejemplos.

![Diagrama de Arquitectura](./img/img_1.jpeg)

Para acceder al menu de la calculadora mediante el typer, es necesario estar en la carpeta del archivo y utilizar el siguiente comando: uv run main_matriz.py --help con ese comando se desplegara el anterior comun, en donde notara las operaciones que soporta la calculadora, las cuales son: sumar, multiplicar, inversa y determinate, para usar estas operaciones desde terminal, debe emplear el siguiente comando:

- uv run main_matriz.py sumar
- uv run main_matriz.py multiplicar
- uv run main_matriz.py inversa
- uv run main_matriz.py determinante

Para hacer porbar matrices distintas se necesita hacer un cambio en el archivo matrices.json, pero la utilizacion de estas funciones se ve acontinuacion:

![Diagrama de Arquitectura](./img/img_2.jpeg)

En este apartado se denotan la utilizacion de los comandos necesarios para hacer las operaciones desde terminal sin necesidad de utilizar un menu, en caso de que se desee hacer una operacion de manera mas rapida para comprabar un resultado.

Pero si la idea es hacer varias operaciones, utlice la siguiente operando

- uv run main_matriz.py calculadora

Como se ve en el siguiente imagen: 

![Diagrama de Arquitectura](./img/img_3.jpeg)

Al momento de usar el comando de calculadora se despliega un menu ciclico que le permite hacer operaciones mas facilmente, sin la necesidad de escribir nuevamente el comando, simplemente utilizando los numero pertinente a la operacion (Keys)

### Pasos para la Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repositorio.git](https://github.com/tu-usuario/nombre-del-repositorio.git)
   cd nombre-del-repositorio