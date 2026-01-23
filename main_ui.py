import sys
from PySide6.QtWidgets import QApplication
from avatar.avatar_window import AvatarWindow
from api_contract import UIEvent
from dummy_ai import DummyAI
from voice.tts_player import TTSPlayer

class MainUI:
    def __init__(self):
        self.avatar = AvatarWindow()
        self.ai = DummyAI()
        self.avatar.emit_ui_event = self.emit_ui_event
        self.tts = TTSPlayer()

    def emit_ui_event(self, event: UIEvent):
        ai_state = self.ai.handle_event(event)
        self.avatar.apply_ai_state(ai_state)

        # 🔊 Speak AI response (NO THINKING)
        if ai_state.response_text:
            self.tts.speak(ai_state.response_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    sys.exit(app.exec())
