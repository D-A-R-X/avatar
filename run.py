import sys
from PySide6.QtWidgets import QApplication

from events.event_bus import EventBus
from orchestrator.controller import Orchestrator
from orchestrator.state_manager import StateManager
from ui.main_ui import MainUI


def main():
    print("Desktop AI Agent starting...")

    app = QApplication(sys.argv)

    # ✅ ONE shared bus
    bus = EventBus()

    # ✅ Backend
    state = StateManager()
    orchestrator = Orchestrator(bus, state)

    # ✅ UI
    ui = MainUI(bus)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
