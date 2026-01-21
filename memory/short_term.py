"""
Short-term memory for storing recent interactions and context.
"""


class ShortTermMemory:
    """Manages short-term memory for recent interactions."""

    def __init__(self, capacity=100):
        """Initialize short-term memory.
        
        Args:
            capacity: Maximum number of items to store.
        """
        self.capacity = capacity
        self.memories = []

    def store(self, item):
        """Store an item in short-term memory.
        
        Args:
            item: The item to store.
        """
        self.memories.append(item)
        if len(self.memories) > self.capacity:
            self.memories.pop(0)

    def retrieve(self, count=10):
        """Retrieve the most recent items.
        
        Args:
            count: Number of items to retrieve.
            
        Returns:
            List of recent items.
        """
        return self.memories[-count:]

    def clear(self):
        """Clear all short-term memory."""
        self.memories = []

    def get_size(self):
        """Get current size of short-term memory.
        
        Returns:
            Number of items stored.
        """
        return len(self.memories)
