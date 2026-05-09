"""Player class with property-based lives and level management; score adjusts with level changes."""


class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
        self.control = 1

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level <= 0:
            print('Level cannot be 0')
            level = 1
            pass

        if level > self.control:
            self._score = ((level * 1000) - 1000)
        elif level < self.control:
            self.control -= level
            self._score -= (self.control * 1000)

        self._level = level
        self.control = level

    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self._score}"
