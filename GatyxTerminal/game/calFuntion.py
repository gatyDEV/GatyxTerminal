#calFuntion.py
from colorama import init, Fore, Back, Style
init(autoreset=True)
#Suma FUNTION
def suma():
	try:
		primer_num = float(input("Primer número: "))
		segundo_num = float(input("Segundo número: "))
		resultado = primer_num + segundo_num
		print(Fore.GREEN + "El resultado es: ", resultado)
	except ValueError:
		print("Ups. Uvo Un ERROR")
#Resta FUNTION
def resta():
	try:
		primer_num = float(input("Primer número: "))
		segundo_num = float(input("Segundo número: "))
		resultado = primer_num - segundo_num
		print(Fore.GREEN + "El resultado es: ", resultado)
	except ValueError:
		print("Ups. Uvo Un ERROR")
#Multiplicar FUNTION
def multiplicacion():
	try:
		primer_num = float(input("Primer número: "))
		segundo_num = float(input("Segundo número: "))
		resultado = primer_num * segundo_num
		print(Fore.GREEN + "El resultado es: ", resultado)
	except ValueError:
		print("Ups. Uvo Un ERROR")
#Divicion FUNTION
def divicion():
	try:
		primer_num = float(input("Primer número: "))
		segundo_num = float(input("Segundo número: "))
		resultado = primer_num / segundo_num
		print(Fore.GREEN + "El resultado es: ", resultado)
	except ValueError:
		print("Ups. Uvo Un ERROR")