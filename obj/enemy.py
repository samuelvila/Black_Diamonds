class Enemy:
    def __init__(self, hp):
        self.hp = hp

    def take_damage(self, dam):
        self.hp -= dam

class Infantry(Enemy):
    def __init__(self, hp):
        super().__init__(hp)