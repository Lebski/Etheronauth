import web3
import time

from web3.auto import w3
from etheronauth import chainhandler
from etheronauth import web3login
from etheronauth import log
from etheronauth import tokengen

def start_listening():
    transfer_filter = authority_contract.eventFilter('PermissionRequestDeployed')
    log.out.info("\033[92mStart listening!\033[0m")
    while True:
        for event in transfer_filter.get_new_entries():
            request_id_bytes = event["args"]["permissionId"]
            request_id = w3.toHex(request_id_bytes)
            log.out.debug("Event found {}".format(event["args"]["permissionId"]))
            verify(request_id)
        time.sleep(3)


def verify(request_id):
    request = chainhandler.request_token(account, request_id)
    #Fill in verifier address
    request["payload"]["iss"] = account

    time_current = time.time()
    time_nbf = time_current + 12
    time_exp = time_current + 60 * 10

    request["payload"]["iat"] = time_current
    request["payload"]["nbf"] = time_nbf
    request["payload"]["exp"] = time_exp

    jwt = tokengen.encode_jwt(request["payload"]).decode('utf-8')
    log.out.debug("JWT generated: {}".format(jwt))
    chainhandler.store_token(account, request_id, jwt, time_current, time_nbf, time_exp, wait=False)





authority_contract = chainhandler.authority_contract
account = web3login.web3_silent_login("0x4F6b4c67eEE111497Ef2b85FC1d133D3Ca3FD51B", "TestTestTest")
start_listening()
