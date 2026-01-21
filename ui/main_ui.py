import sys
from PySide6.QtWidgets import QApplication
from ui.avatar.avatar_window import AvatarWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    avatar = AvatarWindow(
        image_path="ui/avatar/avatar_master.png"
    )
    avatar.show()

    sys.exit(app.exec())
