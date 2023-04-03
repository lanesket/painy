class NoSettingException(Exception):
    def __init__(self, message: str = "No setting found."):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message