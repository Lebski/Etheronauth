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

def make_request(deployed_Contract):
    print("Using Contract at contract at > {}\n".format(deployed_Contract.address))

    ############## only for debugging ##################
    testhash = '0xaba'
    testbytes = "hi"
    ####################################################

    hex_bytes = Web3.toBytes(hexstr=testhash)
    text_bytes = Web3.toBytes(text="testhash")
    print(text_bytes)
    deployed_Contract.functions.addPermissionRequest(hex_bytes, text_bytes, text_bytes, web3.eth.coinbase , 4, 4, 4, 4, 4).transact({'from': web3.eth.coinbase})

    ############## Filter nicht verfügbar ##############
    #transfer_filter = deployed_Contract.eventFilter('PermissionRequestdeployed', {'filter': {'_from': '0xD6C35F62F6Ca97A28f175078CD47Ce62bF74de36'}})
    #print(transfer_filter.get_all_entries())
    ####################################################

    [alg, typ, iss, sub, audience, exp, nbf, iat, jti, signature] = deployed_Contract.functions.permissionList(hex_bytes).call(
        {'from': web3.eth.coinbase})

    print('Erg: \n Algo:{}\n Typ:{}\n Issue:{}\n Subject:{}\n Audience:{}\n Expiration:{}\n NotBefore:{}\n Issued at:{}\n Nonce:{}\n Signature:{}\n'.format(Web3.toText(alg), Web3.toText(typ), iss, sub, audience, exp, nbf, iat, jti, Web3.toText(signature)))


setup_Web3()
data = get_Ressources('metadata.json')
interface = get_Ressources('interface.json')
voting_interface = interface
deployed_Contract = get_Contract(voting_interface, data["parameter"]["address"])
make_request(deployed_Contract)
