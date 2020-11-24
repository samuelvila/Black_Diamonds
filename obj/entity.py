import pygame


class Entity:
    """
    Clase que describe las entidades del juego. Esto son los todos los objetos: tienen una hitbox que representa el espacio
    fisico que ocupan y su posicion; y un sprite que representa que se va a imprimir por pantalla.
    """

    def __init__(self, x: int, y: int, sprite):
        self.sprite = sprite    # Sprite del objeto
        self.box = pygame.Rect(x, y, sprite.get_width(), sprite.get_height())

    def check_coll(self, box_list):
        """
        Metodo que retorna la lista de objetos cuyas hitboxs han colisionado con este
        :param box_list:
        :return:
        """
        boxes_hit = []
        for box in box_list:
            if self.box.colliderect(box):
                boxes_hit.append(box)
        return boxes_hit

    def draw(self, frame, scroll):
        """
        Dibuja en el frame el sprite de la entidad sobre el origen de su hitbox
        :param frame:
        :param scroll:
        :return:
        """
        frame.blit(self.sprite, (self.box.x + scroll[0], self.box.y + scroll[1]))

    def update(self, box_list):
        """
        Metodo que actualiza la entidad - Ahora mismo 'abstracto'
        :param box_list:
        :return:
        """
        pass
