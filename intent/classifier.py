"""
Intent classifier for determining user intent from input.
"""


class IntentClassifier:
    """Classifies user input to determine their intent."""

    def __init__(self):
        """Initialize the intent classifier."""
        self.intents = {}

    def classify(self, input_text):
        """Classify the intent of the user input.
        
        Args:
            input_text: The user input text to classify.
            
        Returns:
            The classified intent with confidence score.
        """
        pass

    def add_intent(self, intent_name, patterns):
        """Add an intent with associated patterns.
        
        Args:
            intent_name: Name of the intent.
            patterns: List of patterns that match this intent.
        """
        self.intents[intent_name] = patterns
