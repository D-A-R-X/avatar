import sys
from PySide6.QtWidgets import QApplication
from avatar.avatar_window import AvatarWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    avatar = AvatarWindow()
    sys.exit(app.exec())