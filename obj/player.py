import sys

from obj.tangible import *


class Player(Tangible):
    inertia = 10
    """
    Clase del avatar que controla el jugador. Aviso para navegantes: se va a usar POO como base de
    de todas las clases instanciables que hagamos.
    """

    # Constructor
    def __init__(self, hp, x, y, sprite, spd, j_spd):
        super().__init__(x, y, sprite)
        self.hp = hp                    # Puntos de vida del avatar
        self.spd = spd                  # Velocidad del avatar al moverse
        self.j_spd = j_spd              # Velocidad del avatar al saltar
        self.air_time = 0               # Tiempo (en frames) que el jugador estuvo en el aire
        self.input = [False, False]     # Array de los posibles inputs te tipo hold

    def take_damage(self, dam, diff):
        """
        Esta funcion se llamara en cuanto el jugador reciba daño (es decir, esté dentro de un rect de
        una instancia de una clase proyectil/explosion)
        :param dam:
        :param diff:
        :return:
        """
        self.hp -= dam * diff

    def checkInput(self):
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
                    self.input[0] = True
                if event.key == pygame.K_d:
                    self.input[1] = True
                if event.key == pygame.K_SPACE:
                    if self.air_time < 6:
                        self.mom_y = -self.j_spd
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.input[0] = False
                if event.key == pygame.K_d:
                    self.input[1] = False
        # Aplicamos el input del jugador
        self.vec = [0, 0]
        if self.input[0]:
            self.vec[0] -= self.spd
        if self.input[1]:
            self.vec[0] += self.spd
        self.vec[1] += self.mom_y
        self.mom_y += self.grav
        if self.mom_y > self.inertia:
            self.mom_y = self.inertia

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
        self.box.x += self.vec[0]
        # Recogemos la lista de cjajas con las que ha colisionado el avatar
        boxes_hit = self.check_coll(box_list)
        for box in boxes_hit:
            if self.vec[0] > 0:
                self.box.right = box.left
                coll_register[0] = True
            elif self.vec[0] < 0:
                self.box.left = box.right
                coll_register[1] = True
        # Ahora que tenemos el las colisiones en el eje x gestionadas, hacemos lo mismo con el eje y
        self.box.y += self.vec[1]
        boxes_hit = self.check_coll(box_list)
        for box in boxes_hit:
            if self.vec[1] > 0:
                self.box.bottom = box.top
                coll_register[2] = True
            elif self.vec[1] < 0:
                self.box.top = box.bottom
                coll_register[3] = True
        return coll_register

    def update(self, box_list):
        # Actualizo el avatar
        coll = self.move(box_list)
        if coll[0]:
            pass
        if coll[1]:
            pass
        if coll[2]:
            self.mom_y = 0
            self.air_time = 0
        else:
            self.air_time += 1
        if coll[3]:
            self.mom_y = 0
