class Player:
    def __init__(self, name: str, score: int = 0):
        self.name = name.title()
        self.score = score