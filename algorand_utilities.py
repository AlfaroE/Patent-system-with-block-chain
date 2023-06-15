import algosdk
from algosdk import transaction
from algosdk import constants
from algosdk.v2client import algod
from algosdk import account, mnemonic, encoding
from algosdk.transaction import *
import json
import base64

algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "JzBNFMDyDTaNttfTSiCmu92UBGPqQ5La6EV9A4y1"}
)


def transfer_Algos(sender,receptor,SenderMnmonic,amount):
    privateKey = algosdk.mnemonic.to_private_key(SenderMnmonic)
    params = algod_client.suggested_params()
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE 
    receiver = receptor
    note = "Pago por solicitud de patente".encode()
    amount = int(amount)
    unsigned_txn = transaction.PaymentTxn(sender, params, receiver, amount, None, note)
    signed_txn = unsigned_txn.sign(privateKey)
    #submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))
    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)
    return txid
    
def opt_in(usrAddress,SenderMnmonic):
    privateKey = algosdk.mnemonic.to_private_key(SenderMnmonic)
    params = algod_client.suggested_params()
    account_info = algod_client.account_info(usrAddress)
    holding = None
    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]
        idx = idx + 1
        if (scrutinized_asset['asset-id'] == '239302561'):
            holding = True
            break
    if not holding:
        txn = AssetTransferTxn(
            sender=usrAddress,
            sp=params,
            receiver=usrAddress,
            amt=0,
            index='239302561')
        stxn = txn.sign(privateKey)

        try:
            txid = algod_client.send_transaction(stxn)
            print("Signed transaction with txID: {}".format(txid))
            confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
            print("TXID: ", txid)
            print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))

        except Exception as err:
            print(err)
    
def transfer_assets(usrAddress,SenderMnmonic,fileHash):
    params = algod_client.suggested_params()
    privateKey = algosdk.mnemonic.to_private_key(SenderMnmonic)
    txn = AssetTransferTxn(
        sender='YG6ZXLSRL7X567Z3MSKCI4ECQCHQMSQFO6PRF4S3C2ZIAGXHI2ZUVHOKDU',
        sp=params,
        receiver=usrAddress,
        amt=1,
        index='239302561',
        note= fileHash.encode()
        )
    stxn = txn.sign(privateKey)

    try:
        txid = algod_client.send_transaction(stxn)
        print("Signed transaction with txID: {}".format(txid))
        confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
        print("TXID: ", txid)
        print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))

    except Exception as err:
        print(err)
        

#opt_in('EDPOXN6YC76HJ7T2XYLWUA7TA274FPKCWI5UL37SCEFNIXYRK2QIYM56IE','quote absent slight tired hobby second seed dwarf rifle suggest welcome concert uncover hurry castle dust eagle thing coconut meat season suffer clean ability pig')