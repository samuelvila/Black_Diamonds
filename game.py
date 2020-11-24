import data
import var
from maps import map

from obj.player import *


def load():
    """
    Este metodo de clase cargara los sprites necesarios en memoria que se vayan a usar
    la instracia del juego. Este metodo deberia ser cambiado en el futuro
    :return:
    """
    data.avatar = pygame.image.load("res/spr/pSoldier.png")


class Game:
    """
    Clase principal del juego. Cuando se crea una instancia de la clase se crea un display de pygame. Contendra un 
    metodo llamado run() que lanzara el bucle principal del juego. 
    """

    # Constructor
    def __init__(self):
        var.CLK_TICKS = 60
        var.RES = (1600, 900)
        var.TILE_SIZE = 32

        pygame.init()
        self.display = pygame.display.set_mode(var.RES, 0, 32)  # Display por donde se muestra el frame
        self.frame = pygame.Surface((640, 360))                 # Frame donde se va a dibujar
        self.map = map.Map("tunisia_test")                      # Mapa
        self.true_scroll = [0, 0]                               # Scroll (con valores decimales)
        self.clock = pygame.time.Clock()                        # Reloj

    def scroll(self, player):
        """

        :param player:
        :return:
        """
        self.true_scroll[0] += (player.box.x - self.true_scroll[0] - 128) / 8
        self.true_scroll[1] += (player.box.y - self.true_scroll[1] - 200) / 8
        scroll = self.true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        return scroll

    def draw(self, player, obj_list, scroll):
        """
        Dibuja todos los objetos de la lista
        :param scroll:
        :param player:
        :param obj_list:
        :return:
        """
        self.map.render(self.frame, scroll)
        for obj in obj_list:
            obj.draw(self.frame, scroll)
        player.draw(self.frame, scroll)

    def update(self, player, obj_list):
        """
        Recorre toda la lista de objetos instanciados y los actualiza. Aqui se recorrera
        la lista de proyectiles y si algun proyectil esta entra en contacto con alguno de
        los objetos se llamara a la funcion 'take_damage'.
        :param player:
        :param obj_list:
        :return:
        """
        for obj in obj_list:
            obj.update(obj_list)
        player.update(self.map.tile_boxes)

    # Metodo que lanza el bucle principal del juego
    def run(self):
        """
        :return:
        """
        # Cargamos los sprites
        load()
        # Creamos las variables necesarias para la ejecucion
        obj_list = []
        player = Player(data.avatar, 100, 5, 6)
        while True:
            # Dibujamos un fondo de color
            self.frame.fill((80, 110, 230))
            # Aplicamos el scroll
            scroll = self.scroll(player)
            # Comprobamos el input del jugador
            player.check_user_input()
            # Actualizamos los objetos
            self.update(player, obj_list)
            # Dibujamos el frame
            self.draw(player, obj_list, scroll)
            """
            Escalamos el frame (donde estamos dibujado) y lo escalamos en una ventana 
            (display) mas grande. Esto nos permitira ademas cambiar con facilidad la 
            resolucion (mas bien escalado, ya que vamos a trabajar con pixel-art)
            """
            self.display.blit(pygame.transform.scale(self.frame, var.RES), (0, 0))
            # Actualizamos la pantalla
            pygame.display.update()
            # Limitamos el refresco de la pantalla
            self.clock.tick(var.CLK_TICKS)

# class Backround:
    # def __init__(self):
