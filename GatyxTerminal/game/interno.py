#interno.py
#Codigo que da vida a todo
#Importando Libs

import os
import helpFuntion
import tablaFuntion
import calFuntion as cal
import zipFuntion as zyp
import piedraFuntion as piedra
import botFuntion as botsito
from colorama import Fore, Back, Style, init

def main_logic():
	while True: #<--- Bucle infinito
		command = input(">>>") #input
		tokken = command.split(" ") #Tokken
	
		#Detectar el Comandos Salir
		if command.lower() == "/quit":
			print(Fore.RED + "Saliendo...")
			break
		
		#Ayuda rapida
		elif command.lower() == "/help":
			print(Style.BRIGHT + Fore.WHITE + helpFuntion.help_say + Fore.RED)
		#--Comando Clear---
		elif command.lower() == "/clear":
			os.system("cls")
		#---Comando <Create>---
		elif tokken[0] == "/create":
			if tokken[1] == "bloc":
				name_bloc = input(Fore.CYAN + "Nombre>>>")
				contenido = input(Fore.CYAN + "Contenido>>>")
				with open(f"{name_bloc}.txt", 'w', encoding="utf-8") as archivo:
					archivo.write(contenido)
					print(Fore.GREEN + f"El Bloc de texto '{name_bloc}' A sido Creado Correctamente." + Fore.RED)
			elif tokken[1] == "dir":
				name_dir = input(Fore.CYAN + "Nombre>>>")
				os.makedirs(name_dir, exist_ok=True)
				print(Fore.GREEN + f"El directorio '{name_dir}' A sido Creado Correctamente." + Fore.RED)
			elif tokken[1] == "zip":
				zyp.zipe()

		#Comando tabla
		elif command.lower() == "/tabla":
			tablaFuntion.table()
	
		#---Comando Calculadora---
		elif command.lower() == "/cal":
			print(Fore.CYAN + ">>>¿Que Aras? + * / -")
			command_cal = input(Fore.GREEN + ">>>")
			if (command_cal == "+"):
				cal.suma()
			elif (command_cal == "*"):
				cal.multiplicacion()
			elif (command_cal == "/"):
				cal.divicion()
			elif (command_cal == "-"):
				cal.resta()
	
		#Comando del bot
		elif command.lower() == "/bot":
			botsito.Bot()
		#Comando del primer juego
		elif command.lower() == "/game_1":
			piedra.Game_1()