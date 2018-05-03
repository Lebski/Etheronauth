import json
from etheronauth import log
from etheronauth import web3login
from etheronauth import chainhandler

# Please make sure:
# - Geth/ Another RPC is started
# - an instance of your contract is deployed
# - Tests 01 - 05 are successful
# - the following files are present in the ressources folder
#     o resources/user_information.json
#     o contract_address.txt
#     o contract_interface.json

# IMPORTANT: Run validator externally. Do NOT import.

log.out.info("### Testing on module > validator <")

log.out.info("# Checking submit_request")
account = web3login.web3_silent_login("0x4F6b4c67eEE111497Ef2b85FC1d133D3Ca3FD51B", "TestTestTest")
request_id = chainhandler.submit_request(account, wait=True)
log.out.info("Request_id: {}".format(request_id))
web3login.web3_logout
