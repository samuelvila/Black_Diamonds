import pygame
import var
from maps import background


class Map:
    def __init__(self, map_name):
        self.tile_map = []          # Lista con los valores de lso tiles del mapa
        self.tile_set = []          # Lista con las texturas de los tiles
        self.tile_boxes = []        # Lista con las hitbox de los tiles
        self.bckgnd = background.Background(map_name)
        self.p_spawn = [300, 200]   # Punto de aparicion del jugador
        self.load(map_name)         # Cargamos el mapa

    def load(self, map_name):
        # Establecemos el directorio del mapa en el que estamosss
        direc = "maps/res/" + map_name + "/"
        # Cargamos las imagenes (texturas) del mapa: los nombres son estandar
        self.tile_set = [
            pygame.image.load(direc + "tiles/mid.png"),  # 1
            # Suelo y esquinas de suelo
            pygame.image.load(direc + "tiles/top.png"),  # 2
            pygame.image.load(direc + "tiles/top_right.png"),  # 3
            pygame.image.load(direc + "tiles/top_left.png"),  # 4
            # Paredes verticales
            pygame.image.load(direc + "tiles/left_wall.png"),  # 5
            pygame.image.load(direc + "tiles/right_wall.png"),  # 6
            # Esquinas
            pygame.image.load(direc + "tiles/left_corner.png"),  # 7
            pygame.image.load(direc + "tiles/right_corner.png")]  # 8
        # Abrimos el archivo que contiene el mapa de tiles
        f = open(direc + "tile_map.txt", 'r')
        data = f.read()
        f.close()
        # Separamos las filas de datos segun el caracter de fin de linea (lo podemos cambiar)
        data = data.split('\n')
        # Insertamos en el mapa de tiles del objeto las filas que hemos separado
        for row in data:
            self.tile_map.append(row)

    def render(self, frame, scroll):
        self.bckgnd.render(frame, scroll)
        self.tile_boxes = []
        y = 0
        for row in self.tile_map:
            x = 0
            for column in row:
                # Si el valor en la columna actual del mapa de tiles es distinto de 0,
                # el tile no es 'aire', y se transforma en un int para transformarlo
                # directamente en un indice del set de tiles
                if column != '0':
                    # Dibujamos el tile correspondiente (-1 porque el set de tiles empieza en
                    # 0 pero en el archivo el valor 0 se reserva para el aire)
                    frame.blit(self.tile_set[int(column) - 1],
                               (x * var.TILE_SIZE - scroll[0],
                                y * var.TILE_SIZE - scroll[1]))
                    # Le asignamos una hitbox al tile
                    self.tile_boxes.append(pygame.Rect(x * var.TILE_SIZE,
                                                       y * var.TILE_SIZE,
                                                       var.TILE_SIZE,
                                                       var.TILE_SIZE))
                x += 1
            y += 1
