from api_contract import UIEvent, AIState


class DummyAI:
    def handle_event(self, event: UIEvent) -> AIState:
        """
        Very dumb AI.
        Just reacts based on event type.
        """

        if event.type == "CLICK":
            return AIState(
                avatar_state="HOVER",
                response_text="You clicked me 👀",
                emotion="happy"
            )

        if event.type == "INPUT":
            text = event.data.get("text", "")
            return AIState(
                avatar_state="IDLE",
                response_text=f"You said: {text}",
                emotion="neutral"
            )

        if event.type == "SLEEP":
            return AIState(
                avatar_state="SLEEP",
                response_text="Going to sleep 😴",
                emotion="neutral"
            )

        if event.type == "WAKE":
            return AIState(
                avatar_state="IDLE",
                response_text="I'm awake ☀️",
                emotion="happy"
            )

        # fallback (must exist)
        return AIState(
            avatar_state="IDLE",
            response_text="...",
            emotion="neutral"
        )
