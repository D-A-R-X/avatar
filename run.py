from events.event_bus import EventBus
from events.event_types import AVATAR_CLICK, USER_TEXT_INPUT, AI_RESPONSE
from orchestrator.controller import Orchestrator
from orchestrator.state_manager import StateManager

def log_response(data):
    print("[AI RESPONSE]", data)

def main():
    print("Desktop AI Agent starting...")

    bus = EventBus()
    state = StateManager()
    orchestrator = Orchestrator(bus, state)

    bus.subscribe(AI_RESPONSE, log_response)

    bus.publish(AVATAR_CLICK)
    bus.publish(USER_TEXT_INPUT, "hello")

if __name__ == "__main__":
    main()
