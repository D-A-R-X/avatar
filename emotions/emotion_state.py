"""
Emotion state tracking for the AI agent's current emotional state.
"""


class EmotionState:
    """Tracks and manages the current emotional state of the agent."""

    def __init__(self):
        """Initialize the emotion state."""
        self.current_emotions = {}
        self.emotion_history = []

    def set_emotion(self, emotion_name, intensity):
        """Set or update an emotion intensity.
        
        Args:
            emotion_name: Name of the emotion.
            intensity: Intensity value from 0 to 1.
        """
        self.current_emotions[emotion_name] = intensity
        self.emotion_history.append({
            "emotion": emotion_name,
            "intensity": intensity
        })

    def get_emotion(self, emotion_name):
        """Get the current intensity of an emotion.
        
        Args:
            emotion_name: Name of the emotion.
            
        Returns:
            Current intensity value or 0 if emotion not present.
        """
        return self.current_emotions.get(emotion_name, 0.0)

    def get_dominant_emotion(self):
        """Get the emotion with the highest intensity.
        
        Returns:
            Tuple of (emotion_name, intensity) or (None, 0).
        """
        if not self.current_emotions:
            return None, 0
        return max(self.current_emotions.items(), key=lambda x: x[1])

    def reset_emotions(self):
        """Reset all emotions to neutral state."""
        self.current_emotions = {}
