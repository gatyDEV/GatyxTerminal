#tablaFuntion.py
def table():
	while True:
		print("¿Que tabla quieres saber 0 <-- para salir.?")
		try:
			num = int(input(">>> "))
			for i in range(11):
				x = num
				print(f"{x} x {i} = {x*i}")
			if (num == 0):
				break
		except ValueError:
			print("ERROR")