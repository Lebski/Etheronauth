import json
from web3 import Web3
from etheronauth import storeOnBlockchain

sub = 1
exp = 1
nbf = 2
iat = 2
audience = 2333
permission_id = storeOnBlockchain.make_request(sub=sub, audience=audience, exp=exp, nbf=nbf, iat=iat)
output = permission_id.hex()
print (output)
permission_id = Web3.toBytes(hexstr=output)

storeOnBlockchain.store_signature(permission_id, '0xaba')
print(storeOnBlockchain.read_request(permission_id))
