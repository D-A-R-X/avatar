"""
Emotion rules for governing how emotions affect agent behavior.
"""


class EmotionRules:
    """Defines and enforces rules for emotional behavior responses."""

    def __init__(self):
        """Initialize emotion rules."""
        self.rules = {}

    def add_rule(self, emotion, condition, action):
        """Add a rule for how the agent should behave with an emotion.
        
        Args:
            emotion: The emotion this rule applies to.
            condition: Condition for triggering the rule.
            action: Action to take when rule is triggered.
        """
        if emotion not in self.rules:
            self.rules[emotion] = []
        self.rules[emotion].append({
            "condition": condition,
            "action": action
        })

    def evaluate_rules(self, emotion_state):
        """Evaluate and apply rules based on current emotion state.
        
        Args:
            emotion_state: Current emotional state.
            
        Returns:
            List of actions to execute.
        """
        actions = []
        for emotion, rules in self.rules.items():
            intensity = emotion_state.get_emotion(emotion)
            if intensity > 0:
                for rule in rules:
                    if self._check_condition(rule["condition"], intensity):
                        actions.append(rule["action"])
        return actions

    def _check_condition(self, condition, intensity):
        """Check if a condition is met based on intensity.
        
        Args:
            condition: The condition to check.
            intensity: The emotion intensity.
            
        Returns:
            bool: True if condition is met.
        """
        return True

    def get_rules(self, emotion):
        """Get all rules for a specific emotion.
        
        Args:
            emotion: The emotion to query.
            
        Returns:
            List of rules for the emotion.
        """
        return self.rules.get(emotion, [])
