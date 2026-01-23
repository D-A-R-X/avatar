from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPainterPath

# ==================================================
# MUST MATCH InputBubble EXACTLY
# ==================================================
INPUT_BUBBLE_WIDTH = 260
INPUT_BUBBLE_HEIGHT = 44

AVATAR_COLORS = {
    "neutral": ("#ffe6f2", "#f0e9ff"),
    "happy":   ("#ffd6eb", "#f6eaff"),
    "sad":     ("#e6f0ff", "#eef3ff"),
    "angry":   ("#ffe6e6", "#ffdada"),
}


# ==================================================
# 💗 Mini Heart Tail (SAME AS INPUT)
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
# 💬 Output Bubble (Windows 11 SAFE)
# ==================================================
class OutputBubble(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 🔒 Cache size (prevents Win11 resize spam)
        self._last_size = None

        # ---------------- Body ----------------
        self.body = QWidget(self)

        # ---------------- Label ----------------
        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.label.setStyleSheet("color:#444;")

        layout = QVBoxLayout(self.body)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.addWidget(self.label)

        # ---------------- Heart Tail ----------------
        self.tail = HeartTail(AVATAR_COLORS["neutral"][0])
        self.tail.setParent(self)
        self.tail.raise_()

        # ---------------- Auto-hide ----------------
        self.hide_timer = QTimer(self)
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.hide)

        self.hide()

    # ==================================================
    # Typing
    # ==================================================
    def show_typing(self):
        self.show_message("...", "neutral")

    # ==================================================
    # Show Message (NO BREATHING, NO RESIZE LOOP)
    # ==================================================
    def show_message(self, text, emotion="neutral"):
        self.hide_timer.stop()

        c1, c2 = AVATAR_COLORS.get(emotion, AVATAR_COLORS["neutral"])

        # 🔑 MUST be visible before resize (Win11 rule)
        if not self.isVisible():
            self.show()

        # 🔒 HARD LOCK WIDTH (same as input)
        self.body.setFixedWidth(INPUT_BUBBLE_WIDTH)
        self.label.setFixedWidth(INPUT_BUBBLE_WIDTH - 28)

        # Set text
        self.label.setText(text)

        # Measure natural height
        self.body.adjustSize()
        natural_h = self.body.height()

        # 🔒 Small text = same height as input
        final_h = max(natural_h, INPUT_BUBBLE_HEIGHT)
        self.body.setFixedHeight(final_h)

        # Rounded bubble (safe)
        self.body.setStyleSheet(f"""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0,
                stop:0 {c1},
                stop:1 {c2}
            );
            border-radius:{final_h // 2}px;
        """)

        # 🔒 SAFE resize (ONLY if size changed)
        new_size = (INPUT_BUBBLE_WIDTH, final_h + 14)
        if self._last_size != new_size:
            self.resize(*new_size)
            self._last_size = new_size

        # Heart tail (same as input)
        self.tail.color = c1
        self.tail.move(
            16,
            final_h + 4
        )

        # Auto hide
        self.hide_timer.start(6000)
