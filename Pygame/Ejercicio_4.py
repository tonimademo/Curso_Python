#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import sys
import string
import time

from pygame.locals import *

#Funcion para comprobar si al saltar cambia de nivel del suelo( colisiona con algun suelo diferente)
def saltar(pj, suelo1, suelo2, suelo3):
	if 	pygame.sprite.collide_rect(pj, suelo1) or pygame.sprite.collide_rect(pj, suelo2) or pygame.sprite.collide_rect(pj, suelo3):
			return 0
	else:
			return 10

#Funcion para comprobar si ha habido una colision
def colision_obj_est (pj, objt_est):
	if 	pygame.sprite.collide_rect(pj, objt_est):
			return 0
	else:
			return 1
def get_key():
	while 1:
		event = pygame.event.poll()
		if event.type == KEYDOWN:
			return event.key
		else:
			pass

			
def main():

	
	pygame.init()

	Reloj= pygame.time.Clock()

	Ventana = pygame.display.set_mode((570, 400))
	pygame.display.set_caption("Caballero en busca de su princesa")
	
	# Ruidito es un objeto Sound creado a partir del archivo *.wav
	Musica_intro = pygame.mixer.Sound("Intro.wav")
	Musica_ambiente = pygame.mixer.Sound("ambiente.wav")
	Musica_ranking = pygame.mixer.Sound("Ranking.wav")
    # Bajamos el volumen de la música (sí, se puede hacer antes o durante la reproducción)
	Musica_intro.set_volume(0.5)
	Musica_ambiente.set_volume(0.5)
	Musica_ranking.set_volume(0.5)
    # Reproducimos nuestro sample de música en un bucle infinito (-1)
	Musica_intro.play(-1)
    
	# Elegimos la fuente y el tamaño
	Fuente_Intro = pygame.font.Font(None, 22)
	Fuente= pygame.font.Font(None, 30)

	# Cargo las letras que informaran del tiempo y de las vidas y se renderizan
	Tiempo = Fuente.render("Tiempo: ", 0, (255,255,255))
	segundos = 10
	Segundos = Fuente.render(str(segundos), 0, (255,255,255))
	Mensaje_vidas = Fuente.render("Vidas: ", 0, (255,255,255))
	vidas = 10
	Vidas = Fuente.render(str(vidas), 0, (255,255,255))
	Intro_nomb = Fuente.render("Introduzca su nombre: ", 0, (255,255,255))
	Historia_1 = Fuente_Intro.render("Las fuerzas del mal ha robado el gran corazon de la princesa M. ", 0, (255,255,255))
	Historia_2 = Fuente_Intro.render("Para poder tener un corazon propio, han fragmentado el corazon robado.", 0, (255,255,255))
	Historia_3 = Fuente_Intro.render("Recupera los fragmentos del corazon de la princesa M y poder salvarla...", 0, (255,255,255))
	
	
	Fondo = pygame.image.load("escenario.png")
	Fondo_Negro = pygame.image.load("ranking.png")
	
	#Defino las coordenadas de las zonas del mapa que interactuaran con el pj
	suelo1_coord = (160,312,412,4)
	suelo1_topleft =(160,312)
	suelo2_coord = (22,242,178,4)
	suelo2_topleft =(22,242)
	suelo3_coord = (204,175,270,4)
	suelo3_topleft =(204,175)
	
	#Defino los surfaces de las zonas
	Suelo1 = Suelo(suelo1_coord,suelo1_topleft,Fondo.subsurface(suelo1_coord))
	Suelo2 = Suelo(suelo2_coord,suelo2_topleft,Fondo.subsurface(suelo2_coord))
	Suelo3 = Suelo(suelo3_coord,suelo3_topleft,Fondo.subsurface(suelo3_coord))
	
	#cargo las imagenes de los sprites de los pjś
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

	#creo el sprite del pj principal
	MiMonigotillo = Monigotillo((coordX, coordY), Imagen_pj)
	incrementoX = 0
	incrementoY = 0
	
	#Movimiento que tendran los malos y los corazones
	incrementoX_est = -3
	obj_est = tipo = tipo_mov = salto = malo = corazon= 0
	
	#Pantalla de introduccion de duracion 10 segundos
	while segundos >= 8:
		
		contador_new = time.time()
		if contador_new - contador > 1.0:
			segundos = segundos -1
			contador = contador_new	
			
		Ventana.blit(Fondo_Negro, (0, 0))
		Ventana.blit(Historia_1, (40, 45))
		Ventana.blit(Historia_2, (40, 95))
		Ventana.blit(Historia_3, (40, 145))
		pygame.display.flip()
		
		
	contador = time.time()
	segundos = 10
	Musica_intro.stop()
	Musica_ambiente.play(-1)
	#Pantalla del juego de duracion 10 segundos
	while segundos > 8:
	
		contador_new = time.time()
		print str(contador_new - contador)
		if contador_new - contador > 1.0:
			segundos = segundos -1
			Segundos = Fuente.render(str(segundos), 0, (255,255,255))
			contador = contador_new	
		Ventana.blit(Fondo, (0, 0))
		Ventana.blit(Mensaje_vidas, (5, 5))
		Ventana.blit(Vidas, (70, 5))
		Ventana.blit(Tiempo, (120, 5))
		Ventana.blit(Segundos, (200, 5))
		Ventana.blit(MiMonigotillo.image, MiMonigotillo.rect)
		
		#generador de maloso y de corazon
		if obj_est == 0:
			print "generando algo"
			prob = random.random()
			corazon = malo = 0
			coordXini_est = 573
			coordYini_est = random.randint(0,400)
			print str(prob)
			if prob > 0.5:
				print "generando malo"
				malo = 1
				Objt_est = Maloso((coordXini_est, coordYini_est), Imagen_maloso)	
			else:
				print "generando corazon"
				corazon = 1
				Objt_est = Heart((coordXini_est, coordYini_est), Imagen_heart)
			obj_est = 1
			
		else:
			Ventana.blit(Objt_est.image, Objt_est.rect)
			
		pygame.display.flip()
		# Manejador de eventos
		for evento in pygame.event.get():
			# Pulsación de la tecla escape
			
			if evento.type == pygame.KEYDOWN:
				tipo_mov = 1
				if evento.key == pygame.K_ESCAPE:
					sys.exit()
				elif evento.key == pygame.K_RIGHT:
					incrementoX = 5
					tipo = 1
				elif evento.key == pygame.K_LEFT:
					incrementoX = -5
					tipo = 0
				elif evento.key == pygame.K_SPACE:
					#Preparo las variables para controlar el salto
					salto = 1
					#Guardo desde que altura voy a saltar
					suelo = coordY
					fin_salto = 0
					#Guardo hasta que altura voy a saltar
					limite_salto = coordY - 75
					while fin_salto == 0:
						Ventana.blit(Fondo, (0, 0))
						Ventana.blit(Mensaje_vidas, (5, 5))
						Ventana.blit(Vidas, (70, 5))
						Ventana.blit(Tiempo, (120, 5))
						Ventana.blit(Segundos, (200, 5))
						Ventana.blit(MiMonigotillo.image, MiMonigotillo.rect)
						if obj_est == 1:
							Ventana.blit(Objt_est.image, Objt_est.rect)
							
						pygame.display.flip()
						
						#Si estoy subiendo
						if coordY > limite_salto and salto == 1:
							incrementoY = -10
						#Si salto de una plataforma a otra
						elif saltar(MiMonigotillo,Suelo1,Suelo2,Suelo3) == 0 or coordY == suelo:
							incrementoY = 0
							fin_salto = 1
							salto = 0
						#Si salto sobre el mismo nivel de suelo
						elif coordY < suelo:
							incrementoY = 10
							salto = 0
						#Actualizo al pj
						coordX = coordX + incrementoX
						coordY = coordY + incrementoY
						Coordenadas = (coordX, coordY)
						MiMonigotillo.update(Coordenadas, tipo, tipo_mov)
						if obj_est == 1:
							coordXini_est = coordXini_est + incrementoX_est
							if coordXini_est > 0:
								Coordenadas_est = (coordXini_est,coordYini_est )
								Objt_est.update(Coordenadas_est)
							else:
								obj_est = 0
								
						if colision_obj_est (MiMonigotillo, Objt_est) == 0 and obj_est == 1:
							if malo == 1:
								vidas = vidas -1
								
							else:	
								vidas = vidas +1
							Vidas = Fuente.render(str(vidas), 0, (255,255,255))
							obj_est = 0
						# Asignamos un "tic" de 30 milisegundos
						Reloj.tick(50)
		
		#Control de gravedad	
		
		incrementoY = saltar(MiMonigotillo,Suelo1,Suelo2,Suelo3)
				
		if evento.type == pygame.KEYUP:
			incrementoX = 0
			tipo_mov = 0

		coordX = coordX + incrementoX
		coordY = coordY + incrementoY

		
		Coordenadas_pj = (coordX, coordY)
		#Actualizo la posicion del pj principal
		MiMonigotillo.update(Coordenadas_pj, tipo, tipo_mov)
		#si hay algun pj estatico (sin que se mueva por teclado) actualizo su posicion y si ha llegado al final de la pantalla, no lo pinto mas
		if obj_est == 1:
			coordXini_est = coordXini_est + incrementoX_est
			if coordXini_est > 0:
				Coordenadas_est = (coordXini_est,coordYini_est )
				Objt_est.update(Coordenadas_est)
			else:
				obj_est = 0
			
		#Si ha habido una colision, contabilizo las vidas dependiendo si es un malo o un corazon	
		if colision_obj_est (MiMonigotillo, Objt_est) == 0:
			if malo == 1:
				vidas = vidas - 1
				
			else:	
				vidas = vidas + 1
			Vidas = Fuente.render(str(vidas), 0, (255,255,255))
			obj_est = 0
		# Asignamos un "tic" de 30 milisegundos
		Reloj.tick(50)

	#pantalla ranking
	
	Musica_ambiente.stop()
	Musica_ranking.play(-1)
	
	letras = []
	Ventana.blit(Fondo_Negro, (0, 0))
	Ventana.blit(Intro_nomb, (60, 45))
	pygame.display.flip()
	
	while 1:
		inkey = get_key()
		if inkey == K_BACKSPACE:
			letras = letras[0:-1]
		elif inkey == K_RETURN:
			break
		elif inkey == K_MINUS:
			current_string.append("_")
		elif inkey <= 127:
			letras.append(chr(inkey))
		Nombre_usuario = string.join(letras,"")
		Usuario = Fuente.render(str(Nombre_usuario), 0, (255,255,255))
		Ventana.blit(Usuario, (60, 90))
		pygame.display.flip()
		
	while True:
		
		Ventana.blit(Fondo_Negro, (0, 0))
		Ventana.blit(Usuario, (60, 45))
		Ventana.blit(Vidas, (350, 45))
		pygame.display.flip()
	
		for evento in pygame.event.get():
			# Pulsación de la tecla escape
			
			if evento.type == pygame.KEYDOWN:
				tipo_mov = 1
				if evento.key == pygame.K_ESCAPE:
					sys.exit()
		
		
			
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
