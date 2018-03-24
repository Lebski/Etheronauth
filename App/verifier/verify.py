import json
from web3 import Web3
from etheronauth import storeOnBlockchain
from etheronauth import generator

#TODO Provide this with a filter
output = "0xf7ddaf656eba4e09162a4b1c7170d038c7a091ce7bbb1f326702f29d127f959d"

permission_id = Web3.toBytes(hexstr=output)
#get JSON Token from Blockchain
response = storeOnBlockchain.read_request(permission_id)
#Generate JWT from JSON
JWT = generator.encode_Data(response["payload"]).decode('utf-8')
#Take the last Part of the Token
signature = JWT.split('.')[2]
#Sign the JSON-Token on the Blockchain
storeOnBlockchain.store_signature(permission_id, signature)
