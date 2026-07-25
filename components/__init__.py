"""
Custom Components para Langflow.

Estructura:
    components/
    ├── data_utils/   # utilidades de procesamiento de datos
    └── whatsapp/     # integración con WhatsApp

Para agregar un componente nuevo:
    1. Crear una carpeta components/mi_feature/
    2. Agregar components/mi_feature/__init__.py
    3. Escribir el componente en un archivo .py dentro de esa carpeta
    4. Al redeployar, Langflow lo detecta automáticamente
       porque LANGFLOW_COMPONENTS_PATH=/app/components
"""
