class StateManager:
    def __init__(self):
        self.state = {
            "avatar": "IDLE",
            "emotion": "neutral",
            "busy": False
        }

    def get(self, key):
        return self.state.get(key)

    def set(self, key, value):
        self.state[key] = value

    def update(self, updates: dict):
        self.state.update(updates)

    def snapshot(self):
        return self.state.copy()
