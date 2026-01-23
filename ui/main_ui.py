import os
import sys
from PySide6.QtWidgets import QApplication
from avatar.avatar_window import AvatarWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    avatar = AvatarWindow()
    sys.exit(app.exec())

if os.environ.get("CODESPACES") == "true":
    print("UI disabled in Codespaces")
    exit(0)