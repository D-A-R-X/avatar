from dataclasses import dataclass
from typing import Optional, Literal

# -------- UI -> AI --------
UIEventType = Literal["CLICK", "HOVER", "INPUT", "SLEEP", "WAKE"]

@dataclass(frozen=True)
class UIEvent:
    type: UIEventType
    data: Optional[dict] = None


# -------- AI -> UI --------
AvatarState = Literal["IDLE", "WALK", "HOVER", "SLEEP"]
EmotionType = Literal["neutral", "happy", "sad", "angry"]

@dataclass(frozen=True)
class AIState:
    avatar_state: AvatarState
    response_text: str
    emotion: EmotionType
