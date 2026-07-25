#!/bin/bash
# Entrypoint para Langflow con Custom Components
set -e

echo "Iniciando Langflow..."
echo "-----------------------------------------"
echo "LANGFLOW_COMPONENTS_PATH=$LANGFLOW_COMPONENTS_PATH"
echo "PORT=$PORT"
echo "-----------------------------------------"

# Si no hay DATABASE_URL seteada, avisamos (Railway ya te la inyecta si tenés Postgres conectado)
if [ -z "$LANGFLOW_DATABASE_URL" ]; then
    echo "Aviso: LANGFLOW_DATABASE_URL no está seteada como env var explícita."
    echo "Si tenés Postgres conectado en Railway, debería venir inyectada automáticamente."
fi

mkdir -p /app/data

# Arranca Langflow igual que lo hace la imagen oficial
exec langflow run --host 0.0.0.0 --port "${PORT:-7860}"
