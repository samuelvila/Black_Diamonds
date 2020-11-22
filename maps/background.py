import pygame


class Background:
    def __init__(self, map_name):
        direc = "maps/res/" + map_name + "/"
        self.layers = [
            [0.25, [120, 10, 70, 400]],
            [0.25, [280, 30, 40, 400]],
            [0.5, [30, 40, 40, 400]],
            [0.5, [130, 90, 50, 400]]]
        self.layer_set = [
            pygame.image.load(direc + "bckgnd/sky.png"),
            pygame.image.load(direc + "bckgnd/clouds.png"),
            pygame.image.load(direc + "bckgnd/back2.png"),
            pygame.image.load(direc + "bckgnd/back1.png")]

    def render(self, frame, scroll):
        pygame.draw.rect(frame, (150, 160, 230), pygame.Rect(0, 260, 640, 100))
        for layer in self.layers:
            obj_layer = pygame.Rect(layer[1][0] - scroll[0]*layer[0],
                                    layer[1][1] - scroll[1]*layer[0],
                                    layer[1][2],
                                    layer[1][3])
