from events.event_bus import EventBus
from events.event_types import (
    AVATAR_CLICK,
    USER_TEXT_INPUT,
    AI_RESPONSE,
    AI_STATE_UPDATE
)
from orchestrator.controller import Orchestrator
from orchestrator.state_manager import StateManager


def log_response(data):
    print("[AI RESPONSE]", data)


def log_state(update):
    print("[AI STATE]", update)


def main():
    print("Desktop AI Agent starting...")

    bus = EventBus()
    state = StateManager()
    orchestrator = Orchestrator(bus, state)

    # ✅ SUBSCRIPTIONS MUST BE INSIDE main()
    bus.subscribe(AI_RESPONSE, log_response)
    bus.subscribe(AI_STATE_UPDATE, log_state)

    # 🔥 test events
    bus.publish(AVATAR_CLICK)
    bus.publish(USER_TEXT_INPUT, "hello")
    bus.publish("SLEEP")
    bus.publish("WAKE")
    bus.publish("ROAM_TOGGLE")


if __name__ == "__main__":
    main()
