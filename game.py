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

    def drawObj(self, obj_list):
        """
        Dibuja todos los objetos de la lista
        :param obj_list:
        :return:
        """
        for obj in obj_list:
            obj.draw(self.frame)

    @staticmethod
    def updateObj(obj_list):
        """
        Recorre toda la lista de objetos instanciados y los actualiza. Aqui se recorrera
        la lista de proyectiles y si algun proyectil esta entra en contacto con alguno de
        los objetos se llamara a la funcion 'take_damage'.
        :param obj_list:
        :return:
        """
        for obj in obj_list:
            obj.update(obj_list)

    @staticmethod
    def checkInput(player_input):
        """

        :param player_input:
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_input[0] = True
                if event.key == pygame.K_d:
                    player_input[1] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player_input[0] = False
                if event.key == pygame.K_d:
                    player_input[1] = False
            # if event.type == pygame.K_SPACE:
            # if event.type == pygame.K_s:

    @staticmethod
    def applyInput(player, player_input):
        """
        :param player:
        :param player_input:
        :return:
        """
        if player_input[0]:
            player.accelerate(-1)
        if player_input[1]:
            player.accelerate(1)

    # Metodo que lanza el bucle principal del juego
    def run(self):
        """

        :return:
        """
        # Cargamos los sprites
        load()
        # Creamos las variables necesarias para la ejecucion
        obj_list = []
        player = Player(100, 50, 50, data.avatar, 10, 5)
        player_input = [False, False]   # Izquierda, derecha
        obj_list.append(player)
        while True:
            self.frame.fill((0, 0, 0))
            self.map.render(self.frame)
            self.drawObj(obj_list)
            self.checkInput(player_input)
            self.applyInput(player, player_input)
            self.updateObj(obj_list)
            self.display.blit(pygame.transform.scale(self.frame, var.RES), (0, 0))
            pygame.display.update()
            self.clock.tick(var.CLK_TICKS)

# class Backround:
    # def __init__(self):
