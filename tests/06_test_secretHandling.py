import json

from etheronauth import secrethandling
from etheronauth import log
from cryptography.fernet import Fernet

log.out.info("### Testing on module > secrethandling <")
# Testing basic decryption/encryption
log.out.info("This is the testing func")
key = Fernet.generate_key()
fernet_obj = Fernet(key)
data = str.encode("Hello Hello Major Timo")
token = secrethandling.encrypt(fernet_obj, data)
log.out.info("Testing Encryption with string: \"Hello Hello Major Timo\"")
log.out.info("Returns {}".format(token))
output = secrethandling.decrypt(fernet_obj, token)
log.out.info("Decrypts to {}".format(output))

# Testing Key-Generation with passwords
#salt = get_salt()
key = secrethandling.generate_key("Hallo")
fernet_obj = Fernet(key)
input = str.encode("Hello Hello Major Timo")
token = secrethandling.encrypt(fernet_obj, input)
log.out.info("Testing Encryption with string: \"Hello Hello Major Timo\"")
log.out.info("Returns {}".format(token))
key = secrethandling.generate_key("Hallo")
output = secrethandling.decrypt(fernet_obj, token)
log.out.info("Decrypts to {}".format(output))


#From now on don't use the cryptography package

# Testing write/read files
secrethandling.write_bytes_to_file("munckintime", "../tests/results/crypto_test_password.txt", b"5uP3R53CR37P55wRD")
data = secrethandling.read_bytes_from_file("munckintime", "../tests/results/crypto_test_password.txt")
log.out.info("Passwordfile contains: {}".format(data))

example_json = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
secrethandling.write_json_to_file("munckintime", "../tests/results/crypto_test_json.txt", example_json)
data = secrethandling.read_json_from_file("munckintime", "../tests/results/crypto_test_json.txt")
log.out.info("Json in File is: {}".format(data))
