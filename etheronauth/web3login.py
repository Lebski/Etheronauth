import web3
import getpass

from web3.auto import w3
from etheronauth import log
from etheronauth import tools

def web3_login():
    log.out.info("\033[93m### GETH LOG IN ####\033[0m")
    is_unlocked = False
    attempts_left = 3
    while (is_unlocked is False and (attempts_left > 0)):
        log.out.debug("Loading User Info")
        user_info = tools.get_json("user_info.json")
        log.out.debug("User_info: {}".format(user_info))
        log.out.info("\033[93mPlease enter your username:\033[0m")
        #username = "user_1"
        username = input()
        try:
            account = user_info[username]["address"]
            log.out.info("\033[93mLogging in with Account: {}\033[0m".format(account))
            log.out.info("\033[93mPlease enter your Pasword\033[0m")
            password = getpass.getpass()
            is_unlocked = w3.personal.unlockAccount(account, password, 15000)
            if (is_unlocked is False):
                log.out.warning("\033[91mPassword incorrect, please try again.\033[0m")
                attempts_left -= 1
                if (attempts_left > 0):
                    log.out.warning("\033[91m{} attepts left\033[0m".format(attempts_left))
                else:
                    log.out.warning("\033[91mNo attepts left.\033[0m".format(attempts_left))
                    log.out.warning("\033[91mExiting...\033[0m".format(attempts_left))
                    exit()
            else:
                log.out.info("\033[92mLogin successful.\033[0m")
                return account
        except KeyError as e:
            log.out.warning("\033[91mUsername {} not found, please try again.\033[0m".format(username))
            attempts_left -= 1
            if (attempts_left > 0):
                log.out.warning("\033[91m{} attepts left\033[0m".format(attempts_left))
            else:
                log.out.warning("\033[91mNo attepts left.\033[0m".format(attempts_left))
                log.out.warning("\033[91mExiting...\033[0m".format(attempts_left))
                exit()

def web3_silent_login(account, password):
    is_unlocked = w3.personal.unlockAccount(account, password, 15000)
    if (is_unlocked):
        log.out.info("\033[92mLogin successful.\033[0m")
        return account

def web3_logout(account):
    w3.personal.lockAccount(account)
    log.out.info("\033[92mLogged out.\033[0m")


'''
def deploy_contract():

def load_contract():

def compile_contract():

def send_contract():

def store_contract_info():
'''
