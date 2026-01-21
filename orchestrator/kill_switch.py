"""
Kill switch for emergency termination of agent operations.
"""


class KillSwitch:
    """Provides emergency termination capabilities for the agent."""

    def __init__(self):
        """Initialize the kill switch."""
        self.is_active = False

    def activate(self):
        """Activate the kill switch to stop all operations."""
        self.is_active = True

    def deactivate(self):
        """Deactivate the kill switch to resume operations."""
        self.is_active = False

    def is_triggered(self):
        """Check if the kill switch is currently active.
        
        Returns:
            bool: True if kill switch is active, False otherwise.
        """
        return self.is_active
