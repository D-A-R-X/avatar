from events.event_types import AVATAR_CLICK, USER_TEXT_INPUT, AI_RESPONSE
from brain.responder import Responder
from shared.response_schema import AIChatResponse

class Orchestrator:
    def __init__(self, event_bus, state_manager):
        self.event_bus = event_bus
        self.state = state_manager
        self.responder = Responder()

        self.event_bus.subscribe(AVATAR_CLICK, self.on_avatar_click)
        self.event_bus.subscribe(USER_TEXT_INPUT, self.on_user_text)

    def on_avatar_click(self, data):
        print("[Orchestrator] Avatar clicked")

    def on_user_text(self, text):
        print(f"[Orchestrator] User said: {text}")
        self.state.set("busy", True)

        # ✅ self is VALID here
        response = self.responder.generate_reply(text)

        self.state.set("busy", False)

        # emit chat response
        chat_response = AIChatResponse(text=response["text"])
        self.event_bus.publish(AI_RESPONSE, chat_response)
