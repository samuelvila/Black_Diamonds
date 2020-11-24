import sys
import pygame
from obj.fisical import Fisical


class Player(Fisical):
    """
    Clase del avatar que controla el jugador. Aviso para navegantes: se va a usar POO como base de
    de todas las clases instanciables que hagamos.

    Constantes de la clase jugador:"""
    inertia = 10
    HITBOX_SIZE = [32, 64]

    # Constructor
    def __init__(self, sprite, hp: int, spd: int, j_spd: int):
        # Lo creamos con la anchura de la hitbox de finida
        super().__init__(self.HITBOX_SIZE[0], self.HITBOX_SIZE[1], sprite, hp)
        self.spd = spd  # Velocidad del avatar al moverse
        self.j_spd = j_spd  # Velocidad del avatar al saltar
        self.air_time = 0  # Tiempo (en frames) que el jugador estuvo en el aire
        self.sht_halt = 0  # Tiempo (en frames) durante el que el jugador no podra disparar
        # Array de los posibles estados
        self.states = {"IDLE": False, "RUNNING_RIGHT": False, "RUNNING_LEFT": False,
                       "SHOOTING": False, "JUMPING": False, "AIR_TIME": False, "LANDING": False}

    def check_user_input(self):
        """
        :param player_input:
        :return:
        """
        # Comprobamos que input nos esta dando el jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.states["RUNNING_RIGHT"] = True
                if event.key == pygame.K_d:
                    self.states["RUNNING_LEFT"] = True
                if event.key == pygame.K_SPACE:
                    if self.air_time < 6:
                        self.mom[1] = -self.j_spd
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.states["RUNNING_RIGHT"] = False
                if event.key == pygame.K_d:
                    self.states["RUNNING_LEFT"] = False

    def move(self, box_list):
        """
        (COMO RECORDATORIO: las coordenadas en pygame empiezan en la esquina superior izquierda,
        por lo tanto, para que el un objeto vaya hacia abajo se le debe aumentar su posicion en
        el eje y, reducirlo para moverse hacia arriba)

        Esta funcion mueve el avatar del jugador (en un futuro todas las entidades fisicas excepto
        proyectiles). Aqui es donde igual se complica la cosa, asi que lo voy a explicar:

        El primer paso es tener en cuenta que puede haber colisiones con multiples objetos a la
        vez, y que por lo tanto, tenemos que gestionar todas las colisiones que tengan lugar en
        un fotograma concreto.

        Es coveniente, ademas, saber en que direccion se ha producido la colision: de ahi el
        registro llamado coll_register, representado por una lista (los componentes son:
        (derecha, izquierda, abajo, arriba))

        Para evitar problemas, primero se gestiona uno de los ejes, se actualiza la posicion, y
        se hace lo mismo con el otro eje. Esto se debe a que si se comprueban los dos ejes a la
        vez, acabas con una incoherencia sobre donde poner el objeto tras la colision. En este
        caso, gestionamos primero el movimiento en el eje x y luego en el y.

        En el eje x: si el valor en el vector de movimiento es x, te estas moviendo hacia la
        derecha
        :return:
        """
        # Registro de los tipos de colisiones (derecha, izquierda, abajo, arriba)
        coll_register = [False, False, False, False]
        # Primero vamos a gestionar el movimiento en el eje x
        self.box.x += self.mov[0]
        # Recogemos la lista de cjajas con las que ha colisionado el avatar
        boxes_hit = self.check_coll(box_list)
        for box in boxes_hit:
            if self.mov[0] > 0:
                self.box.right = box.left
                coll_register[0] = True
            elif self.mov[0] < 0:
                self.box.left = box.right
                coll_register[1] = True
        # Ahora que tenemos el las colisiones en el eje x gestionadas, hacemos lo mismo con el eje y
        self.box.y += self.mov[1]
        boxes_hit = self.check_coll(box_list)
        for box in boxes_hit:
            if self.mov[1] > 0:
                self.box.bottom = box.top
                coll_register[2] = True
            elif self.mov[1] < 0:
                self.box.top = box.bottom
                coll_register[3] = True
        return coll_register

    def apply_state(self):
        """

        :return:
        """
        self.mov = [0, 0]
        if self.state:
            self.mov[0] -= self.spd
        if self.input[1]:
            self.mov[0] += self.spd
        self.mov[1] += self.mom_y
        self.mom[1] += self.grav
        if self.mom[1] > self.inertia:
            self.mom[1] = self.inertia

    def jump(self):

    def run(self):


    def land(self):
        self.mom[1] = 0
        self.air_time = 0
        self.sht_halt = 12

    def shoot(self):
        PASS

    def manage_coll(self, coll):
        if coll[0]:
            pass
        if coll[1]:
            pass
        if coll[2]:
            self.mom[1] = 0
            self.air_time = 0
        else:
            self.air_time += 1
        if coll[3]:
            self.mom[1] = 0

    def draw(self, screen, scroll):
        # Dibujamos el sprite del jugador donde este su caja de colisiones
        # Como la Hitbox del jugador no coincide con su sprite, hay que dibujar el sprite
        # con un offset
        screen.blit(self.sprite, (self.box.x - 8 - scroll[0], self.box.y - scroll[1]))

    def update(self, box_list):
        # Actualizo el movimiento del avatar y gestiono sus colisiones
        coll = self.move(box_list)
        self.manage_coll()
        for state in self.states:

