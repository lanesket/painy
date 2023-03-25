class GitDiffException(Exception):
    def __init__(self, message: str = "Error. Are you in a git repository?"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message