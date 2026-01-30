import sys
from PySide6.QtWidgets import QApplication

from ui.avatar.avatar_window import AvatarWindow
from events.event_types import AI_RESPONSE, AI_STATE_UPDATE, USER_TEXT_INPUT


class MainUI:
    def __init__(self, bus):
        self.bus = bus
        self.avatar = AvatarWindow()

        # 🔗 Wire Avatar → Backend
        self.avatar.emit_ui_event = self.emit_ui_event

        # 🔗 Backend → UI
        self.bus.subscribe(AI_RESPONSE, self.on_ai_response)
        self.bus.subscribe(AI_STATE_UPDATE, self.on_state_update)

    def emit_ui_event(self, event_type, data):
        self.bus.publish(event_type, data)

    def on_ai_response(self, response):
        if response and hasattr(response, "text"):
            self.avatar.show_chat(response.text)

    def on_state_update(self, update):
        state = update.avatar_state

        if state == "SLEEP":
            self.avatar.set_state("SLEEP")
        elif state == "IDLE":
            self.avatar.set_state("IDLE")
        elif state == "WALK":
            self.avatar.roaming = True
