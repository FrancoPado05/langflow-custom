# Dockerfile para Langflow con soporte para Custom Components
# Build reproducible y production-ready
# Base: imagen oficial de Langflow

FROM langflowai/langflow:1.10.3

# Metadatos
LABEL description="Langflow with Custom Components support"
LABEL version="1.0.0"

# Variables de entorno predeterminadas
# (Railway las puede sobrescribir con las que ya tenés configuradas como Variables del servicio)
ENV LANGFLOW_COMPONENTS_PATH=/app/components \
    PORT=7860 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Copiamos requirements primero para aprovechar el cache de Docker
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copiamos los Custom Components dentro de la imagen
COPY components /app/components

# Copiamos y damos permisos al entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 7860

HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:7860/health || exit 1

ENTRYPOINT ["/entrypoint.sh"]
