import pygame
class Imagen(pygame.sprite.Sprite):
    def __init__(self,imagen1, imagen2, imagen3 ):
        self.imagen = imagen1
        self.imagenes = []
        self.imagenes.append(imagen1)
        self.imagenes.append(imagen2)
        self.imagenes.append(imagen3)
        self.rect = self.imagen.get_rect()
        self.posX = 0
        self.posY =580
        self.rect.move_ip(self.posX, self.posY)
        self.cte = 0
    def accion(self):
        if self.cte == 0:
            self.imagen = self.imagenes[1]
            self.cte = 1
        elif self.cte == 1:
            self.imagen = self.imagenes[2]
            self.cte=2
        elif self.cte == 2:
            self.cte=0
            self.imagen = self.imagenes[0]