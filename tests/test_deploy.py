import json
from etheronauth import deploy
from etheronauth import log
from etheronauth import tools

# Please make sure Geth/ Another RPC is started
# Please make sure test_web3login is successful
# Please make sure to adjust the account infomation in:
# o resources/user_information.json
# o this file
# Please provide the Authority smart contract in resources/Authority.sol

log.out.info("### Testing on module > deploy <")
log.out.info("# Checking load_contract")
contract = deploy.load_contract()
log.out.info("Contract: \"{}\" ...".format(contract[0:24]))
log.out.info("# Checking compile_contract")
contract_interface = deploy.compile_contract()
#log.out.debug("Compiled contract: \"{}\" ...".format(contract_interface))
if contract_interface is not None:
    log.out.info("Compiled contract: successful")
log.out.info("# Checking deploy_contract")
contract_address  = deploy.deploy_contract()
if contract_address is not None:
    log.out.info("Contract with address {} deployed".format(contract_address))
log.out.info("# Checking if file is written")
log.out.info("Address file contains: {}".format(tools.get_file("contract_address.txt")))
