import os
from account_utilities import *


def main_menu():
#    os.system('cls')
    print ("Selecciona una opción")
    print ("\t1 - Consultar patentes existentes")
    print ("\t2 - Crear Cuenta")
    print ("\t3 - Solicitar Algos")
    print ("\t4 - Solicitar Patente")
    print ("\t5 - Consultar Saldo")
    print ("\t6 - Consultar tus patentes")
    print ("\t7 - Consultar más información de una patente")
    print ("\t9 - Salir")



while True:
	main_menu()
 
	opcionMenu = input("inserta un numero valor >> ")
	print('')
 
	if opcionMenu=="1":
		consult_patent()
	elif opcionMenu=="2":
		sign_in()
	elif opcionMenu=="3":
		dispenser()
	elif opcionMenu=="4":
		patent_request()
	elif opcionMenu=="5":
		consult_amount()
	elif opcionMenu=="6":
		consult_assets()
	elif opcionMenu=="7":
		consult_pdf()
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



	

