import json
import jwt
import cryptography
import getpass
from etheronauth import tools
from etheronauth import log
from etheronauth import secrethandling


def get_private_key(password):
    try:
        data = secrethandling.read_json_from_file(password, "jwt_keys.secure")
        private_key = data["private_key"].encode("ascii")
        return private_key
    except IOError as e:
        log.out.error("Private_key could not be accessed")
        print (e)
        return False

def get_public_key(password):
    try:
        data = secrethandling.read_json_from_file(password, "jwt_keys.secure")
        private_key = data["public_key"].encode("ascii")
        return private_key
    except IOError as e:
        log.out.error("Public_key could not be accessed")
        print (e)
        return False

#jwt-encrypted --> jwt-json
def decode_jwt(encoded_Data):
    dec_jwt = (jwt.decode(encoded_Data, public_key, algorithm='RS256')) # In doubt use algorithm='RS256'
    log.out.debug("Decoded JWT is: {}".format(dec_jwt))
    return dec_jwt

#jwt-json --> jwt-encrypted
def encode_jwt(data):
    enc_jwt = (jwt.encode(data, private_key, algorithm='RS256')) # In doubt use algorithm='RS256'
    log.out.debug("Encoded JWT is: {} ...".format(enc_jwt[0:20]))
    return enc_jwt


is_unlocked = False
attempts_left = 3
while (is_unlocked is False and (attempts_left > 0)):
    log.out.info("\033[93mEnter your password to unlock your keys for signing/reading the jwt.\033[0m")
    password = getpass.getpass()
    try:
        #Handle private_key
        try:
            private_key = get_private_key(password)
            is_unlocked = True
            log.out.info("\033[92mPrivate Key successfuly imported.\033[0m")
        except KeyError as e:
            log.out.warning("\033[91mprivate_key not found. Do you want to import only public_key?\033[0m".format(secrethandling.get_dir()))
            private_key = None
            only_public = input("(y/N):")
            print(only_public)
            if only_public is not ("y" or "Y" or "yes" or "Yes"):
                log.out.warning("\033[91mNo Key found. Exiting \033[0m")
                exit()
        #Handle public_key
        try:
            public_key = get_public_key(password)
            is_unlocked = True
            log.out.info("\033[92mPublic Key successfuly imported.\033[0m")
        except KeyError as e:
            log.out.warning("\033[91mPublic Key not found. Make sure the File is in the {} File.\033[0m".format(secrethandling.get_dir()))
            private_key = None
    except cryptography.fernet.InvalidToken as e:
        log.out.warning("\033[91mPassword invalid, please try again.\033[0m")
        attempts_left -= 1
        if (attempts_left > 0):
            log.out.warning("\033[91m{} attepts left\033[0m".format(attempts_left))
        else:
            log.out.warning("\033[91mNo attepts left.\033[0m".format(attempts_left))
            log.out.warning("\033[91mExiting...\033[0m".format(attempts_left))
            exit()
