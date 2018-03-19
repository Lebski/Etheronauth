import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source

def setup_Web3():
    global web3
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    print("sucessfully set up Web3 Env to Account: ", web3.eth.accounts[0])


def get_Ressources(filename):
    data = json.load(open(filename))
    return data

def get_Contract(contract_interface, contract_address):
        deployed_Contract = web3.eth.contract(
            abi=contract_interface['abi'], address=contract_address)
        return deployed_Contract

def make_request(sub=0, audience=0, exp=0, nbf=0, iat=0):
    
    print("Using Contract at contract at > {}\n".format(deployed_Contract.address))
    permission_id = Web3.soliditySha3(['address', 'uint256', 'uint256', 'uint256', 'uint256', 'uint256'], [web3.eth.coinbase, sub, audience, exp, nbf, iat])
    alg = Web3.toBytes(text="RS256")
    typ = Web3.toBytes(text="JWT")

    deployed_Contract.functions.addPermissionRequest(permission_id, alg, typ, sub, audience, exp, nbf, iat).transact({'from': web3.eth.coinbase})


    ############## Filter nicht verfügbar ##############
    #transfer_filter = deployed_Contract.eventFilter('PermissionRequestdeployed', {'filter': {'_from': '0xD6C35F62F6Ca97A28f175078CD47Ce62bF74de36'}})
    #print(transfer_filter.get_all_entries())
    ####################################################

    [alg, typ, iss, verifier,sub, audience, exp, nbf, iat, jti, signature] = deployed_Contract.functions.permissionList(permission_id).call(
        {'from': web3.eth.coinbase})

    print('Stored request on Blockchain: \n Algo:{}\n Typ:{}\n Issue:{}\n Verifier:{}\n Subject:{}\n Audience:{}\n Expiration:{}\n NotBefore:{}\n Issued at:{}\n Nonce:{}\n Signature:{}\n'.format(Web3.toText(alg), Web3.toText(typ), iss, verifier,sub, audience, exp, nbf, iat, jti, Web3.toText(signature)))
    return permission_id

def read_request(permission_id):
    print("Reading Contract at contract at > {}\n".format(deployed_Contract.address))
    [alg, typ, iss, verifier,sub, audience, exp, nbf, iat, jti, signature] = deployed_Contract.functions.permissionList(permission_id).call(
        {'from': web3.eth.coinbase})

    print('Issued JWT-Token: \n Algo:{}\n Typ:{}\n Issue:{}\n Verifier:{}\n Subject:{}\n Audience:{}\n Expiration:{}\n NotBefore:{}\n Issued at:{}\n Nonce:{}\n Signature:{}\n'.format(Web3.toText(alg), Web3.toText(typ), iss, verifier,sub, audience, exp, nbf, iat, jti, Web3.toText(signature)))

def store_signature(permission_id, signature):

    signature_bytes = Web3.toBytes(text=signature)
    deployed_Contract.functions.storeSignature(permission_id, signature_bytes).transact({'from': web3.eth.coinbase})

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
