"""
Session memory for tracking the current session context and state.
"""


class SessionMemory:
    """Manages memory specific to the current session."""

    def __init__(self, session_id):
        """Initialize session memory.
        
        Args:
            session_id: Unique identifier for the session.
        """
        self.session_id = session_id
        self.session_data = {}
        self.session_history = []

    def store_session_data(self, key, value):
        """Store data in session memory.
        
        Args:
            key: Data key.
            value: Data value.
        """
        self.session_data[key] = value

    def retrieve_session_data(self, key):
        """Retrieve data from session memory.
        
        Args:
            key: Data key to retrieve.
            
        Returns:
            Data value or None if not found.
        """
        return self.session_data.get(key)

    def add_to_history(self, event):
        """Add an event to session history.
        
        Args:
            event: Event to record.
        """
        self.session_history.append(event)

    def get_history(self):
        """Get the session history.
        
        Returns:
            List of session events.
        """
        return self.session_history

    def clear_session(self):
        """Clear all session memory."""
        self.session_data = {}
        self.session_history = []
