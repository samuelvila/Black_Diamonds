from obj.tangible import *


class Proyectile(Tangible):
    """
    """

    def __init__(self, x, y, sprite, vector, spd, dam):
        super().__init__(x, y, sprite)
        self.vector = vector
        self.spd = spd
        self.dam = dam

    def get_dam(self):
        return self.dam

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def update(self):
        self.x += self.spd * self.vector[0]
        self.y += self.spd * self.vector[1]
