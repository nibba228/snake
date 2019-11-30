class GameStats:
    """Статистика игры"""

    def __init__(self):
        self.score = 0
        self.max_score = 0
        self.load_max_score()

    def add_score(self):
        self.score += 10

    def update_max_score(self):
        if self.score > self.max_score:
            with open('max_score.txt', 'w') as f:
                f.write(str(self.score))

    def load_max_score(self):
        with open('max_score.txt') as f:
            self.max_score = int(f.read())
