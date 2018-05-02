import json
from etheronauth import web3login
from etheronauth import log

log.out.info("### Testing on module > web3login <")
log.out.info("# Checking on web3_login")
account_test1 = web3login.web3_login()
log.out.info("Account: {}".format(account_test1))
log.out.info("# Checking on web3_logout")
web3login.web3_logout(account_test1)
log.out.info("# Logged out.")
log.out.info("# Checking on web3_silent_login")
account_test2 = web3login.web3_silent_login(account_test1, "TestTestTest")
log.out.info("Account: {}".format(account_test2))
web3login.web3_logout(account_test2)
log.out.info("# Logged out.")
