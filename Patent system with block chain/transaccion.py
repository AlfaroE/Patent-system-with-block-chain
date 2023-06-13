import algosdk
from algosdk import transaction
from algosdk import constants
from algosdk.v2client import algod
import json
import base64

my_address = "SDXC4QPPWK2XUNH6PB5FPDWJBJF4MTKTVG2IBB53XVDF6K66CBOTWQFGQE"
receptor = "2F4S3Y6Q6XYUKBORVAZH7LRD4MW2VXSC3IBZ5GYBYB33KIZIA7HJQUVHZQ"
private_key = algosdk.mnemonic.to_private_key("glance syrup suffer normal mixture carpet hurdle clump copper gesture crush shrug exclude injury crater general decorate occur clever access river sunset purity abstract prefer") 
algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "JzBNFMDyDTaNttfTSiCmu92UBGPqQ5La6EV9A4y1"}

)


params = algod_client.suggested_params()
params.flat_fee = True
params.fee = constants.MIN_TXN_FEE 
receiver = receptor
note = "Hello World".encode() #Nota a
amount = 1000000
unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

signed_txn = unsigned_txn.sign(private_key)


#submit transaction
txid = algod_client.send_transaction(signed_txn)
print("Successfully sent transaction with txID: {}".format(txid))
# wait for confirmation 
try:
    confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
except Exception as err:
    print(err)
    
account_info = algod_client.account_info(my_address)

print("Transaction information: {}".format(
    json.dumps(confirmed_txn, indent=4)))
print("Decoded note: {}".format(base64.b64decode(
    confirmed_txn["txn"]["txn"]["note"]).decode()))
print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
print("Amount transfered: {} microAlgos".format(amount) )    
print("Fee: {} microAlgos".format(params.fee) )


print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")