import pygame, sys

class Game:
    """
    Clase principal del juego. Cuando se crea una instancia de la clase se crea un display de pygame. Contendra un metodo
    llamado run() que lanzara el bucle principal del juego.
    """
    def __init__(self):
        display = pygame.display.set_mode((800,600))