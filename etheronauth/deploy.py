import web3
import getpass
import time

from etheronauth import web3login
from etheronauth import tools
from etheronauth import log
from solc import compile_source
from web3.auto import w3

def load_contract():
    contract = tools.get_file("Authority.sol")
    return contract

def compile_contract():
    raw_contract = load_contract()
    compiled_contract = compile_source(raw_contract)
    try:
        contract_interface = compiled_contract["<stdin>:Authority"]
        tools.write_json("contract_interface.json", contract_interface)
        log.out.debug("Compiled contract: successful")
        return contract_interface
    except KeyError as e:
        log.out.warning("\033[91mCompiling was not successful. Check your solidity file.\033[0m")
        exit()

def store_contract_info(contract_address):
    tools.write_file("contract_address.txt", contract_address)

def deploy_contract():
    account_address = web3login.web3_login()
    contract_interface = compile_contract()
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    abs_cost = w3.eth.gasPrice * contract.constructor().estimateGas()
    log.out.debug("Absolute cost for this transaction: {} Ether".format(w3.fromWei(abs_cost, "ether")))
    deploy_txn = contract.constructor().transact(transaction={'from': w3.eth.accounts[0]})
    timer = 50
    tx_receipt = None
    log.out.info("Contract deployed, waiting for mining: max. {} seconds".format(timer))
    while (tx_receipt is None and timer > 0):
        tx_receipt = w3.eth.getTransactionReceipt(deploy_txn)
        time.sleep(1)
        timer -= 1
    if tx_receipt is None:
        log.out.warning("\033[91mCouldn't mine transaction. Check your node or increase timer (in deploy.py)\033[0m")
        web3login.web3_logout(account_address)
        exit()
    else:
        #log.out.debug("Transaction receipt: {}".format(tx_receipt))
        contract_address = tx_receipt['contractAddress']
        log.out.info("\033[92mContract with address {} deployed\033[0m".format(contract_address))
        store_contract_info(contract_address)
        web3login.web3_logout(account_address)
        return contract_address

if __name__ == "__main__":
    deploy_contract()
