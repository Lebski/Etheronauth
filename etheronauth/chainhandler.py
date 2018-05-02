import web3
import getpass
import time

from etheronauth import web3login
from etheronauth import tools
from etheronauth import log
from web3.auto import w3

# This method get's automatically called instanciation
def import_contract():
    contract_address = tools.get_file("contract_address.txt")
    contract_interface = tools.get_json("contract_interface.json")
    contract = w3.eth.contract(abi=contract_interface['abi'], address=contract_address)
    log.out.debug("Imported contract: {}".format(contract.address))
    return contract

def submit_request(account, sub=0, audience=0, exp=0, nbf=0, iat=0):
    log.out.debug("submit_request: \"Using contract at {}\"".format(contract.address))
    # cast numbers to int if they get delivered as json/string
    sub = int(sub)
    exp = int(exp)
    nbf = int(nbf)
    iat = int(iat)
    audience = int(audience)

    # setting header
    alg = w3.toBytes(text="RS256")
    typ = w3.toBytes(text="JWT")

    # hashing request id
    try:
        request_id = w3.soliditySha3(['address', 'uint256', 'uint256', 'uint256', 'uint256', 'uint256'], [account, sub, audience, exp, nbf, iat])
    except web3.exceptions.InvalidAddress as e:
        log.out.warning("\033[91mPlease make sure your address has a valid EIP cheksum. Test on etherscan.io and correct in ressources/user_info.json\033[0m")
        exit()


    # submit to blockchain
    txn_hash = contract.functions.addPermissionRequest(request_id, alg, typ, sub, audience, exp, nbf, iat).transact({'from': account})

    # wait for tx_receipt, could be disabled
    timer = 50
    tx_receipt = None
    log.out.info("Contract deployed, waiting for mining: max. {} seconds".format(timer))
    while (tx_receipt is None and timer > 0):
        tx_receipt = w3.eth.getTransactionReceipt(txn_hash)
        time.sleep(1)
        timer -= 1
    if tx_receipt is not None:
        log.out.info("\033[92mTransaction with request id {}... mined!\033[0m".format(request_id))

    return request_id




contract = import_contract()
