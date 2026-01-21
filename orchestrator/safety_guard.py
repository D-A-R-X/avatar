"""
Safety guard for monitoring and preventing unsafe agent operations.
"""


class SafetyGuard:
    """Monitors and enforces safety constraints on agent operations."""

    def __init__(self):
        """Initialize the safety guard."""
        self.safety_rules = []

    def validate_action(self, action):
        """Validate that an action is safe to execute.
        
        Args:
            action: The action to validate.
            
        Returns:
            bool: True if action is safe, False otherwise.
        """
        pass

    def add_rule(self, rule):
        """Add a safety rule."""
        self.safety_rules.append(rule)
