"""
State manager for tracking and managing agent state throughout execution.
"""


class StateManager:
    """Manages the state of the AI agent during operation."""

    def __init__(self):
        """Initialize the state manager."""
        self.state = {}

    def update_state(self, key, value):
        """Update a state value."""
        self.state[key] = value

    def get_state(self, key):
        """Retrieve a state value."""
        return self.state.get(key)
