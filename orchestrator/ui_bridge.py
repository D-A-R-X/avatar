from events.event_types import USER_TEXT_INPUT, AI_RESPONSE
from shared.response_schema import AIChatResponse, AIStateUpdate

class UIBridge:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    # UI → Backend
    def handle_ui_event(self, ui_event):
        if ui_event.type == "USER_INPUT":
            text = ui_event.data.get("text", "")
            self.event_bus.publish(USER_TEXT_INPUT, text)

    # Backend → UI
    def emit_chat_response(self, text: str):
        response = AIChatResponse(text=text)
        self.event_bus.publish(AI_RESPONSE, response)
