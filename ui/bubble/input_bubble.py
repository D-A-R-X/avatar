from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QColor, QPainterPath

AVATAR_COLORS = ("#ffe6f2", "#f0e9ff")


# ==================================================
# 💗 Mini Heart Tail Widget
# ==================================================
class HeartTail(QWidget):
    def __init__(self, color):
        super().__init__()

        # 🔧 FIX: mini heart size (square for clean drawing)
        self.setFixedSize(10, 10)

        self.color = color

        # 🔧 FIX: transparent + ignore mouse
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor(self.color))
        painter.setPen(Qt.NoPen)

        # 🔧 FIX: centered heart path
        path = QPainterPath()
        path.moveTo(5, 9)
        path.cubicTo(1, 6, 1, 2, 5, 3)
        path.cubicTo(9, 2, 9, 6, 5, 9)

        painter.drawPath(path)


# ==================================================
# 💬 Input Bubble
# ==================================================
class InputBubble(QWidget):
    text_submitted = Signal(str)
    mic_toggled = Signal(bool)

    def __init__(self):
        super().__init__()
        self.mic_on = False

        # ---------------- Window ----------------
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        c1, c2 = AVATAR_COLORS

        # ---------------- Body ----------------
        self.body = QWidget(self)
        
        # ---------------- Input ----------------
        self.input = QLineEdit(self.body)
        self.input.setPlaceholderText("thinking…")
        self.input.setStyleSheet(
            "border:none; background:transparent; color:#444;"
        )

        btn_style = """
            QPushButton {
                background: transparent;
                border: none;
                font-size: 16px;
            }
        """

        self.mic_btn = QPushButton("🎤", self.body)
        self.send_btn = QPushButton("💗", self.body)
        self.mic_btn.setStyleSheet(btn_style)
        self.send_btn.setStyleSheet(btn_style)

        self.mic_btn.clicked.connect(self.toggle_mic)
        self.send_btn.clicked.connect(self.send_text)
        self.input.returnPressed.connect(self.send_text)

        layout = QHBoxLayout(self.body)
        layout.setContentsMargins(10, 6, 10, 6)
        layout.addWidget(self.input)
        layout.addWidget(self.mic_btn)
        layout.addWidget(self.send_btn)

        # ---------------- Heart Tail ----------------
        # 🔧 FIX: mini floating heart tail
        self.tail = HeartTail(c1)
        self.tail.setParent(self)
        self.tail.raise_()

        self.setMinimumHeight(44)
        self.setMaximumWidth(360)

        self.update_size()

    # ---------------- Resize logic ----------------
    def update_size(self):
        self.tail.hide()
        self.body.adjustSize()

        body_h = self.body.height()

        # 🔧 FIX: force pill radius dynamically (Windows 11 safe)
        self.body.setStyleSheet(f"""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0,
                stop:0 {AVATAR_COLORS[0]},
                stop:1 {AVATAR_COLORS[1]}
            );
            border-radius:{body_h // 2}px;
        """)

        # 🔧 FIX: resize including heart space
        self.resize(
            self.body.width(),
            self.body.height() + 14
        )

        # 🔧 FIX: floating heart below bubble
        self.tail.move(
            16,
            self.body.height() + 4
        )

        self.tail.show()

    # ---------------- Actions ----------------
    def send_text(self):
        text = self.input.text().strip()
        if text:
            self.text_submitted.emit(text)
            self.input.clear()
            self.update_size()

    def toggle_mic(self):
        self.mic_on = not self.mic_on
        self.mic_btn.setText("🎀🎤" if self.mic_on else "🎤")
        self.mic_toggled.emit(self.mic_on)
