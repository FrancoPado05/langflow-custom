"""
Ejemplo de Custom Component para Langflow.

Basado en la API de componentes de Langflow (langflow.custom.Component).
Reemplazá esto por tu propia lógica.

Documentación oficial: https://docs.langflow.org/custom-components
"""

from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data


class CleanTextComponent(Component):
    display_name = "Clean Text"
    description = "Limpia y normaliza un texto de entrada (trim, espacios dobles, etc.)"
    icon = "type"

    inputs = [
        MessageTextInput(
            name="input_text",
            display_name="Texto de entrada",
            info="Texto que se quiere limpiar",
        ),
    ]

    outputs = [
        Output(display_name="Texto limpio", name="output", method="clean"),
    ]

    def clean(self) -> Data:
        text = (self.input_text or "").strip()
        text = " ".join(text.split())
        return Data(data={"text": text})
