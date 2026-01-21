"""
Intent router for directing requests to appropriate handlers based on intent.
"""


class IntentRouter:
    """Routes requests to appropriate handlers based on classified intent."""

    def __init__(self):
        """Initialize the intent router."""
        self.handlers = {}

    def register_handler(self, intent_name, handler):
        """Register a handler for a specific intent.
        
        Args:
            intent_name: Name of the intent.
            handler: Callable handler for this intent.
        """
        self.handlers[intent_name] = handler

    def route(self, intent_name, data):
        """Route a request to the appropriate handler based on intent.
        
        Args:
            intent_name: The classified intent.
            data: Data to pass to the handler.
            
        Returns:
            Result from the handler.
        """
        handler = self.handlers.get(intent_name)
        if handler:
            return handler(data)
        return None

    def has_handler(self, intent_name):
        """Check if a handler exists for the given intent.
        
        Args:
            intent_name: Name of the intent.
            
        Returns:
            bool: True if handler exists, False otherwise.
        """
        return intent_name in self.handlers
