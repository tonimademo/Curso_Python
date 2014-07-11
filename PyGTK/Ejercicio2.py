#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import os
import MySQLdb
os.system("clear")

class Handler:
	builder=None
	def __init__(self):
		# Iniciamos el GtkBuilder para tirar del fichero de glade
		self.builder = Gtk.Builder()
		self.builder.add_from_file("interfaz.glade")
		self.handlers = {
			"onDeleteWindow": Gtk.main_quit,
			"Mostrar_VentanaBorrar": self.Mostrar_VentanaBorrar,
			"Mostrar_VentanaInsert": self.Mostrar_VentanaInsert,
			"Mostrar_VentanaAct": self.Mostrar_VentanaAct,
			"on_btn_clicked_aboutdialog": self.on_btn_clicked_aboutdialog,
			"on_btn_clicked_help": self.on_btn_clicked_help,
			"onCloseAboutDialog": self.onCloseAboutDialog,
			"onButtonClick_new_limp": self.onButtonClick_new_limp,
			"onButtonClick_new_env": self.onButtonClick_new_env,
			"onButtonClick_borr_limp": self.onButtonClick_borr_limp,
			"onButtonClick_borr_env": self.onButtonClick_borr_env,
			"onButtonClick_act_env": self.onButtonClick_act_env,
			"onButtonClick_act_con": self.onButtonClick_act_con,
			"onButtonClick_act_limp": self.onButtonClick_act_limp,
			"onButtonClick_act_bus": self.onButtonClick_act_bus,
			"onCloseMessageDialog_insert": self.onCloseMessageDialog_insert,
			"onCloseMessageDialog_borrar": self.onCloseMessageDialog_borrar}

		# Conectamos las señales e iniciamos la aplicación
		self.builder.connect_signals(self.handlers)
		self.window = self.builder.get_object("window")
		self.window1 = self.builder.get_object("window1")
		self.window2 = self.builder.get_object("window2")
		self.about = self.builder.get_object("acerca_de")
		self.ventana_help = self.builder.get_object("ventana_help")
		self.warning_insert = self.builder.get_object("warning_insert")
		self.warning_borrar = self.builder.get_object("warning_borrar")
		self.combo_borr = self.builder.get_object("combo_borr")
		self.window.show_all()
		
	def onDeleteWindow(self, *args):
		print "Taluego noruego"
		Gtk.main_quit(*args)
		
	def Mostrar_VentanaBorrar(self, window):
		print "vamos a mostrar la ventana de borrado"
		self.window.hide()
		self.window2.hide()
		self.window1.show()
	
	def Mostrar_VentanaAct(self, window):
		print "vamos a mostrar la ventana de borrado"
		self.window.hide()
		self.window1.hide()
		self.window2.show()
		
	def Mostrar_VentanaInsert(self, window):
		print "vamos a mostrar la ventana de insert"
		self.window.show()
		self.window1.hide()
		self.window2.hide()

	def on_btn_clicked_aboutdialog(self, window):
		print "Aparece querido Acerca de"
		self.about.show()
		
	def on_btn_clicked_help(self, window):
		print "Aparece querido Acerca de"
		self.ventana_help.show()

	def onCloseAboutDialog(self,window,data=None):
		print "Digan adiós a nuestro Acerca de"
		self.about.hide()
	
	def onCloseMessageDialog_insert(self,window,data=None):
		print "Digan adiós a nuestro Warning"
		self.warning_insert.hide()
		
	def onCloseMessageDialog_borrar(self,window,data=None):
		print "Digan adiós a nuestro Warning"
		self.warning_borrar.hide()
		
	def onButtonClick_new_limp(self,button):
		print "Vamos a limpiar"
		
		#Obtengo los objetos de los entry
		nombre = self.builder.get_object("nombre")
		origen = self.builder.get_object("origen")
		profesion = self.builder.get_object("profesion")
		edad = self.builder.get_object("edad")
		muerte = self.builder.get_object("muerte")
		
		#Limpio los valores escritos
		nombre.set_text("")
		origen.set_text("")
		profesion.set_text("")
		edad.set_text("")
		muerte.set_text("")
		
	def onButtonClick_new_env(self,button):
		print "Vamos a introducir tupla"
		
		nombre = self.builder.get_object("nombre_insert")
		origen = self.builder.get_object("origen_insert")
		profesion = self.builder.get_object("profesion_insert")
		edad = self.builder.get_object("edad_insert")
		muerte = self.builder.get_object("muerte_insert")
		
		try:
			nombre = nombre.get_text()
			origen = origen.get_text()
			profesion = profesion.get_text()
			edad = int(edad.get_text())
			muerte = muerte.get_text()
				
			# Insertamos el registro
			micursor.execute("INSERT INTO Criaturas (Nombre,Origen,Edad,Profesion,Muerte) VALUES (%s, %s, %s, %s, %s);",(nombre, origen, edad, profesion, muerte))
			Conexion.commit()
			
		except ValueError:
			print "no es entero"
			self.warning_insert.show()
			
	def onButtonClick_borr_limp(self,button):
		print "Vamos a limpiar"
		
		#Obtengo los objetos de los entry
		nombre = self.builder.get_object("nombre_borr_valor")
		origen = self.builder.get_object("origen_borr_valor")
		profesion = self.builder.get_object("profesion_borr_valor")
		edad = self.builder.get_object("edad_borr_valor")
		muerte = self.builder.get_object("muerte_borr_valor")
		
		#Limpio los valores escritos
		nombre.set_text("")
		origen.set_text("")
		profesion.set_text("")
		edad.set_text("")
		muerte.set_text("")		
		
	def onButtonClick_borr_env(self,button):
		print "Vamos a borrar tupla"
		
		#Obtengo el objeto de los checks
		nombre_check = self.builder.get_object("nombre_borr")
		origen_check = self.builder.get_object("origen_borr")
		profesion_check = self.builder.get_object("profesion_borr")
		edad_check = self.builder.get_object("edad_borr")
		muerte_check = self.builder.get_object("muerte_borr")
		
		#Obtengo los objetos de los entrytext
		nombre = self.builder.get_object("nombre_borr_valor")
		origen = self.builder.get_object("origen_borr_valor")
		profesion = self.builder.get_object("profesion_borr_valor")
		edad = self.builder.get_object("edad_borr_valor")
		muerte = self.builder.get_object("muerte_borr_valor")
		
		checks =[]
		checks_valores=[]
		
		#Creo dos listas con los campos y los valores de la tupla que quiero eliminar
		if nombre_check.get_active():
			checks.append("Nombre")
			checks_valores.append(nombre.get_text())
		if origen_check.get_active():
			checks.append("Origen")
			checks_valores.append(origen.get_text())
		if profesion_check.get_active():
			checks.append("Profesion")
			checks_valores.append(profesion.get_text())
		if edad_check.get_active():
			checks.append("Edad")
			checks_valores.append(edad.get_text())
		if muerte_check.get_active():
			checks.append("Muerte")
			checks_valores.append(muerte.get_text())
		
		#Creo la consulta
		consulta = "DELETE from Criaturas Where " +checks[0]+ "= '" +checks_valores[0]+"'"
		
		for i in range(1,len(checks)):
			consulta = consulta + " AND " +checks[i]+ "='"+checks_valores[i]+"'"
		
		# Borramos la tupla
		try:
			micursor.execute(consulta)
		except:
			print "valores incorrectos"
			self.warning_borrar.show()
			
		Conexion.commit()
		
	def onButtonClick_act_bus(self,button):
		print "Vamos a buscar tupla"
		
		#Obtengo el objeto de los checks
		nombre_check = self.builder.get_object("nombre_act")
		origen_check = self.builder.get_object("origen_act")
		profesion_check = self.builder.get_object("profesion_act")
		edad_check = self.builder.get_object("edad_act")
		muerte_check = self.builder.get_object("muerte_act")
		
		#Obtengo los objetos de los entrytext
		nombre = self.builder.get_object("nombre_act_valor")
		origen = self.builder.get_object("origen_act_valor")
		profesion = self.builder.get_object("profesion_act_valor")
		edad = self.builder.get_object("edad_act_valor")
		muerte = self.builder.get_object("muerte_act_valor")
		
		checks =[]
		checks_valores=[]
		
		#Creo dos listas con los campos y los valores de la tupla que quiero eliminar
		if nombre_check.get_active():
			checks.append("Nombre")
			checks_valores.append(nombre.get_text())
		if origen_check.get_active():
			checks.append("Origen")
			checks_valores.append(origen.get_text())
		if profesion_check.get_active():
			checks.append("Profesion")
			checks_valores.append(profesion.get_text())
		if edad_check.get_active():
			checks.append("Edad")
			checks_valores.append(edad.get_text())
		if muerte_check.get_active():
			checks.append("Muerte")
			checks_valores.append(muerte.get_text())
			
		if len(checks) == 0:
			#Creo la consulta
			consulta = "SELECT * from Criaturas"
		
		else:
			#Creo la consulta
			consulta = "SELECT * from Criaturas where " +checks[0]+ "= '" +checks_valores[0]+"'"

			for i in range(1,len(checks)):
				consulta = consulta + " AND " +checks[i]+ "='"+checks_valores[i]+"'"
		
		# Busco
		micursor.execute(consulta)
		texto = self.builder.get_object("textview_act")
		texto= texto.get_buffer()
		
		registros= micursor.fetchall()

		for registro in registros:

			texto.insert_at_cursor("Nombre: " + str(registro["Nombre"]) + "    Origen: " + str(registro["Origen"]) + "    Profesion: " + str(registro["Profesion"]) + "    Edad: " + str(registro["Edad"]) + "    Muerte: " + str(registro["Muerte"]) + "\n")
			
			
		Conexion.commit()
		
	def onButtonClick_act_con(self,button):
		print "Vamos a buscar tupla para cambiar"
		
		#Obtengo el objeto de los checks
		nombre_check = self.builder.get_object("nombre_act")
		origen_check = self.builder.get_object("origen_act")
		profesion_check = self.builder.get_object("profesion_act")
		edad_check = self.builder.get_object("edad_act")
		muerte_check = self.builder.get_object("muerte_act")
		
		#Obtengo los objetos de los entrytext
		nombre = self.builder.get_object("nombre_act_valor")
		origen = self.builder.get_object("origen_act_valor")
		profesion = self.builder.get_object("profesion_act_valor")
		edad = self.builder.get_object("edad_act_valor")
		muerte = self.builder.get_object("muerte_act_valor")
		
		checks =[]
		checks_valores=[]
		
		#Creo dos listas con los campos y los valores de la tupla que quiero eliminar
		if nombre_check.get_active():
			checks.append("Nombre")
			checks_valores.append(nombre.get_text())
		if origen_check.get_active():
			checks.append("Origen")
			checks_valores.append(origen.get_text())
		if profesion_check.get_active():
			checks.append("Profesion")
			checks_valores.append(profesion.get_text())
		if edad_check.get_active():
			checks.append("Edad")
			checks_valores.append(edad.get_text())
		if muerte_check.get_active():
			checks.append("Muerte")
			checks_valores.append(muerte.get_text())
			
		if len(checks) == 0:
			#Creo la consulta
			consulta = "SELECT * from Criaturas"
		
		else:
			#Creo la consulta
			consulta = "SELECT * from Criaturas where " +checks[0]+ "= '" +checks_valores[0]+"'"

			for i in range(1,len(checks)):
				consulta = consulta + " AND " +checks[i]+ "='"+checks_valores[i]+"'"
		
		# Busco
		micursor.execute(consulta)
		
		registro= micursor.fetchone()

		nombre.set_text(registro["Nombre"])
		origen.set_text(registro["Origen"])
		profesion.set_text(registro["Profesion"])
		edad.set_text(str(registro["Edad"]))
		muerte.set_text(registro["Muerte"])

			
		Conexion.commit()
		
	def onButtonClick_act_env(self,button):
		print "vamos a enviar los cambios"
		
		#Obtengo el objeto de los checks
		nombre_check = self.builder.get_object("nombre_act")
		origen_check = self.builder.get_object("origen_act")
		profesion_check = self.builder.get_object("profesion_act")
		edad_check = self.builder.get_object("edad_act")
		muerte_check = self.builder.get_object("muerte_act")
		
		#Obtengo los objetos de los entrytext
		nombre = self.builder.get_object("nombre_act_valor")
		origen = self.builder.get_object("origen_act_valor")
		profesion = self.builder.get_object("profesion_act_valor")
		edad = self.builder.get_object("edad_act_valor")
		muerte = self.builder.get_object("muerte_act_valor")
		
		#Creo una pareja de lista para los valores que he usado para buscar la tupla y para los valores que voy a cambiar
		
		checks =[]
		cambios_checks=[]
		checks_valores=[]
		cambios_valores=[]
		
		#Creo dos listas con los campos y los valores de la tupla que quiero eliminar
		if nombre_check.get_active():
			cambios_checks.append("Nombre")
			cambios_valores.append(nombre.get_text())
		else:
			checks,append("Nombre")
			checks_valores.append(nombre.get_text())
			
		if origen_check.get_active():
			cambios_checks.append("Origen")
			cambios_valores.append(origen.get_text())
		else:
			checks.append("Origen")
			checks_valores.append(origen.get_text())
			
		if profesion_check.get_active():
			cambios_checks.append("Profesion")
			cambios_valores.append(profesion.get_text())
		else:
			checks.append("Profesion")
			checks_valores.append(profesion.get_text())
			
		if edad_check.get_active():
			cambios_checks.append("Edad")
			cambios_valores.append(edad.get_text())
		else:
			checks.append("Edad")
			checks_valores.append(edad.get_text())
		
		if muerte_check.get_active():
			cambios_checks.append("Muerte")
			cambios_valores.append(muerte.get_text())
		else:
			checks.append("Muerte")
			checks_valores.append(muerte.get_text())
		
		#Creo la consulta
		consulta = "UPDATE Criaturas SET " +cambios_checks[0]+ "= '" +cambios_valores[0]+"'"
		
		#Añado los valores a cambiar
		for i in range(1,len(cambios_checks)):
			consulta = consulta + " , " +cambios_checks[i]+ "='"+cambios_valores[i]+"'"
			
		#Añado los valores que formaran la condicion
		
		consulta = consulta + " Where " +checks[0]+ "= '" +checks_valores[0]+"'"
		
		for i in range(1,len(checks)):
				consulta = consulta + " AND " +checks[i]+ "='"+checks_valores[i]+"'"
				
		# Borramos la tupla
		print consulta
		
		try:
			micursor.execute(consulta)
		except:
			print "valores incorrectos"
			self.warning_borrar.show()
			
		Conexion.commit()
		
		
		
	def onButtonClick_act_limp(self,button):
		print "vamos a limpiar"	
		
		
def main():
	
	
	window = Handler()
	Gtk.main()
	return 0

if __name__ == '__main__':
	
	Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
	#Creamos el cursor, pero especificando que sea de la subclase DictCursor
	micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
	
	main()
	
	#Cierro la conexion
	micursor.close()
	Conexion.close()
