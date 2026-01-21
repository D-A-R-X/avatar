"""
Character profile management for the AI agent's personality and traits.
"""


class CharacterProfile:
    """Manages the character profile and personality traits of the agent."""

    def __init__(self, name, traits=None):
        """Initialize the character profile.
        
        Args:
            name: Name of the character.
            traits: Dictionary of personality traits.
        """
        self.name = name
        self.traits = traits or {}

    def get_trait(self, trait_name):
        """Retrieve a specific trait value.
        
        Args:
            trait_name: The name of the trait.
            
        Returns:
            The trait value or None if not found.
        """
        return self.traits.get(trait_name)

    def set_trait(self, trait_name, value):
        """Set a trait value.
        
        Args:
            trait_name: The name of the trait.
            value: The value to set.
        """
        self.traits[trait_name] = value
