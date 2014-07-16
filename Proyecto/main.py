#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import os
import MySQLdb
import subprocess
os.system("clear")

class Handler:
	builder=None
	def __init__(self):
		# Iniciamos el GtkBuilder para tirar del fichero de glade
		self.builder = Gtk.Builder()
		self.builder.add_from_file("interfaz1.glade")
		self.handlers = {
			"onDeleteWindow": Gtk.main_quit,
			"Princess_Rescue_ejecutar": self.Princess_Rescue_ejecutar,
			"Star_Battle_ejecutar":self.Star_Battle_ejecutar,
			"Mostrar_Ventana_Est": self.Mostrar_Ventana_Est,
			"onButton_Consulta": self.onButton_Consulta,
			"Mostrar_Ventana_AcercaDe": self.Mostrar_Ventana_AcercaDe,
			"error_game_ok_clicked": self.error_game_ok_clicked,
			"onButton_Limpiar": self.onButton_Limpiar
			}

		# Conectamos las señales e iniciamos la aplicación
		self.builder.connect_signals(self.handlers)
		self.window = self.builder.get_object("window")
		self.window1 = self.builder.get_object("window1")
		self.about = self.builder.get_object("acerca_de_vent")
		self.error_game = self.builder.get_object("error_game")
		self.window.show_all()
		
	def onDeleteWindow(self, *args):
		print "Taluego noruego"
		Gtk.main_quit(*args)
		
	def Mostrar_Ventana_Est(self,window):
		self.window.hide()
		self.window1.show()
	
	def Mostrar_Ventana_AcercaDe(self,window):
		self.about.show()
		
	def error_game_ok_clicked(self,window):
		self.error_game.hide()
		
	def onButton_Limpiar(self,button):

		#Obtengo el objeto de los checks y del menu despregable
		nombre_check = self.builder.get_object("nombre_check")
		puntuacion_check = self.builder.get_object("puntuacion_check")
		
		#Obtengo los objetos de los entrytext
		nombre = self.builder.get_object("nombre")
		puntuacion = self.builder.get_object("puntuacion")
		texto = self.builder.get_object("textview")
		texto= texto.get_buffer()
		
		#Limpio los valores escritos
		nombre.set_text("")
		puntuacion.set_text("")
		texto.set_text("")
		
		
		
	def onButton_Consulta (self,button):
		#Obtengo el objeto de los checks y del menu despregable
		nombre_check = self.builder.get_object("nombre_check")
		puntuacion_check = self.builder.get_object("puntuacion_check")
		videojuego = self.builder.get_object("game")
		
		#Obtengo los objetos de los entrytext
		nombre = self.builder.get_object("nombre")
		puntuacion = self.builder.get_object("puntuacion")

		checks =[]
		checks_valores=[]
		
		if nombre_check.get_active():
			checks.append("user_name")
			checks_valores.append(nombre.get_text())
		if puntuacion_check.get_active():
			checks.append("puntuacion")
			checks_valores.append(origen.get_text())
			
		try:
			#Selecciono el juego
			videojuego = videojuego.get_active_text()
			if videojuego[0][0] == 'P':
				videojuego = "Princess_rescue"
			elif videojuego[0][0] == 'S':
				videojuego = "Star_battle"
			
			if len(checks) == 0:
				#Creo la consulta
				consulta = "SELECT * from " + videojuego
			
			else:
				#Creo la consulta
				consulta = "SELECT * from " + videojuego +" where " +checks[0]+ "= '" +checks_valores[0]+"'"

				for i in range(1,len(checks)):
					consulta = consulta + " AND " +checks[i]+ "='"+checks_valores[i]+"'"
			
			# Busco
			micursor.execute(consulta)
			texto = self.builder.get_object("textview")
			texto= texto.get_buffer()
			
			registros= micursor.fetchall()
			#limpio lo que habia antes escrito
			texto.set_text("")
			for registro in registros:
				texto.insert_at_cursor("ID: " + str(registro["id"]) + "         Nombre: " + str(registro["user_name"]) + "         Puntuacion: " + str(registro["puntuacion"]) + "\n")
		
			Conexion.commit()
			
		#Si no selecciono ningun juego, error
		except TypeError:
			self.error_game.show()
		
	def Princess_Rescue_ejecutar(self, window):
		self.window.hide()
		proc = subprocess.Popen('python princess_rescue.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
		resultado = proc.stdout.read()
		proc.stdout.close()
		self.window.show()
		print resultado
		
	def Star_Battle_ejecutar(self, window):
		self.window.hide()
		proc = subprocess.Popen('python star_battle.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
		resultado = proc.stdout.read()
		proc.stdout.close()
		self.window.show()
		print resultado
		
def main():
	window = Handler()
	Gtk.main()
	#Cierro la conexion
	micursor.close()
	Conexion.close()
	return 0

if __name__ == '__main__':
	
	Conexion = MySQLdb.connect(host='localhost', user='master',passwd='master', db='Videojuegos')
	#Creamos el cursor, pero especificando que sea de la subclase DictCursor
	micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
	
	main()
	
