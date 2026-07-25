# langflow-custom

Imagen Docker propia de Langflow con soporte para Custom Components.

## Qué es esto

Este repo reemplaza el uso de la imagen oficial `langflowai/langflow:latest` como
"Source Image" directa en Railway, por un build propio a partir de un Dockerfile.
Esto permite versionar y agregar Custom Components en Python.

## Estructura

```
.
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
├── .dockerignore
└── components/
    ├── data_utils/
    │   └── example.py
    └── whatsapp/
        └── example.py
```

## Cómo desplegar en Railway

1. Subí este repo a GitHub.
2. En Railway, andá al servicio `langflow` → Settings → Source.
3. Reemplazá "Docker Image" por "GitHub Repo" y elegí este repositorio.
4. Copiá las Variables de entorno que ya tenías configuradas en el servicio actual
   (usuario/contraseña de superusuario, DATABASE_URL de Postgres, etc.) al nuevo servicio,
   o mantenelas si estás editando el mismo servicio.
5. Railway va a buildear el Dockerfile automáticamente y desplegar.

## Cómo agregar un Custom Component nuevo

1. Creá una carpeta `components/mi_feature/`.
2. Agregá `components/mi_feature/__init__.py` (puede quedar vacío o con un docstring).
3. Escribí tu componente siguiendo el patrón de `components/data_utils/example.py`.
4. Hacé commit y push. Railway rebuildea automáticamente y el componente aparece
   en el panel de Langflow la próxima vez que cargue.

## Desarrollo local (opcional)

```bash
docker build -t langflow-custom .
docker run -p 7860:7860 langflow-custom
```

Luego accedé a http://localhost:7860
