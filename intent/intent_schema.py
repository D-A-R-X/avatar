"""
Intent schema definitions for standardizing intent structure.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class IntentSchema:
    """Schema for defining intent structure and validation."""
    
    name: str
    description: str
    parameters: Optional[Dict[str, Any]] = None
    confidence_threshold: float = 0.7
    
    def validate(self, data: Dict[str, Any]) -> bool:
        """Validate data against the intent schema.
        
        Args:
            data: Data to validate.
            
        Returns:
            bool: True if data is valid, False otherwise.
        """
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert schema to dictionary representation.
        
        Returns:
            Dictionary representation of the schema.
        """
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters or {},
            "confidence_threshold": self.confidence_threshold
        }
