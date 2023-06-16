import algosdk
from algosdk import transaction
from algosdk import constants
from algosdk.v2client import algod
import json
import base64
import os
import requests
from form import create_patent
from hash_file import get_hash
from algorand_utilities import *
import random
import subprocess

algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "JzBNFMDyDTaNttfTSiCmu92UBGPqQ5La6EV9A4y1"}
)



def sign_in():
    print("Registrarse le otorgará una cuenta en Algorand esta consiste de una “Address” y su llave privada que le será otorgada en forma de mnemotécnico, por favor guarde estos dos datos con cuidado porque nosotros no podemos recuperarlos ni los guardamos en nuestro sistema, pero serán necesarios si desea aumentar su número de Algos o desea solicitar patentes")
    print("")
    opt = input("Deseas generar la cuenta? \n \t y/n \n r:")
    if opt == ('y' or 'Y' or 'yes' or 'Yes'):
        private_key, account_address = algosdk.account.generate_account()
        mnemonic = algosdk.mnemonic.from_private_key(private_key)
        print("")
        print("Private key mnemonic: " + mnemonic)
        print("")
        print("Account address: " + account_address)
        print("")
        input("Recuerde guardar cuidadosamente estos datos...\npulsa enter para continuar")
    elif opt == ('n' or 'N' or 'No' or 'no'):
        input("pulsa enter para continuar")
        print('')

def dispenser():
    address = input("Ingrese Address de su cuenta:\t")
    algos = input("Ingrese Cantidad de Algos deseada:\t")
    ticket = input("Ingrese codigo de barras del ticket de pago:\t")
    request_dict = {'usrAddress':address,'amount':algos,'ticketBarCode':ticket}
    request_dict_json = json.dumps(request_dict)
    r = requests.post('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests.json',data=request_dict_json)
    if (r.status_code == 200):
        print('La solicitud fue enviada correctamente, uno de nuestros\nadministradores la revisara y aprobara a la brevedad,\npor favor consulte su saldo dentro de los siguientes dos minutos.\nBuen día')
    else:
        print('La solicitud fracaso favor de revisar sus datos e intentar de nuevo')
        input("pulsa enter para continuar")
        print('')
        
def patent_request():
    rand = random.randint(0,1)
    mainAddress = '0'
    if rand == 0:
        mainAddress = 'YG6ZXLSRL7X567Z3MSKCI4ECQCHQMSQFO6PRF4S3C2ZIAGXHI2ZUVHOKDU'
    else:
        mainAddress = 'YG6ZXLSRL7X567Z3MSKCI4ECQCHQMSQFO6PRF4S3C2ZIAGXHI2ZUVHOKDU'
    
    opt = input("Esta acción consumirá 01 Algos de su Wallet ¿Desea continuar? \n \t y/n \n r:")
    print('')
    if opt == ('y' or 'Y' or 'yes' or 'Yes'):
        address = input("Ingrese Address de su cuenta:\t")
        mnemonic = input("Ingrese el memotécnico de su Private key:\t")
        tittle,file = create_patent()
        hash = get_hash(file,65536)
        txid = transfer_Algos(address,mainAddress,mnemonic,1000000)
        request_dict = {'fileHash':hash,'patentTitle':tittle,'txid':txid,'usrAddress':address,'filePath':file}
        request_dict_json = json.dumps(request_dict)
        r = requests.post('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests.json',data=request_dict_json)
        if (r.status_code == 200):
            opt_in(address,mnemonic)
            print('La solicitud fue enviada correctamente, uno de nuestros\nadministradores la revisara y aprobara a la brevedad,\npor favor consulte sus patentes.\nBuen día')
        else:
            print('La solicitud fracaso favor de revisar sus datos e intentar de nuevo')
    elif opt == ('n' or 'N' or 'No' or 'no'):
        print('Hasta luego tenga buen día')
        input("pulsa enter para continuar")
        print('')

def consult_amount():
    address = input("Ingrese Address de su cuenta:\t")
    account_info = algod_client.account_info(address)
    print("\t Saldo actuales: "+ str(account_info.get('amount')) + '  Algos')
    print('')
    input("pulsa enter para continuar")
    print('')

def consult_assets():
    address = input("Ingrese Address de su cuenta:\t")
    account_info = algod_client.account_info(address)
    print("\t Patentes actuales: ")
    print(account_info.get('assets'))
    print('')
    input("pulsa enter para continuar")
    print('')

def consult_pdf():
    title = input('Ingrese nombre de la patente:\t')
    r = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentCatalog.json')
    if(r.status_code == 200):
        dict = r.json()
        for key in dict:
            if dict[key]['patentTitle'] == title:
                path = dict[key]['file']
                print(path)
                subprocess.Popen([path], shell= True)
        input("pulsa enter para continuar")
        print('')
    else:
        print('La solicitud fracaso favor de revisar sus datos e intentar de nuevo')
        input("pulsa enter para continuar")
        print('')

def consult_patent():
    r = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentCatalog.json')
    if(r.status_code == 200):
        dict = r.json()
        for key in dict:
            print('Nombre de patente:\t'+dict[key]['patentTitle'])
            print('Patent Path:\t'+dict[key]['file'])
            print('')
        input("pulsa enter para continuar")
        print('')
    else:
        print('La solicitud fracaso favor de revisar sus datos e intentar de nuevo')
        input("pulsa enter para continuar")
        print('')
    