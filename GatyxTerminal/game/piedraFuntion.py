#piedraFuntion.py
import random as r
from colorama import Fore, Back, Style, init
ia = ["piedra", "tijera", "papel"]

def Game_1():
    player_input = input(Fore.GREEN + "Tú>>>").lower()
    iar = r.choice(ia)

    if player_input == "papel":
        if iar == "papel":
            resultado = "¡EMPATE!"
        elif iar == "piedra":
            resultado = "¡GANASTE!"
        else:
            resultado = "¡PERDISTE!"
    elif player_input == "piedra":
        if iar == "piedra":
            resultado = "¡EMPATE!"
        elif iar == "tijera":
            resultado = "¡GANASTE!"
        else:
            resultado = "¡PERDISTE!"
    elif player_input == "tijera":
        if iar == "tijera":
            resultado = "¡EMPATE!"
        elif iar == "papel":
            resultado = "¡GANASTE!"
        else:
            resultado = "¡PERDISTE!"
    else:
        print("Opción no válida")
        return

    print(resultado)
    print(Fore.GREEN + f"Computadora>>> {iar}")
    print(Fore.GREEN + f"Tú>>> {player_input}")		