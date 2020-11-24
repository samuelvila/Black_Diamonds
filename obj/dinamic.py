from obj.entity import Entity


class Dinamic(Entity):
    """
    Entidades que pueden desplazarse. Tendran vectores de movimiento y momento
    """

    def __init__(self, x: int, y: int, sprite):
        super().__init__(x, y, sprite)
        self.mov = [0, 0]  # Vector de movimiento de la entidad
        self.mom = [0, 0]  # Vector de momento de la entidad

