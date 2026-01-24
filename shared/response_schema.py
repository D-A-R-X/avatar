from dataclasses import dataclass
from typing import Literal

EmotionType = Literal["neutral", "happy", "sad", "angry"]
AvatarState = Literal["IDLE", "WALK", "HOVER", "SLEEP"]

@dataclass(frozen=True)
class AIChatResponse:
    text: str


@dataclass(frozen=True)
class AIStateUpdate:
    avatar_state: AvatarState
    emotion: EmotionType
