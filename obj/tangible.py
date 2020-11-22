import pygame
import var


class Tangible:
    """
    Clase que describe ojetos fisicos dentro del juego. Contiene la posicion del objeto, y su caja de colisiones.
    Contiene la imagen que lo representa en el display.
    """

    grav = 0.2  # Gravedad constante que empujara a todos los objetos tangibles hacia abajo

    def __init__(self, x, y, sprite):
        self.vec = [0, 0]       # Vector de movimiento del objeto
        self.mom_x = 0          # Momento horizontal
        self.mom_y = 0          # Momento vertical
        self.sprite = sprite    # Sprite del objeto
        self.box = pygame.Rect(x, y, sprite.get_width(), sprite.get_height())

    def fall(self):
        if self.vec[1] < 5:
            self.vec[1] += Tangible.grav

    def check_coll(self, box_list):
        boxes_hit = []
        for box in box_list:
            if self.box.colliderect(box):
                boxes_hit.append(box)
        return boxes_hit

    def draw(self, screen, scroll):
        # Dibujamos el sprite del jugador donde este su caja de colisiones
        screen.blit(self.sprite, (self.box.x + scroll[0], self.box.y + scroll[1]))

    def update(self, box_list):
        pass

