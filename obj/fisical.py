from obj.dinamic import Dinamic


class Fisical(Dinamic):
    """
    Clase que define las entidades afectadas por gravedad. Son ademas entidades que puedan sufrir
    daños.
    """
    # Gravedad constante que empujara a todos los objetos tangibles hacia abajo
    grav = 0.2

    def __init__(self, x: int, y: int, sprite, hp: int):
        super().__init__(x, y, sprite)
        self.hp = hp  # Puntos de vida de la entidad

    def fall(self):
        if self.mov[1] < 5:
            self.mov[1] += Fisical.grav
