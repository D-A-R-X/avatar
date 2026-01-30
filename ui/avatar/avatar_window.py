import os
import math

from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtCore import Qt, QTimer, QPoint

from ui.bubble.input_bubble import InputBubble
from ui.bubble.output_bubble import OutputBubble
from ui.voice.mic_listener import MicListener
from ui.api_contract import UIEvent
from ui.bubble.emotion_style import EMOTION_STYLE
from events.event_types import USER_TEXT_INPUT

# ==================================================
# PATH
# ==================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class AvatarWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ==================================================
        # WINDOW (WINDOWS SAFE)
        # ==================================================
        self.base_size = 150
        self.setFixedSize(self.base_size, self.base_size)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # ==================================================
        # STATE
        # ==================================================
        self.state = "IDLE"
        self.roaming = False
        self.direction = 1
        self.dragging = False

        # ==================================================
        # IMAGES (SAFE PATH)
        # ==================================================
        self.awake_pixmap = QPixmap(os.path.join(BASE_DIR, "cute_pet.png"))
        self.sleep_pixmap = QPixmap(os.path.join(BASE_DIR, "cute_pet_sleep.png"))
        self.current_pixmap = self.awake_pixmap

        # DEBUG (remove later)
        print("awake image ok:", not self.awake_pixmap.isNull())
        print("sleep image ok:", not self.sleep_pixmap.isNull())

        # ==================================================
        # BREATHING
        # ==================================================
        self.time = 0.0

        # ==================================================
        # GLOW
        # ==================================================
        self.glow = QGraphicsDropShadowEffect(self)
        self.glow.setBlurRadius(0)
        self.glow.setColor(QColor("#ffb6d5"))
        self.glow.setOffset(0, 0)
        self.setGraphicsEffect(self.glow)

        # ==================================================
        # BUBBLES
        # ==================================================
        self.input_bubble = InputBubble()
        self.output_bubble = OutputBubble()

        self.input_bubble.text_submitted.connect(self.on_text)
        self.input_bubble.mic_toggled.connect(self.toggle_mic)

        # ==================================================
        # MIC
        # ==================================================
        self.mic = MicListener()
        self.mic.text_ready.connect(self.on_voice_text)

        # ==================================================
        # TIMER
        # ==================================================
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.loop)
        self.timer.start(16)  # ~60 FPS

        # FORCE VISIBILITY
        self.move(300, 300)
        self.show()

        QTimer.singleShot(1000, lambda: self.show_chat("Hello 👋"))

    # ==================================================
    # PAINT (WINDOWS SAFE)
    # ==================================================
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        scale = 1.0 + math.sin(self.time) * 0.01
        scale = max(0.99, min(scale, 1.01))

        size = min(self.base_size, int(self.base_size * scale))
        x = (self.base_size - size) // 2
        y = (self.base_size - size) // 2

        painter.drawPixmap(x, y, size, size, self.current_pixmap)

    # ==================================================
    # LOOP
    # ==================================================
    def loop(self):
        self.time += 0.05
        self.update()

        if self.roaming and self.state == "IDLE":
            self.move(self.x() + self.direction, self.y())
            screen = self.screen().availableGeometry()
            if self.x() <= 0 or self.x() >= screen.width() - self.width():
                self.direction *= -1

        if self.output_bubble.isVisible():
            self.output_bubble.move(
                self.pos() + QPoint(
                    self.base_size // 2 - self.output_bubble.width() // 2,
                    -self.output_bubble.height() - 14
                )
            )

        if self.input_bubble.isVisible():
            self.input_bubble.move(
                self.pos() + QPoint(
                    self.base_size + 10,
                    self.base_size // 2 - self.input_bubble.height() // 2 - 30
                )
            )

    # ==================================================
    # STATE CONTROL
    # ==================================================
    def set_state(self, state: str):
        if state == self.state:
            return

        self.state = state
        self.current_pixmap = (
            self.sleep_pixmap if state == "SLEEP" else self.awake_pixmap
        )
        self.update()

    def apply_ai_state(self, state):
        self.set_state(state.avatar_state)

        style = EMOTION_STYLE.get(state.emotion, EMOTION_STYLE["neutral"])
        self.glow.setBlurRadius(style["glow"])

        if state.response_text:
            self.output_bubble.show_message(
                state.response_text,
                emotion=state.emotion
            )

        self.glow.setBlurRadius(0)

    # ==================================================
    # INPUT
    # ==================================================
    def on_text(self, text):
        if self.state == "SLEEP":
            return

        # 🔥 SEND DIRECT EVENT (NO UIEvent)
        if hasattr(self, "emit_ui_event"):
            self.emit_ui_event(USER_TEXT_INPUT, text)

    def on_voice_text(self, text):
        if self.state == "SLEEP":
            return
        if hasattr(self, "emit_ui_event"):
            self.emit_ui_event(UIEvent(type="INPUT", data={"text": text}))

    def toggle_mic(self, on):
        if self.state == "SLEEP":
            return
        self.mic.start() if on else self.mic.stop()

    # ==================================================
    # MOUSE
    # ==================================================
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_offset = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.drag_offset)

    def mouseReleaseEvent(self, event):
        self.dragging = False

    def mouseDoubleClickEvent(self, event):
        if self.input_bubble.isVisible():
            self.input_bubble.hide()
            self.output_bubble.hide()
        else:
            self.input_bubble.show()

    # ==================================================
    # KEYS
    # ==================================================
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            self.roaming = not self.roaming
        elif event.key() == Qt.Key_S:
            self.set_state("SLEEP")
        elif event.key() == Qt.Key_W:
            self.set_state("IDLE")

    def show_chat(self, text):
        if not text:
            return

        self.output_bubble.show_message(text)
        self.output_bubble.show()
