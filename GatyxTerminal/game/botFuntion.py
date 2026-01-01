#botFuntion.py
import random as r
from colorama import Fore, Back, Style, init
bot_say_ok = [
#Cosas para decir
"Caca", "Ayer", "Si", "No", "Que", "Ummm", "Soy un bot", "Jajaja",
"Claro que sí", "Ni idea", "Tal vez", "Depende", "Nunca", "Siempre",
"Eso es secreto", "Pregunta otra vez", "Estoy pensando...", "No puedo decirlo",
"¡Qué pregunta!", "Interesante...", "Hmm...", "¿En serio?", "Obvio",
"Puede ser", "Nunca lo había pensado", "Me gusta eso", "¡Genial!",
"Lo siento, no entendí", "Quizás mañana", "Estoy ocupado", "¿Por qué preguntas eso?",
"Eso suena divertido", "¡Vaya!", "No sé", "Definitivamente", "Probablemente",
"¿En serio?", "¡Increíble!", "No me digas", "¡Qué locura!", "Eso es raro",
"Estoy confundido", "¡Qué interesante!", "No estoy seguro", "Buena idea",
"No puedo creerlo", "¡Fantástico!", "Eso me hace reír", "Me suena familiar",
"Eso es imposible", "Nunca había pensado en eso", "¡Exacto!", "Tal cual",
"¡Qué coincidencia!", "Eso es verdad", "Increíble, ¿no?", "No lo sabía",
"¡Sí, claro!", "Eso me recuerda algo", "Curioso...", "¡Qué bien!", "Eso me gusta",
"¡Wow!", "Eso es genial", "Me pregunto...", "No te creo", "¡Qué emocionante!",
"Eso es confuso", "¡Vamos allá!", "¡Qué divertido!", "Me encanta eso", "Eso es interesante",
"No estoy convencido", "¡Qué sorpresa!", "Eso es extraño", "¡Perfecto!", "Me parece bien",
"Eso suena mal", "¡Qué lástima!", "Eso es misterioso", "¡Qué emocionante!", "No importa",
"Eso es lógico", "¡Increíble!", "Eso es cierto", "No puedo esperar", "¡Qué divertido!",
"Eso es absurdo", "¡Qué genial!", "Eso me hace pensar", "Me encanta", "Eso es sorprendente","Agara la pala","EH","GG","F en el chat",    "*caminando*", "*te pego*", "*salta*", "*baila*", "*suspira*", "*mira alrededor*", "*corre*", "*se esconde*",
#Aciones
"*aplaude*", "*se tropieza*", "*grita*", "*se ríe*", "*llora*", "*guiña un ojo*", "*se rascó la cabeza*", "*se encoge de hombros*",
    "*se estira*", "*da una vuelta*", "*se cae*", "*se levanta*", "*hace una reverencia*", "*lanza un hechizo*", "*se esconde detrás de algo*",
    "*toma algo*", "*lanza algo*", "*come algo*", "*bebe algo*", "*abraza*", "*golpea el aire*", "*mueve la cabeza*", "*pone cara de sorpresa*",
    "*pone cara de confusión*", "*parpadea*", "*se ríe maliciosamente*", "*se sorprende*", "*susurra*", "*grita fuerte*", "*da un salto mortal*",
    "*hace una señal*", "*se esconde bajo la mesa*", "*levanta los brazos*", "*se tira al suelo*", "*hace muecas*", "*se pone rojo*", "*se ríe nerviosamente*"]
    
bot_say_malo = ['NO', 'SOS VOS', 'ESTUPIDO!', 'CALLATE', 'JAJAJA QUE MALO SOS', 'HABLALE A MI MANO']
#Funcion del bot
def Bot():
	while True:
		player_say = input("User>>>")
		if player_say.lower() == "/quit":
			print(Fore.BLUE + "Salieno Del BOT...")
			break
		elif player_say.islower():
			bot = r.choice(bot_say_ok)
			print(f"BOT>>>{bot}")
		elif player_say.isupper():
			bot = r.choice(bot_say_malo)
			print(f"BOT>>>{bot}")
		else:
			print("BOT>>>No entendi.")