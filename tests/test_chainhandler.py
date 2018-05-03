import json
from etheronauth import chainhandler
from etheronauth import log
from etheronauth import tools
from etheronauth import web3login

# Please make sure:
# - Geth/ Another RPC is started
# - an instance of your contract is deployed
# - test_web3login is successful
# - the following files are present in the ressources folder
#     o resources/user_information.json
#     o contract_address.txt
#     o contract_interface.json

log.out.info("### Testing on module > chainhandler <")

log.out.info("# Checking import_contract")
contract = chainhandler.import_contract()
log.out.info("Imported contract: {}".format(contract.address))

log.out.info("# Checking submit_request")
account = web3login.web3_silent_login("0x4F6b4c67eEE111497Ef2b85FC1d133D3Ca3FD51B", "TestTestTest")
request_id = chainhandler.submit_request(account)
log.out.info("Request_id: {}".format(request_id))

log.out.info("# Checking request_token")
token = chainhandler.request_token(account, request_id)
