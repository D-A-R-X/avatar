# brain/responder.py

class Responder:
    def generate_reply(self, text: str) -> dict:
        text = text.lower().strip()

        if "hello" in text or "hi" in text:
            return {
                "text": "Hi 👋",
                "emotion": "happy",
                "avatar_state": "IDLE"
            }

        if "how are you" in text:
            return {
                "text": "I'm doing fine 🙂",
                "emotion": "happy",
                "avatar_state": "IDLE"
            }

        if "bye" in text:
            return {
                "text": "Bye! See you soon 👋",
                "emotion": "neutral",
                "avatar_state": "IDLE"
            }

        return {
            "text": "Tell me more.",
            "emotion": "neutral",
            "avatar_state": "IDLE"
        }
