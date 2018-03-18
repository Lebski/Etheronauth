import json
import web3
import time


from web3 import Web3, HTTPProvider, TestRPCProvider

def setup_Web3():
    global web3
    web3 = Web3(HTTPProvider('http://localhost:8545'))
    print("Sucessfully set up Web3 Env to Account: ", web3.eth.accounts[0])

def getRessources(filename):
    data = json.load(open(filename))
    return data

def make_request(contract_interface, _contract_address):
    deployed_Contract = web3.eth.contract(
        abi=contract_interface['abi'], address=_contract_address)
    print("Using Contract at contract at > {}\n".format(_contract_address))
    event_filter = deployed_Contract.eventFilter('PermissionRequestdeployed')
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(2)
        print("nothing else found")

def handle_event(event):
    print(event)


setup_Web3()
#Load address
data = getRessources('metadata.json')
#Load ABI
contract_interface = getRessources('interface.json')
make_request(contract_interface, data["parameter"]["address"])
