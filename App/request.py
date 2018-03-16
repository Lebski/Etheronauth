import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract


def setup_Web3():
    global web3
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    print("sucessfully set up Web3 Env to Account: ", web3.eth.accounts[0])


def getRessources(filename):
    data = json.load(open(filename))
    return data

def make_request(contract_interface, _contract_address):
    deployed_Contract = web3.eth.contract(
        abi=contract_interface['abi'], address=_contract_address)
    print("Using Contract at contract at > {}\n".format(_contract_address))

    # only for debugging, works if parent = accounts[0]
    testhash = '0xaba'
    testbytes = "hi"

    # Web3.toBytes(text="testhash") funktion
    tryhash = Web3.toBytes(hexstr=testhash)
    trybytes = Web3.toBytes(text="testhash")
    print(trybytes)
    deployed_Contract.functions.addPermissionRequest(tryhash, trybytes, trybytes, web3.eth.coinbase , 4, 4, 4, 4, 4).transact({'from': web3.eth.coinbase})
    transfer_filter = deployed_Contract.eventFilter('PermissionRequestdeployed')#, {'filter': {'_from': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24'}})
    print(transfer_filter.get_all_entries())
    [alg, typ, iss, sub, audience, exp, nbf, iat, jti, signature] = deployed_Contract.functions.permissionList(tryhash).call(
        {'from': web3.eth.coinbase})

    print('Erg: \n Algo:{}\n Typ:{}\n Issue:{}\n Subject:{}\n Audience:{}\n Expiration:{}\n NotBefore:{}\n Issued at:{}\n Nonce:{}\n Signature:{}\n'.format(Web3.toText(alg), Web3.toText(typ), iss, sub, audience, exp, nbf, iat, jti, Web3.toText(signature)))


setup_Web3()
data = getRessources('metadata.json')
interface = getRessources('interface.json')
voting_interface = interface
make_request(voting_interface, data["parameter"]["address"])
