import json
import web3

from web3 import Web3
from web3.auto import w3

def get_Ressources(filename):
    data = json.load(open(filename))
    return data

def setup_Web3():
    #errorhandling!
    print("Sucessfully set up Web3 Env to Account: ", w3.eth.accounts[0])

def unlock(coinbase=None):
    if coinbase is not None:
        print(coinbase)
        is_unlocked = w3.personal.unlockAccount(coinbase, "password", 15000)
    else:
        is_unlocked = w3.personal.unlockAccount(preset_coinbase, "password", 15000)
    print("Sucessfully unlocked " + w3.eth.coinbase + ": " + str(is_unlocked))



### INITAL SETUP ###
print(">> Using module unlocker")
setup_Web3()
data = get_Ressources('metadata.json')
preset_coinbase = data["parameter"]["coinbase"]


if __name__ == "__main__":
    unlock()
