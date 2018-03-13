import json
import web3
import code
import inspect

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

def compile_sol(filename, _contractName):
    file = open(filename, "r")
    contract_source_code = file.read()
    compiled_sol = compile_source(contract_source_code) # Compiled source code
    contract_interface = compiled_sol['<stdin>:'+_contractName]
    return contract_interface

def deploy_contract(contract_interface):
    if not contract_interface:
        print ("Please specify contract-abi and bytecode")
    contract = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    #implement time calculation
    tx_hash = contract.deploy(args=[], transaction={'from': web3.eth.accounts[0], 'gas': 3000000})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']
    print("Contract with address {} deployed".format(contract_address))

    return contract_address

def make_request(contract_interface, _contract_address):
    deployed_Contract = web3.eth.contract(contract_interface['abi'], _contract_address)
    print("Using Contract at contract at > {}\n".format(_contract_address))

    #only for debugging, works if parent = accounts[0]
    testhash = '0xaba'
    testbytes = "hi"

    tryhash = Web3.toBytes(hexstr=testhash)#Web3.toBytes(text="testhash") funktion
    trybytes = testbytes#Web3.toBytes(text="testhash") funktion
    print ( Web3.toHex(tryhash))
    deployed_Contract.transact({'from': web3.eth.coinbase}).addPermissionRequest( tryhash, trybytes, trybytes, trybytes, 4, 4, 4, 4, 4, 4)

    [alg, typ, iss, sub, audience, exp, nbf, iat, jti] = deployed_Contract.call({'from': web3.eth.coinbase}).permissionList(tryhash)
    #IN CASE OF HEX: print ('Erg: ', Web3.toHex(getHash[0].encode('latin-1')))

    print ('Erg: ', alg, typ, iss, sub, audience, exp, nbf, iat, jti)





setup_Web3()
data = getRessources('metadata.json')

#Compile WhoVote Contract
voting_interface = compile_sol(data["files"]["contract"], 'Authority')
contract_address = deploy_contract(voting_interface)
#use_deployed_contract(voting_interface, contract_address)
make_request(voting_interface, contract_address)
