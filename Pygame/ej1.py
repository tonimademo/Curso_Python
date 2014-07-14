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
pygame.display.set_caption("Poniendo Imágenes")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
Imagen = pygame.image.load("imagen.png")
# posiciona las imágenes en Ventana
Ventana.blit(Fondo, (0, 0))
Ventana.blit(Imagen, (300, 200))
# refresca los gráficos
pygame.display.flip()

# Bucle infinito para mantener el programa en ejecución
while True:
    
    # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                sys.exit()
