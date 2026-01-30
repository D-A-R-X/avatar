from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPainterPath

from ui.bubble.emotion_style import EMOTION_STYLE


# ==================================================
# MUST MATCH InputBubble EXACTLY
# ==================================================
INPUT_BUBBLE_WIDTH = 260
INPUT_BUBBLE_HEIGHT = 44


# ==================================================
# 💗 Mini Heart Tail
# ==================================================
class HeartTail(QWidget):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.setFixedSize(10, 10)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(self.color))
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.moveTo(5, 9)
        path.cubicTo(1, 6, 1, 2, 5, 3)
        path.cubicTo(9, 2, 9, 6, 5, 9)
        painter.drawPath(path)


# ==================================================
# 💬 Output Bubble (FINAL / CLEAN)
# ==================================================
class OutputBubble(QWidget):
    def __init__(self):
        super().__init__()

        # Window flags
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Cache size (Win11 safe)
        self._last_size = None

        # ---------------- Body (REAL bubble) ----------------
        self.body = QWidget(self)

        # ---------------- Label ----------------
        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout = QVBoxLayout(self.body)
        layout.setContentsMargins(14, 10, 14, 10)  # ONLY padding source
        layout.addWidget(self.label)

        # ---------------- Tail ----------------
        self.tail = HeartTail("#ffffff")
        self.tail.setParent(self)
        self.tail.raise_()

        # ---------------- Auto-hide ----------------
        self.hide_timer = QTimer(self)
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.hide)

        self.hide()

    # ==================================================
    # Show Message (SINGLE SIZE CONTROL)
    # ==================================================
    def show_message(self, text, emotion="neutral"):
        style = EMOTION_STYLE.get(emotion, EMOTION_STYLE["neutral"])

        bg = style["bg_color"]
        fg = style["text_color"]

        # Style ONLY the body (never the parent)
        self.body.setStyleSheet(f"""
            QWidget {{
                background-color: {bg};
                color: {fg};
                border-radius: 16px;
            }}
        """)

        self.label.setStyleSheet(f"color: {fg};")
        self.label.setText(text)
        self.show()

        # Measure natural content height
        self.body.adjustSize()
        natural_h = self.body.height()

        # Minimum height match input bubble
        final_h = max(natural_h, INPUT_BUBBLE_HEIGHT)

        # Resize ONLY the outer widget
        new_size = (INPUT_BUBBLE_WIDTH, final_h + 14)
        if self._last_size != new_size:
            self.resize(*new_size)
            self._last_size = new_size

        # Position tail
        self.tail.color = bg
        self.tail.move(16, final_h + 4)
        self.tail.update()

        # Auto hide after delay
        self.hide_timer.start(6000)
