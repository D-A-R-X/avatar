from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtCore import Qt, QTimer, QPoint
import math

from bubble.input_bubble import InputBubble
from bubble.output_bubble import OutputBubble
from voice.mic_listener import MicListener


# ==================================================
# AVATAR STATE CONTRACT (DO NOT VIOLATE)
# --------------------------------------------------
# Allowed states:
#   IDLE
#   WALK
#   HOVER
#   CLICK_REACT
#   SLEEP
#
# Rules:
# - Avatar NEVER decides its own state
# - Avatar NEVER changes state automatically
# - Avatar ONLY reacts to set_state(state)
# - Avatar contains ZERO AI / emotion logic
# ==================================================


class AvatarWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ==================================================
        # 🔒 WINDOW (FIXED SIZE — WIN11 SAFE)
        # ==================================================
        self.base_size = 150
        self.setFixedSize(self.base_size, self.base_size)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFocusPolicy(Qt.StrongFocus)

        # ==================================================
        # STATE (DATA ONLY)
        # ==================================================
        self.state = "IDLE"
        self.roaming = False
        self.direction = 1
        self.dragging = False

        # ==================================================
        # IMAGES
        # ==================================================
        self.awake_pixmap = QPixmap("avatar/cute_pet.png")
        self.sleep_pixmap = QPixmap("avatar/cute_pet_sleep.png")
        self.current_pixmap = self.awake_pixmap

        # ==================================================
        # BREATHING (VISUAL ONLY)
        # ==================================================
        self.time = 0.0

        # ==================================================
        # GLOW EFFECT
        # ==================================================
        self.glow = QGraphicsDropShadowEffect(self)
        self.glow.setBlurRadius(0)
        self.glow.setColor(QColor("#ffb6d5"))
        self.glow.setOffset(0, 0)
        self.setGraphicsEffect(self.glow)

        # ==================================================
        # CHAT BUBBLES
        # ==================================================
        self.input_bubble = InputBubble()
        self.output_bubble = OutputBubble()

        self.input_bubble.text_submitted.connect(self.on_text)
        self.input_bubble.mic_toggled.connect(self.toggle_mic)

        # ==================================================
        # MIC (DUMB LAYER)
        # ==================================================
        self.mic = MicListener(self.on_voice_text)

        # ==================================================
        # MAIN TIMER (NO RESIZE INSIDE)
        # ==================================================
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.loop)
        self.timer.start(16)  # ~60 FPS

        self.show()

    # ==================================================
    # 🎨 PAINT EVENT (ALL ANIMATION HERE)
    # ==================================================
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        scale = 1.0 + math.sin(self.time) * 0.01
        scale = max(0.99, min(scale, 1.01))

        size = int(self.base_size * scale)
        x = (self.base_size - size) // 2
        y = (self.base_size - size) // 2

        painter.drawPixmap(
            x, y,
            size, size,
            self.current_pixmap
        )

    # ==================================================
    # MAIN LOOP (NO GEOMETRY CHANGES)
    # ==================================================
    def loop(self):
        self.time += 0.05
        self.update()  # repaint only

        # ---------- Roaming ----------
        if self.roaming and self.state == "IDLE":
            self.move(self.x() + self.direction, self.y())
            screen = self.screen().availableGeometry()
            if self.x() <= 0 or self.x() >= screen.width() - self.width():
                self.direction *= -1

        # ---------- Output bubble follow ----------
        if self.output_bubble.isVisible():
            out_pos = self.pos() + QPoint(
                self.base_size // 2 - self.output_bubble.width() // 2,
                -self.output_bubble.height() - 14
            )
            self.output_bubble.move(out_pos)

        # ---------- Input bubble follow ----------
        if self.input_bubble.isVisible():
            input_pos = self.pos() + QPoint(
                self.base_size + 10,
                self.base_size // 2 - self.input_bubble.height() // 2 - 30
            )
            self.input_bubble.move(input_pos)

    # ==================================================
    # 🔒 STATE CONTROL (EXTERNAL ONLY)
    # ==================================================
    def set_state(self, state: str):
        ALLOWED_STATES = {
            "IDLE",
            "WALK",
            "HOVER",
            "CLICK_REACT",
            "SLEEP"
        }

        if state not in ALLOWED_STATES:
            return

        if self.state == state:
            return

        self.state = state

        # Visual reaction ONLY
        if state == "SLEEP":
            self.current_pixmap = self.sleep_pixmap
        else:
            self.current_pixmap = self.awake_pixmap

        self.update()

    # ==================================================
    # CHAT / VOICE (DUMB)
    # ==================================================
    def on_text(self, text):
        if self.state == "SLEEP":
            return
        self.glow.setBlurRadius(18)
        self.output_bubble.show_typing()
        QTimer.singleShot(700, lambda: self.finish_response(text))

    def on_voice_text(self, text):
        if self.state == "SLEEP":
            return
        self.glow.setBlurRadius(18)
        self.output_bubble.show_typing()
        QTimer.singleShot(700, lambda: self.finish_response(text))

    def finish_response(self, text):
        self.glow.setBlurRadius(0)
        self.output_bubble.show_message(text, emotion="happy")

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
        if self.state == "SLEEP":
            return
        if self.input_bubble.isVisible():
            self.input_bubble.hide()
            self.output_bubble.hide()
        else:
            self.input_bubble.show()

    # ==================================================
    # KEYBOARD
    # ==================================================
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            self.roaming = not self.roaming
        elif event.key() == Qt.Key_S:
            self.set_state("SLEEP")
        elif event.key() == Qt.Key_W:
            self.set_state("IDLE")
