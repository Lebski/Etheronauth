import web3
import getpass
import time
import json

from etheronauth import web3login
from etheronauth import tools
from etheronauth import log
from web3.auto import w3

# This method get's automatically called instanciation
def import_contract():
    contract_address = tools.get_file("contract_address.txt")
    contract_interface = tools.get_json("contract_interface.json")
    authority_contract = w3.eth.contract(abi=contract_interface['abi'], address=contract_address)
    log.out.debug("chainhandler: \"Imported contract: {}\"".format(authority_contract.address))
    return authority_contract

def submit_request(account, sub=0, aud=0, exp=0, nbf=0, iat=0, wait=False):
    log.out.debug("submit_request: \"Using contract at {}\"".format(authority_contract.address))

    # setting header
    alg = w3.toBytes(text="RS256")
    typ = w3.toBytes(text="JWT")
    aud = w3.toBytes(text=aud)

    # hashing request id
    try:
        request_id_bytes = w3.soliditySha3(['address', 'bytes32'], [account, aud])
    except web3.exceptions.InvalidAddress as e:
        log.out.warning("\033[91mPlease make sure your address has a valid EIP cheksum. Test on etherscan.io and correct in ressources/user_info.json\033[0m")
        exit()

    # casting those filthy bytes to an human-readable hexstr
    request_id = w3.toHex(request_id_bytes)
    request_id = request_id[0:20]
    # Proof that this works
    #log.out.debug(w3.toBytes(hexstr=request_id))
    #log.out.debug(request_id_bytes)

    # submit to blockchain
    txn_hash = authority_contract.functions.addPermissionRequest(request_id, alg, typ, aud).transact({'from': account})

    # wait for tx_receipt, could be disabled
    if (wait):
        timer = 50
        tx_receipt = None
        log.out.info("Transaction sent, waiting for mining: max. {} seconds".format(timer))
        while (tx_receipt is None and timer > 0):
            tx_receipt = w3.eth.getTransactionReceipt(txn_hash)
            time.sleep(1)
            timer -= 1
        if tx_receipt is not None:
            log.out.info("\033[92mTransaction with request id {} mined!\033[0m".format(request_id))


    return request_id

def request_token(account, request_id):
    log.out.debug("submit_request: \"Using contract at {}\"".format(authority_contract.address))
    log.out.debug("submit_request: \"Using request_id {}".format(request_id))

    # watch submit request
    request_id_bytes = w3.toBytes(hexstr=request_id)

    # Call contract
    alg, typ, iss, sub, aud, iat, nbf, exp, jti, auth_token = authority_contract.functions.permissionList(request_id_bytes).call({'from': account})


    # Sorry, web3 don't remove the padding so doing it manually
    typ = typ.split(b'\0',1)[0]
    alg = alg.split(b'\0',1)[0]
    aud = aud.split(b'\0',1)[0]
    auth_token = auth_token.split(b'\0',1)[0]

    #### Byte-String to text
    typ = w3.toText(typ)
    alg = w3.toText(alg)
    aud = w3.toText(aud)
    auth_token = w3.toText(auth_token)

    token_dict = {
       "header":{
          "typ": typ,
          "alg": alg
       },
       "payload":{
         "iss": iss,
         "sub": sub,
         "aud": aud,
         "exp": exp,
         "nbf": nbf,
         "iat": iat,
         "jti": jti,
       },
       "token": auth_token
    }

    #token_json = json.dumps(token_dict)
    log.out.debug("Token in dict-format: {}".format(token_dict))
    return token_dict

def store_token(account, request_id, auth_token, exp, nbf, iat, wait=False):
    token_bytes = w3.toBytes(text=auth_token)
    exp = int(exp)
    nbf = int(nbf)
    iat = int(iat)
    txn_hash = authority_contract.functions.storeToken(request_id, token_bytes, exp, nbf, iat).transact({'from': account})

    if (wait):
        timer = 50
        tx_receipt = None
        log.out.info("Transaction sent, waiting for mining: max. {} seconds".format(timer))
        while (tx_receipt is None and timer > 0):
            tx_receipt = w3.eth.getTransactionReceipt(txn_hash)
            time.sleep(1)
            timer -= 1
        if tx_receipt is not None:
            log.out.info("\033[92mToken with request id {} mined!\033[0m".format(request_id))



authority_contract = import_contract()
