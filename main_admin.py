import os
from admin_utilities import *


def main_menu():
#    os.system('cls')
    print ("Selecciona una opción")
    print ("\t1 - Procesar Algos Request")
    print ("\t2 - Procesar Patent Request")
    print ("\t9 - Salir")



while True:
	main_menu()
 
	opcionMenu = input("inserta un numero valor >> ")
	print('')
 
	if opcionMenu=="1":
		algo_request()
	elif opcionMenu=="2":
		patent_request()
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")