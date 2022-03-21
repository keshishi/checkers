class Checker:
    def __init__(self, x, y, c):
        self._king = False
        self.x = x
        self.y = y
        self.color = c

    def __str__(self):
        return self.color