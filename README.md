# Computación Heterogénea 2026 — Grupo 1

## Profesor

| Rol | Nombre |
|---|---|
| Profesor | Luis Gerardo León Vega |

## Integrantes

| Nombre | Carnet | Rol |
|---|---|---|
| Ronald Duarte Barrantes | 2021004089 | Líder de equipo |
| Khaterine Salazar Martinez | 2014160591 | Desarrollador |
| Fabian Chacon Solano | 2018135154 | Desarrollador |
| Keylor Muñoz Soto. | 2020100689| Revisor |

---

## Información relevante

Primeramente, quiero dejar algunos aspectos operativos relevantes para que la continuidad del curso sea adecuada y no tengamos problemas de comunicación en el futuro. Estas son las reglas que propongo para el equipo:

- **Respeto:** toda opinión constructiva es bienvenida para la resolución de un problema. No hay ideas tontas: por favor participen en los syncs sin temor a hacerlo.
- **Compromiso:** todos debemos estar comprometidos con las fechas de entrega, con el trabajo en equipo y con las restricciones dadas por el profesor por escrito respecto al uso de IA (menor al 20%).
- **Updates:** es importante trabajar de manera constante para no batallar de último momento con las entregas. Por ello, cada quien debe compartir actualizaciones (avances) de su trabajo para evitar no entregar o entregar algo de forma mediocre.
- **Sinceridad:** sabemos que la universidad es una etapa intensa de estudio y que el aprendizaje consume mucho tiempo. Si en algún momento se ven sobrepasados por la carga, por favor comuníquenlo y tomaremos estrategias para aliviarla, trabajando de buena manera y sin atrasarnos. No habrá ninguna represalia por decir que no se ha podido avanzar, pero es importante avisar con tiempo para poder tomar medidas y ayudar en la medida de lo posible.

**Discord:** https://discord.gg/DNHzqZwXW

**One drive:** https://drive.google.com/drive/folders/14f0yPmSh8cU7nY3NXeMSStrlX9_5XDJZ?usp=drive_link

**OneNote:** https://estudianteccr-my.sharepoint.com/:o:/g/personal/ronald_estudiantec_cr/IgDYnr9V-MBSRYWkfc2jtYx-AWyIvp3Ch7zAGOlElKLD3DM?e=ibEaI5

---

## Disponibilidad de horario para los Sync

La idea es reunirnos al menos una vez por semana en un *Sync* (reunión para sincronizar el trabajo) de alrededor de 30 minutos. El objetivo principal de estas reuniones es:

- Determinar los puntos a trabajar en el día.
- Plantear metas.
- Dar un recuento de lo que se hizo el día anterior.
- Dar un recuento de lo que se planea hacer en el día actual.
- Dar un recuento de lo que se espera trabajar mañana.
- Compartir updates personales sobre los objetivos.
- Gestionar los objetivos de alta prioridad.
- Comentar sobre problemas que puedan estar frenando el desarrollo del equipo.

---
## Laboratorio 1

### Requerimientos:

| Sistema Operativo | Sistema de Construcción |
| --- | --- |
| Linux | Python UV |

- __Instalación de UV__

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


