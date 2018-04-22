import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from web3.auto import w3

def setup_Web3():
    global web3
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    print("sucessfully set up Web3 Env to Account: ", w3.eth.accounts[0])
    is_unlocked = w3.personal.unlockAccount(w3.eth.accounts[0], "password", 15000)
    print("Sucessfully unlocked? {}".format(is_unlocked))

    print("Still in syncing? {}".format(w3.eth.syncing))
    print("Account in use: {}".format(w3.eth.accounts[0]))
    print("Latest Block: {}".format(w3.eth.getBlock("latest").number))
    print("Balance of Account in use: {}".format(w3.eth.getBalance(w3.eth.accounts[0])))

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
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    #tx_hash = contract.deploy(args=[], transaction={'from': w3.eth.accounts[0]})
    abs_cost = w3.eth.gasPrice * contract.constructor().estimateGas()
    print("Absolute cost for this transaction: {}".format(abs_cost))

    #print((w3.eth.getBalance('0xdd34B44d8B80EB9C6f878Fc7F7689920B0935CBA'))<abs_cost)
    deploy_txn = contract.constructor().transact(transaction={'from': w3.eth.accounts[0]})
    tx_receipt = w3.eth.getTransactionReceipt(deploy_txn)
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
