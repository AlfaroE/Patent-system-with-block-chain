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


def algo_request():
    r = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests.json')
    if r.status_code == 200:
        dict = r.json()
        if len(dict) > 1:
            for key in dict:
                usrAddress = dict[key]['usrAddress']
                amount = dict[key]['amount']
                print('\t'+'id de solicitud= ' + key)
                print('usrAddress= '+ usrAddress)
                print('amount= '+ amount)
                print('ticketBarCode= '+dict[key]['ticketBarCode'])
                print('')
                opt = input('\t Procesar Solicitud?    y/n \n r: ')
                if opt == 'y':
                    address = input("Ingrese Address de su cuenta:\t")
                    mnemonic = input("Ingrese el memotécnico de su Private key:\t")
                    txid = transfer_Algos(address,usrAddress,mnemonic,(int(amount)*1000000))
                    opt2 = input('\t Se concreto la transacción?    y/n \n r: ')
                    if opt2 == 'y':
                        r2 = requests.delete('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests/'+key+'.json')
                        if r2.status_code == 200:
                            print('La transacción fue exitosa')
                            r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests.json')
                            dict2 = r4.json()
                            if(len(dict2) < 2):
                                print('No hay más solicitudes')
                                break
                        else:
                            print('La transacción no fue completada')
                            r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests.json')
                            dict2 = r4.json()
                            if(len(dict2) < 2):
                                print('No hay más solicitudes')
                                break
                    elif opt2 == 'n':
                        r2 = requests.delete('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests/'+key+'.json')
                        print('La solicitud NO fue procesada y fue eliminada')
                        r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests.json')
                        dict2 = r4.json()
                        if(len(dict2) < 2):
                            print('No hay más solicitudes')
                            break
                elif opt == 'n':
                    r2 = requests.delete('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests/'+key+'.json')
                    print('La solicitud NO fue procesada y fue eliminada')
                    r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/algoRequests.json')
                    dict2 = r4.json()
                    if(len(dict2) < 2):
                        print('No hay más solicitudes')
                        break
        else:
            print('No hay más solicitudes')
    else:
        print('La solicitud fracaso')

def patent_request():
    r = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests.json')
    if r.status_code == 200:
        dict = r.json()
        if len(dict) > 1:
            for key in dict:
                usrAddress = dict[key]['usrAddress']
                patentTitle = dict[key]['patentTitle']
                fileHash = dict[key]['fileHash']
                filePath = dict[key]['filePath']
                print('\t'+'id de solicitud= ' + key)
                print('usrAddress= '+ usrAddress)
                print('patentTtile= '+ patentTitle)
                print('txid= '+ dict[key]['txid'])
                print('fileHash= '+fileHash)
                print('filePath= '+filePath)
                print('')
                opt = input('\t Procesar Solicitud?    y/n \n r: ')
                if opt == 'y':
                    print('')
                    mnemonic = input("Ingrese el memotécnico de Private key de Manager:\t")
                    transfer_assets(usrAddress,mnemonic,fileHash)
                    opt2 = input('\t Se concreto la transacción?    y/n \n r: ')
                    if opt2 == 'y':
                        request_dict = {'file':filePath,'patentTitle':patentTitle}
                        request_dict_json = json.dumps(request_dict)
                        r2 = requests.post('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentCatalog.json',data=request_dict_json)
                        r3 = requests.delete('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests/'+key+'.json')
                        if r3.status_code == 200 and r2.status_code == 200:
                            print('La transacción fue exitosa')
                            r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests.json')
                            dict2 = r4.json()
                            if(len(dict2) < 2):
                                print('No hay más solicitudes')
                                break
                        else:
                            print('La transacción no fue completada')
                            r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests.json')
                            dict2 = r4.json()
                            if(len(dict2) < 2):
                                print('No hay más solicitudes')
                                break
                    elif opt2 == 'n':
                        r3 = requests.delete('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests/'+key+'.json')
                        print('La solicitud NO fue procesada y fue eliminada')
                        r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests.json')
                        dict2 = r4.json()
                        if(len(dict2) < 2):
                            print('No hay más solicitudes')
                            break
                elif opt == 'n':
                    r3 = requests.delete('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests/'+key+'.json')
                    print('La solicitud NO fue procesada y fue eliminada')
                    r4 = requests.get('https://patents-1f7da-default-rtdb.firebaseio.com/data/patentRequests.json')
                    dict2 = r4.json()
                    if(len(dict2) < 2):
                        print('No hay más solicitudes')
                        break
        else:
            print('No hay más solicitudes')
    else:
        print('La solicitud fracaso')
   