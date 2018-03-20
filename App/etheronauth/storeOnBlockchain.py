import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source

def setup_Web3():
    global web3
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    #errorhandling!
    print("sucessfully set up Web3 Env to Account: ", web3.eth.accounts[0])


def get_Ressources(filename):
    data = json.load(open(filename))
    return data

def get_Contract(contract_interface, contract_address):
        deployed_Contract = web3.eth.contract(
            abi=contract_interface['abi'], address=contract_address)
        return deployed_Contract

def make_request(sub=0, audience=0, exp=0, nbf=0, iat=0):
    sub = int(sub)
    exp = int(exp)
    nbf = int(nbf)
    iat = int(iat)
    audience = int(audience)
    print("Using Contract at contract at > {}\n".format(deployed_Contract.address))
    permission_id = Web3.soliditySha3(['address', 'uint256', 'uint256', 'uint256', 'uint256', 'uint256'], [web3.eth.coinbase, sub, audience, exp, nbf, iat])
    alg = Web3.toBytes(text="RS256")
    typ = Web3.toBytes(text="JWT")

    deployed_Contract.functions.addPermissionRequest(permission_id, alg, typ, sub, audience, exp, nbf, iat).transact({'from': web3.eth.coinbase})

    [alg, typ, iss, verifier,sub, audience, exp, nbf, iat, jti, signature] = deployed_Contract.functions.permissionList(permission_id).call(
        {'from': web3.eth.coinbase})

    print('Stored request on Blockchain: \n Algo:{}\n Typ:{}\n Issue:{}\n Verifier:{}\n Subject:{}\n Audience:{}\n Expiration:{}\n NotBefore:{}\n Issued at:{}\n Nonce:{}\n Signature:{}\n'.format(Web3.toText(alg), Web3.toText(typ), iss, verifier,sub, audience, exp, nbf, iat, jti, Web3.toText(signature)))
    return permission_id

def read_request(permission_id):
    print("Reading Contract at contract at > {}\n".format(deployed_Contract.address))
    [alg, typ, iss, verifier,sub, audience, exp, nbf, iat, jti, signature] = deployed_Contract.functions.permissionList(permission_id).call(
        {'from': web3.eth.coinbase})

    print('Load JWT-Token from Blockchain: \n Algo:{}\n Typ:{}\n Issue:{}\n Verifier:{}\n Subject:{}\n Audience:{}\n Expiration:{}\n NotBefore:{}\n Issued at:{}\n Nonce:{}\n Signature:{}\n'.format(Web3.toText(alg), Web3.toText(typ), iss, verifier,sub, audience, exp, nbf, iat, jti, Web3.toText(signature)))

    #### Sorry, web3 don't remove the padding    ####
    #### ... so doing it manually                ####
    typ = typ.split(b'\0',1)[0]
    alg = alg.split(b'\0',1)[0]
    signature = signature.split(b'\0',1)[0]

    #### Byte-String to text                     ####
    typ = Web3.toText(typ)
    alg = Web3.toText(alg)
    signature = Web3.toText(signature)

    token = {
       "header":{
          "typ": typ,
          "alg": alg
       },
       "payload":{
         "iss": iss,
         "sub": sub,
         "verifier": verifier,
         "aud": audience,
         "exp": exp,
         "nbf": nbf,
         "iat": iat,
         "jti": jti,
       },
       "signature": signature
    }
    #### Returns Token of type 'dict'            ####
    json_token = json.dumps(token)
    return json_token

def store_signature(permission_id, signature):

    signature_bytes = Web3.toBytes(text=signature)
    deployed_Contract.functions.storeSignature(permission_id, signature_bytes).transact({'from': web3.eth.coinbase})

### INITAL SETUP ###
setup_Web3()
data = get_Ressources('metadata.json')
interface = get_Ressources('interface.json')
voting_interface = interface
deployed_Contract = get_Contract(voting_interface, data["parameter"]["address"])


if __name__ == "__main__":
    setup_Web3()
    data = get_Ressources('metadata.json')
    interface = get_Ressources('interface.json')
    voting_interface = interface
    deployed_Contract = get_Contract(voting_interface, data["parameter"]["address"])
    make_request()
