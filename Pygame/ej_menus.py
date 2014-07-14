#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la librería
import pygame

import sys

# Importamos constantes locales de pygame
from pygame.locals import *

# Iniciamos Pygame
pygame.init()

# Creamos una surface (la ventana de juego), asignándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos un título a la ventana
pygame.display.set_caption("Hola. Pulsa Escape para salir")

# Elegimos la fuente y el tamaño
Fuente= pygame.font.Font(None, 40)

# Renderizamos (convertimos a imagen) el mensaje con la fuente definida
Mensaje = Fuente.render("Esto es un texto para ver lo que sale", 0, (0,0,255))

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Mensaje, (5, 5))
    pygame.display.flip()
    # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                sys.exit()
