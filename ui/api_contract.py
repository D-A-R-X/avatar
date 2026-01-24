from dataclasses import dataclass
from typing import Optional, Literal

# -------- UI -> AI --------
UIEventType = Literal[
    "AVATAR_CLICK",
    "AVATAR_HOVER",
    "USER_INPUT",
    "SLEEP",
    "WAKE",
    "CHAT_TOGGLE"
]

@dataclass(frozen=True)
class UIEvent:
    type: UIEventType
    data: Optional[dict] = None


# -------- AI -> UI --------
AvatarState = Literal["IDLE", "WALK", "HOVER", "SLEEP"]
EmotionType = Literal["neutral", "happy", "sad", "angry"]

@dataclass(frozen=True)
class AIStateUpdate:
    avatar_state: AvatarState
    emotion: EmotionType


@dataclass(frozen=True)
class AIChatResponse:
    text: str
