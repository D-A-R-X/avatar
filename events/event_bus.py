"""
Event bus for managing event publishing and subscription.
"""

from typing import Callable, List, Dict, Any


class EventBus:
    """Central event bus for publishing and subscribing to events."""

    def __init__(self):
        """Initialize the event bus."""
        self.subscribers: Dict[str, List[Callable]] = {}
        self.event_history = []

    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to an event type.
        
        Args:
            event_type: Type of event to subscribe to.
            callback: Callback function to execute when event is published.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: Callable):
        """Unsubscribe from an event type.
        
        Args:
            event_type: Type of event to unsubscribe from.
            callback: Callback function to remove.
        """
        if event_type in self.subscribers:
            self.subscribers[event_type] = [
                cb for cb in self.subscribers[event_type] if cb != callback
            ]

    def publish(self, event_type: str, data: Any = None):
        """Publish an event to all subscribers.
        
        Args:
            event_type: Type of event to publish.
            data: Optional data to include with the event.
        """
        event_record = {"type": event_type, "data": data}
        self.event_history.append(event_record)
        
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                try:
                    callback(data)
                except Exception as e:
                    print(f"Error in event callback: {e}")

    def get_subscribers(self, event_type: str) -> List[Callable]:
        """Get all subscribers for an event type.
        
        Args:
            event_type: Type of event.
            
        Returns:
            List of subscriber callbacks.
        """
        return self.subscribers.get(event_type, [])

    def get_event_history(self, event_type: str = None) -> list:
        """Get event history, optionally filtered by type.
        
        Args:
            event_type: Optional event type to filter by.
            
        Returns:
            List of event records.
        """
        if event_type:
            return [e for e in self.event_history if e["type"] == event_type]
        return self.event_history

    def clear_history(self):
        """Clear event history."""
        self.event_history = []
