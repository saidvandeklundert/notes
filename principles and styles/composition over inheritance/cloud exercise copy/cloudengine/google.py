class GoogleAuth:
    def __init__(self, key: str) -> None:
        self.key = key

    def auth(self):
        return self.key
