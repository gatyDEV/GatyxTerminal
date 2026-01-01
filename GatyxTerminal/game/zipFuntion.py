#zipFuntion.py
import zipfile
def zipe():
	nombre_zip = input("Ingresa el nombre del archivo ZIP (sin .zip): ") + ".zip"
	with zipfile.ZipFile(nombre_zip, 'w') as mi_zip:
		nombre_archivo = input("Nombre del archivo dentro del ZIP: ")
		contenido = input("Contenido del archivo: ")
		mi_zip.writestr(nombre_archivo, contenido)
		print(f"Archivo {nombre_zip} Creado!")