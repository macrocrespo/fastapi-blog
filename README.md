# fastapi-blog

Blog construido con FastAPI.

---

## Requisitos

- Python 3.10+
- VSCode

### Extensiones de VSCode recomendadas

| Extensión | ID |
|---|---|
| Python | `ms-python.python` |
| Pylance | `ms-python.vscode-pylance` |
| Ruff (linter) | `charliermarsh.ruff` |

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd fastapi-blog

# 2. Crear el entorno virtual
python -m venv .venv

# 3. Activar el entorno virtual
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt
```

Dependencias principales: `fastapi`, `uvicorn`, `SQLAlchemy`, `alembic`, `psycopg[binary]`, `pydantic-settings`, `pillow`, `PyJWT`, `pwdlib`, `aiosmtplib`, `Jinja2`.

Seleccionar el intérprete en VSCode: `Ctrl+Shift+P` → `Python: Select Interpreter` → elegir `.venv`.

### Actualizar requirements.txt

Para regenerar `requirements.txt` a partir de las dependencias instaladas en el entorno virtual:

```bash
pip freeze > requirements.txt
```

---

## Base de datos

El proyecto ya no usa una base de datos local (SQLite, `blog.db`). Ahora usa **PostgreSQL**, que corre en un **contenedor de Docker** creado para este proyecto (nombre del contenedor y de la base de datos: `fastapi-blog`).

La URL de conexión se lee de la variable `DATABASE_URL` del archivo `.env`:

```
DATABASE_URL=postgresql+psycopg://<usuario>:<contraseña>@localhost:5432/fastapi-blog
```

Driver requerido:

```bash
pip install "psycopg[binary]"
```

### Migraciones con Alembic

Las tablas se gestionan con **Alembic**, en lugar de crearlas con `Base.metadata.create_all`.

Para inicializar Alembic en el proyecto (solo se hace una vez):

```bash
alembic init -t async alembic
```

Qué hace este comando:

- `alembic init`: crea la estructura de Alembic en el proyecto.
- `-t async`: usa la plantilla **asíncrona**, necesaria porque el proyecto usa SQLAlchemy async (`create_async_engine`).
- `alembic` (último argumento): nombre de la carpeta donde se genera, que contiene `env.py` (configuración de la conexión y los modelos), `script.py.mako` (plantilla de las migraciones) y `versions/` (donde se guardan las migraciones). También crea `alembic.ini` en la raíz.

---

## Ejecución

### Desarrollo (hot reload)

```bash
# Opción A — FastAPI CLI (recomendado)
fastapi dev

# Opción B — Uvicorn directo
uvicorn main:app --reload
```

### Producción

```bash
# Opción A — FastAPI CLI
fastapi run

# Opción B — Uvicorn directo
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

La app queda disponible en `http://localhost:8000`.  
Documentación automática en `http://localhost:8000/docs`.
