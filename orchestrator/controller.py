from events.event_types import (
    AVATAR_CLICK,
    USER_TEXT_INPUT,
    AI_RESPONSE,
    AI_STATE_UPDATE,
)
from brain.responder import Responder
from shared.response_schema import AIChatResponse, AIStateUpdate


class Orchestrator:
    def __init__(self, event_bus, state_manager):
        self.event_bus = event_bus
        self.state = state_manager
        self.responder = Responder()

        # event subscriptions
        self.event_bus.subscribe(AVATAR_CLICK, self.on_avatar_click)
        self.event_bus.subscribe(USER_TEXT_INPUT, self.on_user_text)
        self.event_bus.subscribe("SLEEP", self.on_sleep)
        self.event_bus.subscribe("WAKE", self.on_wake)
        self.event_bus.subscribe("ROAM_TOGGLE", self.on_roam_toggle)

    # ---------------- UI EVENTS ----------------

    def on_avatar_click(self, data=None):
        print("[Orchestrator] Avatar clicked")

    def on_user_text(self, text):
        print(f"[Orchestrator] User said: {text}")

        response = self.responder.generate_reply(text)
        chat_response = AIChatResponse(text=response["text"])
        self.event_bus.publish(AI_RESPONSE, chat_response)

    def on_sleep(self, data=None):
        update = AIStateUpdate(
            avatar_state="SLEEP",
            emotion="neutral",
        )
        self.event_bus.publish(AI_STATE_UPDATE, update)

    def on_wake(self, data=None):
        update = AIStateUpdate(
            avatar_state="IDLE",
            emotion="neutral",
        )
        self.event_bus.publish(AI_STATE_UPDATE, update)

    def on_roam_toggle(self, data=None):
        update = AIStateUpdate(
            avatar_state="WALK",
            emotion="neutral",
        )
        self.event_bus.publish(AI_STATE_UPDATE, update)
