from .git import *
from .enums import *
import openai
import os


MODEL_NAME = os.getenv(key="OPENAI_MODEL_NAME", default="gpt-3.5-turbo")
MAX_LENGTH = int(os.getenv(key="OPENAI_MODEL_INPUT_LENGTH", default=4097))
MAX_MESSAGES = 40


class ChatHistory:
    def __init__(self, limit: int = MAX_MESSAGES):
        self.history = []
        self.limit = limit
    
    def add(self, message: str, role: ChatRole):
        self.history.append({"content": message, "role": role.value})

    def get(self) -> list:
        return self.history[-self.limit:]

    def clear(self):
        self.history = []


class Model:
    def __init__(self, purpose_prompt: str, model_name: str = MODEL_NAME):
        self.model_name = model_name
        self.purpose_prompt = purpose_prompt
        self.history = ChatHistory()
        
        self.history.add(self.purpose_prompt, ChatRole.SYSTEM)
        
    def get_response(self, prompt: str) -> str:
        prompt = prompt[:MAX_LENGTH]
        self.history.add(prompt, ChatRole.USER)
        
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=self.history.get(),
        )
        
        response = response["choices"][0]["message"]["content"]
        
        return response