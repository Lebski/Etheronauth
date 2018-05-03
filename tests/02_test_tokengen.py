import json
from etheronauth import tokengen
from etheronauth import log
from etheronauth import tools

# Please make sure:
# - You provide the File: ressources/jwt_keys.secure
# - You adjust the password in this file (line 13 + 16)

log.out.info("### Testing on module > tokengen <")

log.out.info("#Checking get_private_key")
log.out.info(tokengen.get_private_key("TestTestTest")[0:30])

log.out.info("#Checking get_public_key")
log.out.info(tokengen.get_public_key("TestTestTest")[0:30])
log.out.info("Loading Example")
data = tools.get_json("../tests/examples/example_jwt.json")

log.out.info("#Checking encode_jwt")
encoded_Data = tokengen.encode_jwt(data)
tools.write_file("../tests/results/res_encoded_jwt.txt", encoded_Data.decode())
log.out.info("Encoded JWT is: {} ...".format(encoded_Data[0:20]))

log.out.info("#Checking decode_jwt")
decoded_Data = tokengen.decode_jwt(encoded_Data)
tools.write_json("../tests/results/res_decoded_jwt.json", decoded_Data)
log.out.info("Decoded JWT is: {} ...".format(decoded_Data))
