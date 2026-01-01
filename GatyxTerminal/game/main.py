#Principal main.py
#Importando Libs
import os
import gui
import interno
from colorama import Fore, Back, Style, init
init(autoreset=True)

os.system("title GatyxTerminal -- Utility V1.0")

#ajustes Finales
gui.menu_funtion()
interno.main_logic()