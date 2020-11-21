from obj.tangible import *


class Player(Tangible):
    acceleration = 5
    inertia = 2
    """
    Clase del avatar que controla el jugador. Aviso para navegantes: se va a usar POO como base de
    de todas las clases instanciables que hagamos.
    """

    # Constructor
    def __init__(self, hp, x, y, sprite, m_spd, j_spd):
        super().__init__(x, y, sprite)
        self.hp = hp  # Puntos de vida del avatar
        self.m_spd = m_spd  # Velocidad maxima del avatar
        self.j_spd = j_spd  # Velocidad del avatar al saltar

    def take_damage(self, dam, diff):
        """
        Esta funcion se llamara en cuanto el jugador reciba daño (es decir, esté dentro de un rect de
        una instancia de una clase proyectil/explosion)
        :param dam:
        :param diff:
        :return:
        """
        self.hp -= dam * diff

    '''
    def die(self):
        if self.hp <= 0:
            return True
        else:
            return False
    '''

    def accelerate(self, direc):
        """

        :param direc:
        :return:
        """
        if abs(self.vec[0]) < abs(self.m_spd):
            self.vec[0] += Player.acceleration * direc

    def decelerate(self):
        """
        
        :return: 
        """
        if abs(self.vec[0]) < 0.5:
            self.vec[0] = 0
        if self.vec[0] != 0:
            self.vec[0] /= Player.inertia

    def move(self):
        """

        :return:
        """
        # Recogemos la lista de cjajas con las que ha colisionado el avatar
        boxes_hit = self.check_coll()
        # Registro de los tipos de colisiones que se han producido
        coll_register = (False, False, False, False)

        #for box in boxes_hit:
            #if self.vec[0] > 0:

        return coll_register

    def update(self):
        # Aplicamos gravedad y deceleracion
        self.fall()
        self.decelerate()
        # Actualizo la posicion del avatar
        self.move()
