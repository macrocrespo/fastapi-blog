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
pip install fastapi uvicorn[standard]
```

Seleccionar el intérprete en VSCode: `Ctrl+Shift+P` → `Python: Select Interpreter` → elegir `.venv`.

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
