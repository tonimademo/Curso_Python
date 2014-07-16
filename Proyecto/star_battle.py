#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import sys
import string
import time
import MySQLdb
import subprocess

from pygame.locals import *


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

	Conexion = MySQLdb.connect(host='localhost', user='master',passwd='master', db='Videojuegos')
	#Creamos el cursor, pero especificando que sea de la subclase DictCursor
	micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
	
	pygame.init()

	Reloj= pygame.time.Clock()

	Ventana = pygame.display.set_mode((849, 507))
	pygame.display.set_caption("Start Battle")
    
	# Elegimos la fuente y el tamaño
	Fuente_Intro = pygame.font.Font(None, 22)
	Fuente= pygame.font.Font(None, 30)

	# Cargo las letras que informaran del tiempo y de las vidas y se renderizan
	Tiempo = Fuente.render("Tiempo: ", 0, (255,255,255))
	Intro_nomb = Fuente.render("Introduzca su nombre: ", 0, (255,255,255))
	
	Fondo = pygame.image.load("escenarioSB.png")
	Fondo_Negro = pygame.image.load("ranking_PR.png")
	
	#cargo las imagenes de los sprites de los pjś
	Nave_im = pygame.image.load("nave.png")
	transparente = Nave_im.get_at((1, 1))
	Nave_im.set_colorkey(transparente)
	
	Imagen_alien = pygame.image.load("alien.png")
	transparente = Imagen_alien.get_at((1, 1))
	Imagen_alien.set_colorkey(transparente)
	
	Imagen_disparo = pygame.image.load("disparo.png")
	transparente = Imagen_disparo.get_at((1, 1))
	Imagen_disparo.set_colorkey(transparente)
	
	Imagen_explosion = pygame.image.load("explosion.png")
	transparente = Imagen_disparo.get_at((1, 1))
	Imagen_disparo.set_colorkey(transparente)
	
	puntuacion = 0
	Mensaje_puntuacion= Fuente.render("Puntos: ", 0, (255,255,255))
	Puntuacion = Fuente.render(str(puntuacion), 0, (255,255,255))
	contador = time.time()
	
	coordX = 300
	coordY = 160
	vivo = 1
	
	#creo el sprite del pj principal
	MiNave = Nave((coordX, coordY), Nave_im)
	incrementoX = 0
	incrementoY = 0
	
	#Movimiento que tendran los malos y los corazones
	incrementoX_est = -3
	obj_est = tipo = tipo_mov = salto = malo = corazon= 0
	
	#Lista de las explosiones
	explosiones = []
	#lista de los disparos
	disparos =[]

	
	while vivo:
	
		Ventana.blit(Fondo, (0, 0))
		Ventana.blit(Mensaje_puntuacion, (5, 5))
		Ventana.blit(Puntuacion, (100, 5))

		Ventana.blit(MiNave.image, MiNave.rect)
		for i in range(len(disparos)):
			Ventana.blit(disparos[i].image, disparos[i].rect)
		for j in range(len(explosiones)):
			Ventana.blit(explosiones[j].image, explosiones[j].rect)
		
		#generador de maloso y de corazon
		if obj_est == 0:
			prob = random.random()
			corazon = malo = 0
			coordXini_est = 845
			coordYini_est = random.randint(30,470)
			malo = 1
			Objt_est = Alien(coordXini_est, coordYini_est, Imagen_alien)	
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
					micursor.close()
					Conexion.close()
					sys.exit()
				elif evento.key == pygame.K_RIGHT:
					incrementoX = 5
				elif evento.key == pygame.K_LEFT:
					incrementoX = -5
				elif evento.key == pygame.K_UP:
					incrementoY = -5
				elif evento.key == pygame.K_DOWN:
					incrementoY = 5
				#Tecla para disparar
				elif evento.key == pygame.K_SPACE:
					#Calculo las coordenadas donde aparecera el nuevo disparo
					coordX_disparo = coordX + 75
 					coordY_disparo = coordY + 10
 					#Creo el nuevo surface del disparo
					Tiro = Disparo(coordX_disparo, coordY_disparo, Imagen_disparo)
					#Lo añado a mi lista de disaros	
					disparos.append(Tiro)
					if obj_est == 1:
						Ventana.blit(Objt_est.image, Objt_est.rect)	
					pygame.display.flip()

						
		if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_RIGHT:
				incrementoX = 0
				tipo_mov = 0
			elif evento.key == pygame.K_LEFT:
				incrementoX = 0
				tipo_mov = 0
			if evento.key == pygame.K_UP:
				incrementoY = 0
				tipo_mov = 0
			elif evento.key == pygame.K_DOWN:
				incrementoY = 0
				tipo_mov = 0
			
		#aplico el movimiento de la nave controlando que no se salga del mapa
		
		if coordX <= 0 and incrementoX > 0:
			coordX = coordX + incrementoX
		elif coordX >= 849 and incrementoX < 0:
			coordX = coordX + incrementoX
		elif (coordX > 0 and coordX < 849) and incrementoX != 0:
			coordX = coordX + incrementoX
		else:
			coordX = coordX
			
		if coordY <= 0 and incrementoY > 0:
			coordY = coordY + incrementoY
		elif coordY >= 507 and incrementoY < 0:
			coordY = coordY + incrementoY
		elif (coordY > 0 and coordY < 507) and incrementoY != 0:	
			coordY = coordY + incrementoY
		else:
			coordY = coordY
			
		Coordenadas_nave = (coordX, coordY)
		#Actualizo la posicion del pj principal
		MiNave.update(Coordenadas_nave)
		#Si choco contra un alien, muero
		if colision_obj_est (MiNave, Objt_est) == 0:
			vivo = 0
		#lista de los posibles disparos y explosiones que eliminare
		disparo_out = []
		explosiones_out = []
		
		#Actualizo los disparos si los hay
		for k in range(len(disparos)):
			disparos[k].coordX = disparos[k].coordX + 5
			Coordenadas_disparo = (disparos[k].coordX, disparos[k].coordY)
			disparos[k].update(Coordenadas_disparo)
			#Si ha habido una colision, elimino al alien y el disparo y actualizo la puntuacion
			if colision_obj_est (disparos[k], Objt_est) == 0:
				disparo_out.append(k)
				puntuacion = puntuacion + 1
				Puntuacion = Fuente.render(str(puntuacion), 0, (255,255,255))
				obj_est = 0
				Impacto = Explosion(Objt_est.coordX, Objt_est.coordY, Imagen_explosion)	
				explosiones.append(Impacto)
			#Si se ha salido del mapa
			elif disparos[k].coordX > 849:
				disparo_out.append(k)
		for l in range(len(explosiones)):
			if explosiones[l].vivo == 1:
				explosiones[l].update()
			else:
				explosiones_out.append(l)
		#elimino los disparos que ha impactado o se han salido del mapa
		for h in range(len(disparo_out)):
			del disparos[disparo_out[h]]	
		#elimino las explosiones que ya se han producido
		for m in range(len(explosiones_out)):
			del explosiones[explosiones_out[m]]			
		#si hay algun pj estatico (sin que se mueva por teclado) actualizo su posicion y si ha llegado al final de la pantalla, no lo pinto mas
		if obj_est == 1:
			Objt_est.coordX = Objt_est.coordX + incrementoX_est
			if coordXini_est > 0:
				Coordenadas_est = (Objt_est.coordX,coordYini_est )
				Objt_est.update(Coordenadas_est)
			else:
				obj_est = 0
			
		# Asignamos un "tic" de 30 milisegundos
		Reloj.tick(50)

	#pantalla ranking
	
	#Musica_ambiente.stop()
	#Musica_ranking.play(-1)
	
	letras = []
	Ventana.blit(Fondo_Negro, (0, 0))
	Ventana.blit(Intro_nomb, (60, 45))
	pygame.display.flip()
	
	#Introduccion del nombre de usuario
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
		
	micursor.execute("Insert into Star_battle (user_name, puntuacion) VALUES (%s, %s);",(str(Nombre_usuario), str(puntuacion)))
	Conexion.commit()
		
	while True:
		
		Ventana.blit(Fondo_Negro, (0, 0))
		Ventana.blit(Usuario, (60, 45))
		Ventana.blit(Puntuacion, (350, 45))
		pygame.display.flip()
	
		for evento in pygame.event.get():
			# Pulsación de la tecla escape
			if evento.type == pygame.KEYDOWN:
				micursor.close()
				Conexion.close()
				sys.exit()
		
		
	
class Alien(pygame.sprite.Sprite):

    def __init__(self, coordX, coordY, imagen):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = imagen 
		self.coordX = coordX
		self.coordY = coordY
		self.rect = self.image.get_rect()
		self.rect.center = (coordX, coordY)


    def update(self, nuevas_coordenadas):
		self.rect.center = nuevas_coordenadas
		
			
class Nave(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = imagen
		a=0
		c=0
		self.arrayAnim=[]
		
		while a < 4:
			self.arrayAnim.append(self.ImgCompleta.subsurface((0,c*72,71,72)))	
			c=c+1
			a=a+1
			
		self.anim= 0
		self.actualizado = pygame.time.get_ticks()
		self.image = self.arrayAnim[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
			self.rect.center = nuevas_coordenadas
			if self.actualizado + 100 < pygame.time.get_ticks():
				self.anim= self.anim + 1
				if self.anim > 3:
					self.anim= 0
				self.image = self.arrayAnim[self.anim]
				#self.mask = pygame.mask.from_surface(self.image.subsurface((0,45,31,4)))
				self.actualizado= pygame.time.get_ticks()
				
class Disparo(pygame.sprite.Sprite):

    def __init__(self, coordX, coordY, imagen):
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = imagen
		self.coordX = coordX
		self.coordY = coordY
		a=0
		c=0
		self.arrayAnim=[]
		
		
		while a < 3:
			self.arrayAnim.append(self.ImgCompleta.subsurface((c*22,0,21,21)))	
			c=c+1
			a=a+1
			
		self.anim= 0
		self.actualizado = pygame.time.get_ticks()
		self.image = self.arrayAnim[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = (self.coordX, self.coordY)


    def update(self, nuevas_coordenadas):
			self.rect.center = nuevas_coordenadas
			if self.actualizado + 100 < pygame.time.get_ticks():
				self.anim= self.anim + 1
				if self.anim > 2:
					self.anim= 0
				self.image = self.arrayAnim[self.anim]
				self.actualizado= pygame.time.get_ticks()

class Explosion(pygame.sprite.Sprite):

    def __init__(self, coordX, coordY, imagen):
		pygame.sprite.Sprite.__init__(self)

		self.ImgCompleta = imagen
		self.coordX = coordX
		self.coordY = coordY
		self.vivo = 1
		a=0
		b=0
		self.arrayAnim=[]
		
		while a < 3:
			while b < 6:
				self.arrayAnim.append(self.ImgCompleta.subsurface((b*43,a*44,41,44)))	
				b=b+1
			b=0
			a=a+1
			
		self.anim= 0
		self.actualizado = pygame.time.get_ticks()
		self.image = self.arrayAnim[self.anim]
		self.rect = self.image.get_rect()
		self.rect.center = (self.coordX, self.coordY)


    def update(self):
			if self.actualizado + 100 < pygame.time.get_ticks():
				if self.anim >= 17:
					self.vivo= 0
					self.anim = 0
				else:
					self.anim= self.anim + 1
				self.image = self.arrayAnim[self.anim]
				self.actualizado= pygame.time.get_ticks()
			
main()
