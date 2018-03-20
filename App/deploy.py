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

def get_Ressources(filename):
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
    #tx_hash = contract.constructor(args=[], transaction={'from': web3.eth.accounts[0], 'gas': 3000000}).transact()
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']
    print("Contract with address {} deployed".format(contract_address))
    return contract_address

def store_Ressources(filename, data):
    with open(filename, 'w') as metadataFile:
        json.dump(data, metadataFile)





setup_Web3()

#Load Resources
data = get_Ressources('metadata.json')

#Load Smart-Contract (SOL-FILE)
contract_interface = compile_sol(data["files"]["contract"], 'Authority')

#Deploy Smart-Contract to Testnet
contract_address = deploy_contract(contract_interface)
data["parameter"]["address"]=contract_address

#Safe Smart-Contract in Ressource-File
store_Ressources('metadata.json', data)
store_Ressources('interface.json', contract_interface)
