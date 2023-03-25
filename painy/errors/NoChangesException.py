class NoChangesException(Exception):
    def __init__(self, message: str = "No changes found."):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message