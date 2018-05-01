import json
import jwt
from etheronauth import tools
from etheronauth import log


def get_private_key():
    try:
        data = tools.get_json("jwt_keys.json")
        private_key = data["private_key"].encode("ascii")
        return private_key
    except IOError as e:
        log.out.error("Private_key could not be accessed")
        print (e)
        return False

def get_public_key():
    try:
        data = tools.get_json("jwt_keys.json")
        private_key = data["public_key"].encode("ascii")
        return private_key
    except IOError as e:
        log.out.error("Public_key could not be accessed")
        print (e)
        return False

#jwt-encrypted --> jwt-json
def decode_jwt(encoded_Data):
    public_key = get_public_key()
    dec_jwt = (jwt.decode(encoded_Data, public_key, algorithm='RS256')) # In doubt use algorithm='RS256'
    log.out.debug("Decoded JWT is: {}".format(dec_jwt))
    return dec_jwt

#jwt-json --> jwt-encrypted
def encode_jwt(data):
    private_key = get_private_key()
    enc_jwt = (jwt.encode(data, private_key, algorithm='RS256')) # In doubt use algorithm='RS256'
    log.out.debug("Encoded JWT is: {} ...".format(enc_jwt[0:20]))
    return enc_jwt
