import algosdk
from algosdk.v2client import algod

# Generate a fresh private key and associated account address

private_key, account_address = algosdk.account.generate_account()

# Convert the private key into a mnemonic which is easier to use
mnemonic = algosdk.mnemonic.from_private_key(private_key)

print("Private key mnemonic: " + mnemonic)
print("Account address: " + account_address)

algod_client = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-algorand.api.purestake.io/ps2",
    headers={"X-API-Key": "JzBNFMDyDTaNttfTSiCmu92UBGPqQ5La6EV9A4y1"}

)

algod_client2 = algod.AlgodClient(
    algod_token="",
    algod_address="https://testnet-api.algonode.cloud",
    headers={"X-API-Key": ""}
)

my_address = "SDXC4QPPWK2XUNH6PB5FPDWJBJF4MTKTVG2IBB53XVDF6K66CBOTWQFGQE"
account_info = algod_client.account_info(my_address)
print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

