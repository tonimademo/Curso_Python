#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la librería
import pygame

import sys

# Creamos un reloj
Reloj= pygame.time.Clock()

# Importamos constantes locales de pygame
from pygame.locals import *

# Iniciamos Pygame
pygame.init()

# Creamos una surface (la ventana de juego), asignándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos un título a la ventana
pygame.display.set_caption("Moviendo Imágenes")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
Imagen = pygame.image.load("imagen.png")

coordX = 300
coordY = 200
Coordenadas = (coordX, coordY)

incrementoX = 0
incrementoY = 0

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Fondo, (0, 0))
    Ventana.blit(Imagen, Coordenadas)    
    pygame.display.flip()

	# Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sys.exit()
            elif evento.key == pygame.K_RIGHT:
                incrementoX = 5
            elif evento.key == pygame.K_DOWN:
                incrementoY = 5
            elif evento.key == pygame.K_LEFT:
                incrementoX = -5
            elif evento.key == pygame.K_UP:
                incrementoY = -5
        if evento.type == pygame.KEYUP:
            incrementoX = 0
            incrementoY = 0

    coordX = coordX + incrementoX
    coordY = coordY + incrementoY

    Coordenadas = (coordX, coordY)
    # Asignamos un "tic" de 30 milisegundos
    Reloj.tick(30)
