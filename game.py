import sys
import data
import map
from obj.player import *


def load():
    """
    Este metodo de clase cargara los sprites necesarios en memoria que se vayan a usar
    la instracia del juego. Este metodo deberia ser cambiado en el futuro
    :return:
    """
    data.avatar = pygame.image.load("res/img/pSoldier.png")


class Game:
    var.CLK_TICKS = 60
    var.RES = (1280, 720)
    var.TILE_SIZE = 32
    """
    Clase principal del juego. Cuando se crea una instancia de la clase se crea un display de pygame. Contendra un 
    metodo llamado run() que lanzara el bucle principal del juego. 
    """

    # Constructor
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(var.RES, 0, 32)
        self.frame = pygame.Surface((640, 360))
        self.map = map.Map()
        self.clock = pygame.time.Clock()

    def drawObj(self, player, obj_list):
        """
        Dibuja todos los objetos de la lista
        :param player:
        :param obj_list:
        :return:
        """
        player.draw(self.frame)
        for obj in obj_list:
            obj.draw(self.frame)

    @staticmethod
    def updateObj(player, obj_list, g_map):
        """
        Recorre toda la lista de objetos instanciados y los actualiza. Aqui se recorrera
        la lista de proyectiles y si algun proyectil esta entra en contacto con alguno de
        los objetos se llamara a la funcion 'take_damage'.
        :param g_map:
        :param player:
        :param obj_list:
        :return:
        """
        player.update(g_map.tile_hit)
        for obj in obj_list:
            obj.update(obj_list)

    # Metodo que lanza el bucle principal del juego
    def run(self):
        """
        :return:
        """
        # Cargamos los sprites
        load()
        # Creamos las variables necesarias para la ejecucion
        obj_list = []
        player = Player(100, 50, 50, data.avatar, 5, 6)
        while True:
            # Dibujamos en el frame el mapa y un fondo de color
            self.frame.fill((100, 120, 210))
            self.map.render(self.frame)
            # Dibujamos los objetos
            self.drawObj(player, obj_list)
            # Comprobamos el input del jugador
            player.checkInput()
            # Actualizamos los objetos
            self.updateObj(player, obj_list, self.map)
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
