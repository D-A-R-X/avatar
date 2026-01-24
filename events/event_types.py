"""
Event types enumeration for standardized event naming.
"""

from enum import Enum
# events/event_types.py

AVATAR_CLICK = "AVATAR_CLICK"
USER_TEXT_INPUT = "USER_TEXT_INPUT"
AI_RESPONSE = "AI_RESPONSE"
AI_STATE_UPDATE = "AI_STATE_UPDATE"


class EventType(str, Enum):
    """Standard event types used throughout the application."""
    
    # Agent lifecycle events
    AGENT_START = "agent_start"
    AGENT_STOP = "agent_stop"
    AGENT_PAUSE = "agent_pause"
    AGENT_RESUME = "agent_resume"
    
    # User interaction events
    USER_INPUT = "user_input"
    USER_COMMAND = "user_command"
    USER_FEEDBACK = "user_feedback"
    
    # Processing events
    TASK_START = "task_start"
    TASK_PROGRESS = "task_progress"
    TASK_COMPLETE = "task_complete"
    TASK_ERROR = "task_error"
    
    # Memory events
    MEMORY_UPDATE = "memory_update"
    MEMORY_RETRIEVE = "memory_retrieve"
    MEMORY_CLEAR = "memory_clear"
    
    # Emotion events
    EMOTION_CHANGE = "emotion_change"
    EMOTION_TRIGGERED = "emotion_triggered"
    
    # System events
    SYSTEM_ALERT = "system_alert"
    SYSTEM_WARNING = "system_warning"
    SYSTEM_ERROR = "system_error"
    
    # Safety events
    SAFETY_VIOLATION = "safety_violation"
    KILL_SWITCH_TRIGGERED = "kill_switch_triggered"
    
    # Intent events
    INTENT_DETECTED = "intent_detected"
    INTENT_CLASSIFIED = "intent_classified"
    
    # Response events
    RESPONSE_GENERATED = "response_generated"
    RESPONSE_SENT = "response_sent"
    
    # Custom events
    CUSTOM = "custom"


class EventPriority(str, Enum):
    """Priority levels for events."""
    
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class EventSource(str, Enum):
    """Sources of events."""
    
    USER = "user"
    SYSTEM = "system"
    AGENT = "agent"
    EXTERNAL = "external"
UI_SLEEP = "UI_SLEEP"
UI_WAKE = "UI_WAKE"
UI_ROAM_TOGGLE = "UI_ROAM_TOGGLE"
UI_CHAT_TOGGLE = "UI_CHAT_TOGGLE"
