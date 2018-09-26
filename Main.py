import pygame, sys
import Imagen
from Imagen import *
booleano = True
ventana = pygame.display.set_mode((1280,720))
pygame.display.set_caption("ejemplo")
imagen1 = pygame.image.load('imagen 3.png')
imagen2 = pygame.image.load('imagen 2.png')
imagen3 = pygame.image.load('imagen 1.png')
personaje = Imagen(imagen1.convert(), imagen2.convert(),imagen3.convert())
ventana.fill((0,0,0))
while booleano:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            booleano = False
            break
    ventana.blit(personaje.imagen,personaje.rect)
    personaje.accion()
    pygame.display.update()