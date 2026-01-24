## AI_RESPONSE Event

Emitted by backend when a reply is generated.

Payload:
{
  text: string,
  emotion: "happy" | "neutral" | "sad" | "angry",
  avatar_state: "IDLE" | "CLICK" | "HOVER"
}

Rules:
- UI must not modify payload
- UI must only render based on these fields
- Backend is the single authority
