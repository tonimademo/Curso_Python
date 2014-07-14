#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import sys
import time

from pygame.locals import *

def saltar(pj, suelo1, suelo2, suelo3):
	if 	pygame.sprite.collide_rect(pj, suelo1) or pygame.sprite.collide_rect(pj, suelo2) or pygame.sprite.collide_rect(pj, suelo3):
			return 0
	else:
			return 10

def colision_obj_est (pj, objt_est):
	if 	pygame.sprite.collide_rect(pj, objt_est):
			return 0
	else:
			return 1
			
def pintar_est(obj_est):
	if obj_est == 1:
		coordXini_est = coordXini_est + incrementoX_est
		if coordXini_est > 0:
			Coordenadas_est = (coordXini_est,coordYini_est )
			Objt_est.update(Coordenadas_est)
		else:
			obj_est = 0
	

			
def main():

	
	pygame.init()

	Reloj= pygame.time.Clock()

	Ventana = pygame.display.set_mode((600, 400))
	pygame.display.set_caption("Caballero en busca de su princesa")
	
	# Ruidito es un objeto Sound creado a partir del archivo *.wav
	Musica = pygame.mixer.Sound("ambiente.wav")
    # Bajamos el volumen de la música (sí, se puede hacer antes o durante la reproducción)
	Musica.set_volume(0.5)
    # Reproducimos nuestro sample de música en un bucle infinito (-1)
	Musica.play(-1)
    
	# Elegimos la fuente y el tamaño
	Fuente= pygame.font.Font(None, 30)

	# Renderizamos (convertimos a imagen) el mensaje con la fuente definida
	Tiempo = Fuente.render("Tiempo: ", 0, (255,255,255))
	segundos = 10
	Segundos = Fuente.render(str(segundos), 0, (255,255,255))
	Mensaje = Fuente.render("Vidas: ", 0, (255,255,255))
	vidas = 10
	Vidas = Fuente.render(str(vidas), 0, (255,255,255))
	
	Fondo = pygame.image.load("escenario.png")
	Fondo_Ranking = pygame.image.load("ranking.png")
	Intro_nomb = Fuente.render("Introduzca su nombre: ", 0, (255,255,255))
	
	suelo1_coord = (160,312,412,4)
	suelo1_topleft =(160,312)
	suelo2_coord = (22,242,178,4)
	suelo2_topleft =(22,242)
	suelo3_coord = (204,175,270,4)
	suelo3_topleft =(204,175)
	
	Suelo1 = Suelo(suelo1_coord,suelo1_topleft,Fondo.subsurface(suelo1_coord))
	Suelo2 = Suelo(suelo2_coord,suelo2_topleft,Fondo.subsurface(suelo2_coord))
	Suelo3 = Suelo(suelo3_coord,suelo3_topleft,Fondo.subsurface(suelo3_coord))
	
	Imagen_pj = pygame.image.load("pj.png")
	transparente = Imagen_pj.get_at((0, 0))
	Imagen_pj.set_colorkey(transparente)
	
	Imagen_maloso = pygame.image.load("maloso.png")
	transparente = Imagen_maloso.get_at((0, 0))
	Imagen_maloso.set_colorkey(transparente)
	
	Imagen_heart = pygame.image.load("heart.png")
	transparente = Imagen_heart.get_at((0, 0))
	Imagen_heart.set_colorkey(transparente)
	
	contador = time.time()
	
	coordX = 300
	coordY = 160

	MiMonigotillo = Monigotillo((coordX, coordY), Imagen_pj)
	incrementoX = 0
	incrementoY = 0
	
	incrementoX_est = -3
	obj_est = tipo = tipo_mov = salto = malo = corazon= 0
	
	while True:
	
		Ventana.blit(Fondo_Ranking, (0, 0))
		Ventana.blit(Intro_nomb, (180, 5))
		pygame.display.flip()
		nombre = raw_input()
		Nombre = Fuente.render(str(nombre), 0, (255,255,255))
		Ventana.blit(Nombre, (180, 20))
		pygame.display.flip()
		
class Suelo(pygame.sprite.Sprite):
	
	def __init__(self, coordenadas, topleft, imagen):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = imagen
		self.rect = self.image.get_rect()
		self.rect.topleft = (topleft)
	
class Maloso(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
		pygame.sprite.Sprite.__init__(self)

		
		self.ImgCompleta = imagen
		a=0
		self.arrayAnim=[]

			
		while a < 2:	
			self.arrayAnim.append(self.ImgCompleta.subsurface((a*76,0,76,52)))	
			a = a+1
			
			
		self.anim= 0

		self.actualizado = pygame.time.get_ticks()
		self.image = self.arrayAnim[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
		self.rect.center = nuevas_coordenadas
		if self.actualizado + 100 < pygame.time.get_ticks():
			self.anim= self.anim + 1
			if self.anim > 1:
				self.anim= 0
			self.image = self.arrayAnim[self.anim]
			self.actualizado= pygame.time.get_ticks()
		
class Heart(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = imagen 
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
		self.rect.center = nuevas_coordenadas
		
			
class Monigotillo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = imagen
		a=0
		b=0
		c=0
		self.arrayAnim=[]

		self.arrayAnim = [None] * 3
        
		for i in range(3):
			self.arrayAnim[i] = [None] * 6
			
		while a < 2:
			while b < 2:
				self.arrayAnim[a][b] = (self.ImgCompleta.subsurface((c*31,0,31,50)))
				b=b+1	
				c=c+1
			a = a+1
			b = 0
			
		self.anim= 0

		self.actualizado = pygame.time.get_ticks()
		self.image = self.arrayAnim[0][self.anim]
		self.mask = pygame.mask.from_surface(self.image.subsurface((0,45,31,4)))
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas


    def update(self, nuevas_coordenadas, tipo, tipo_mov):
		if tipo_mov == 1:
			if tipo == 0:
				self.rect.center = nuevas_coordenadas
				if self.actualizado + 100 < pygame.time.get_ticks():
					self.anim= self.anim + 1
					if self.anim > 1:
						self.anim= 0
					self.image = self.arrayAnim[tipo][self.anim]
					#self.mask = pygame.mask.from_surface(self.image.subsurface((0,45,31,4)))
					self.actualizado= pygame.time.get_ticks()
			elif tipo == 1:
				self.rect.center = nuevas_coordenadas
				if self.actualizado + 100 < pygame.time.get_ticks():
					self.anim= self.anim + 1
					if self.anim > 1:
						self.anim= 0
					self.image = self.arrayAnim[tipo][self.anim]
					#self.mask = pygame.mask.from_surface(self.image.subsurface((0,45,31,4)))
					self.actualizado= pygame.time.get_ticks()
			elif tipo == 2:
				self.rect.center = nuevas_coordenadas
				if self.actualizado + 100 < pygame.time.get_ticks():
					self.anim= self.anim + 1
					if self.anim > 1:
						self.anim= 0
					self.image = self.arrayAnim[tipo][self.anim]
					#self.mask = pygame.mask.from_surface(self.image.subsurface((0,45,31,4)))
					self.actualizado= pygame.time.get_ticks()
		else:
			self.rect.center = nuevas_coordenadas
			if self.actualizado + 100 < pygame.time.get_ticks():
				self.image = self.arrayAnim[tipo][0]
				
				self.actualizado= pygame.time.get_ticks()

main()
