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

address1 = 'YG6ZXLSRL7X567Z3MSKCI4ECQCHQMSQFO6PRF4S3C2ZIAGXHI2ZUVHOKDU'


privateKey1 = algosdk.mnemonic.to_private_key('average across human control opera horror proud hand allow stand fan beach embrace pitch museum cactus type rug hat net myself wonder mixed abstract ordinary')


params = algod_client.suggested_params()
params.fee = 1000
params.flat_fee = True

def print_created_asset(algodclient, account, assetid):
    account_info = algodclient.account_info(account)
    idx = 0
    for my_account_info in account_info['created-assets']:
        scrutinized_asset = account_info['created-assets'][idx]
        idx = idx + 1
        if (scrutinized_asset['index'] == assetid):
            print("Asset ID: {}".format(scrutinized_asset['index']))
            print(json.dumps(my_account_info['params'], indent=4))
            break


#Función de utilidad para imprimir la tenencia de activos para la cuenta y assetid

def print_asset_holding(algodclient, account, assetid):
    account_info = algodclient.account_info(account)
    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]
        idx = idx + 1
        if (scrutinized_asset['asset-id'] == assetid):
            print("Asset ID: {}".format(scrutinized_asset['asset-id']))
            print(json.dumps(scrutinized_asset, indent=4))
            break

   
txn = AssetConfigTxn(
    sender=address1,
    sp=params,
    total=1000,
    default_frozen=False,
    unit_name="PATENT",
    asset_name="patent",
    manager=address1,
    reserve=address1,
    freeze=address1,
    clawback=address1,
    url="https://path/to/my/asset/details",
    decimals=0)
stxn = txn.sign("{}".format(privateKey1))

try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))

except Exception as err:
    print(err)

print("Transaction information: {}".format(
    json.dumps(confirmed_txn, indent=4)))
try:
    ptx = algod_client.pending_transaction_info(txid)
    asset_id = ptx["asset-index"]
    print_created_asset(algod_client, address1, asset_id)
    print_asset_holding(algod_client, address1, asset_id)
except Exception as e:
    print(e)

