from enum import Enum


class ChatRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"
    
class Action(Enum):
    COMMENT = "comment"
    COMMIT = "commit"