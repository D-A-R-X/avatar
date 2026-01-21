"""
Event models for structuring event data.
"""

from dataclasses import dataclass, field
from typing import Any, Optional, Dict
from datetime import datetime


@dataclass
class Event:
    """Base event model."""
    
    event_type: str
    source: str
    timestamp: datetime = field(default_factory=datetime.now)
    data: Optional[Dict[str, Any]] = None
    priority: str = "normal"
    id: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary.
        
        Returns:
            Dictionary representation of the event.
        """
        return {
            "event_type": self.event_type,
            "source": self.source,
            "timestamp": self.timestamp.isoformat(),
            "data": self.data or {},
            "priority": self.priority,
            "id": self.id
        }


@dataclass
class TaskEvent(Event):
    """Event related to task execution."""
    
    task_id: str = ""
    task_name: str = ""
    status: str = ""
    progress: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task event to dictionary.
        
        Returns:
            Dictionary representation of the event.
        """
        base_dict = super().to_dict()
        base_dict.update({
            "task_id": self.task_id,
            "task_name": self.task_name,
            "status": self.status,
            "progress": self.progress
        })
        return base_dict


@dataclass
class ErrorEvent(Event):
    """Event representing an error."""
    
    error_code: str = ""
    error_message: str = ""
    stack_trace: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert error event to dictionary.
        
        Returns:
            Dictionary representation of the event.
        """
        base_dict = super().to_dict()
        base_dict.update({
            "error_code": self.error_code,
            "error_message": self.error_message,
            "stack_trace": self.stack_trace
        })
        return base_dict


@dataclass
class UserInputEvent(Event):
    """Event representing user input."""
    
    user_id: Optional[str] = None
    input_text: str = ""
    input_type: str = "text"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user input event to dictionary.
        
        Returns:
            Dictionary representation of the event.
        """
        base_dict = super().to_dict()
        base_dict.update({
            "user_id": self.user_id,
            "input_text": self.input_text,
            "input_type": self.input_type
        })
        return base_dict


@dataclass
class EmotionEvent(Event):
    """Event related to emotion changes."""
    
    emotion: str = ""
    intensity: float = 0.0
    trigger: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert emotion event to dictionary.
        
        Returns:
            Dictionary representation of the event.
        """
        base_dict = super().to_dict()
        base_dict.update({
            "emotion": self.emotion,
            "intensity": self.intensity,
            "trigger": self.trigger
        })
        return base_dict


@dataclass
class SystemAlertEvent(Event):
    """Event for system alerts and monitoring."""
    
    alert_type: str = ""
    severity: str = "normal"
    component: str = ""
    metric_name: Optional[str] = None
    metric_value: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert system alert event to dictionary.
        
        Returns:
            Dictionary representation of the event.
        """
        base_dict = super().to_dict()
        base_dict.update({
            "alert_type": self.alert_type,
            "severity": self.severity,
            "component": self.component,
            "metric_name": self.metric_name,
            "metric_value": self.metric_value
        })
        return base_dict
