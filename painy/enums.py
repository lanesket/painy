from enum import Enum


class ChatRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"