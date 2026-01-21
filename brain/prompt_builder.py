"""
Prompt builder for constructing context-aware prompts for the AI model.
"""


class PromptBuilder:
    """Builds optimized prompts for AI model execution."""

    def __init__(self):
        """Initialize the prompt builder."""
        self.base_prompt = ""
        self.context = {}

    def set_base_prompt(self, prompt):
        """Set the base prompt template.
        
        Args:
            prompt: The base prompt template.
        """
        self.base_prompt = prompt

    def add_context(self, key, value):
        """Add context information to the prompt.
        
        Args:
            key: Context key.
            value: Context value.
        """
        self.context[key] = value

    def build(self):
        """Build the final prompt with all context.
        
        Returns:
            The constructed prompt string.
        """
        prompt = self.base_prompt
        for key, value in self.context.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        return prompt
