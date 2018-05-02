import json
from etheronauth import chainhandler
from etheronauth import log

log.out.info("### Testing on module > chainhandler <")
log.out.info("# Checking on web3_login")
account_test1 = chainhandler.web3_login()
log.out.info("Account: {}".format(account_test1))
log.out.info("# Checking on web3_logout")
chainhandler.web3_logout(account_test1)
log.out.info("# Logged out.")
log.out.info("# Checking on web3_silent_login")
account_test2 = chainhandler.web3_silent_login(account_test1, "TestTestTest")
log.out.info("Account: {}".format(account_test2))
chainhandler.web3_logout(account_test2)
log.out.info("# Logged out.")
