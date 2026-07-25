"""
Ejemplo de Custom Component para enviar mensajes de WhatsApp.

Este es un placeholder: no llama a ninguna API real todavía.
Adaptalo a tu proveedor (Twilio, Meta Business API, etc.) agregando
la lógica dentro de send_message() y las dependencias en requirements.txt.

Documentación oficial: https://docs.langflow.org/custom-components
"""

from langflow.custom import Component
from langflow.io import MessageTextInput, Output, SecretStrInput
from langflow.schema import Data


class SendWhatsAppMessageComponent(Component):
    display_name = "Send WhatsApp Message"
    description = "Envía un mensaje de WhatsApp (placeholder, adaptar al proveedor real)."
    icon = "message-circle"

    inputs = [
        SecretStrInput(
            name="api_key",
            display_name="API Key",
            info="Credencial del proveedor de WhatsApp",
        ),
        MessageTextInput(
            name="to_number",
            display_name="Número destino",
        ),
        MessageTextInput(
            name="message",
            display_name="Mensaje",
        ),
    ]

    outputs = [
        Output(display_name="Resultado", name="output", method="send_message"),
    ]

    def send_message(self) -> Data:
        # TODO: reemplazar por la llamada real a tu proveedor (Twilio, Meta, etc.)
        if not self.api_key:
            return Data(data={"status": "error", "detail": "Falta API key"})

        return Data(data={
            "status": "not_implemented",
            "to": self.to_number,
            "message": self.message,
        })
