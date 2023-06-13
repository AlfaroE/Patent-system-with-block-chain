import algosdk
from algosdk import transaction
from algosdk import constants
from algosdk.v2client import algod
import json
import base64
import os


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
        input("Recuerde guardar cuidadosamente estos datos...\npulsa caulquier tecla para continuar")
    elif opt == ('n' or 'N' or 'No' or 'no'):
        return

def dispenser():
    return
    