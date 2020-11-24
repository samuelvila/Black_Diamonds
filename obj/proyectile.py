from obj.dinamic import Dinamic


class Proyectile(Dinamic):
    """
    """

    def __init__(self, x: int, y: int, sprite, vector: [int, int], spd: float, dam: int):
        super().__init__(x, y, sprite)
        self.vector = vector
        self.spd = spd
        self.dam = dam

    def get_dam(self):
        return self.dam

    def move(self):
        self.box.x += self.spd * self.vector[0]
        self.box.y += self.spd * self.vector[1]

    def update(self, box_list):
        self.move()


