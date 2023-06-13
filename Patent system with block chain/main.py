import algosdk
import os
from account_utilities import *

def main_menu():
    os.system('cls')
    print ("Selecciona una opción")
    print ("\t1 - Consultar patentes existentes")
    print ("\t2 - Crear Cuenta")
    print ("\t3 - Solicitar Algos")
    print ("\t4 - Solicitar Patente")
    print ("\t5 - Consultar Saldo")
    print ("\t6 - Consultar tus patentes")
    print ("\t9 - Salir")



while True:
	main_menu()
 
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		sign_in()
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="5":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="6":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



	

