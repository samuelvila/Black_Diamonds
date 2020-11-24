import pygame


class Background:
    def __init__(self, map_name):
        direc = "maps/res/" + map_name + "/"
        self.layers = [
            [0.25, [120, 10, 150, 400]],
            [0.25, [500, 30, 100, 400]],
            [0.5, [200, 40, 140, 400]],
            [0.5, [400, 90, 150, 400]]]
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
            if layer[0] == 0.5:
                pygame.draw.rect(frame, (220, 140, 140), obj_layer)
            if layer[0] == 0.25:
                pygame.draw.rect(frame, (180, 100, 100), obj_layer)
