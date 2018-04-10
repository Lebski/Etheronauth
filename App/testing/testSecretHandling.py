import json

from etheronauth import secure
from cryptography.fernet import Fernet

# Testing basic decryption/encryption
print("This is the testing func")
key = Fernet.generate_key()
fernet_obj = Fernet(key)
data = str.encode("Hello Hello Major Timo")
token = secure.encrypt(fernet_obj, data)
print("Testing Encryption with string: \"Hello Hello Major Timo\"")
print("Returns {}".format(token))
output = secure.decrypt(fernet_obj, token)
print("Decrypts to {}".format(output))

# Testing Key-Generation with passwords
#salt = get_salt()
key = secure.generate_key("Hallo")
fernet_obj = Fernet(key)
input = str.encode("Hello Hello Major Timo")
token = secure.encrypt(fernet_obj, input)
print("Testing Encryption with string: \"Hello Hello Major Timo\"")
print("Returns {}".format(token))
key = secure.generate_key("Hallo")
output = secure.decrypt(fernet_obj, token)
print("Decrypts to {}".format(output))


#From now on don't use the cryptography package

# Testing write/read files
secure.write_bytes_to_file("munckintime", "testing/output/testPassword.txt", b"5uP3R53CR37P55wRD")
data = secure.read_bytes_from_file("munckintime", "testing/output/testPassword.txt")
print("Passwordfile contains: {}".format(data))

example_json = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
secure.write_json_to_file("munckintime", "testing/output/testJson.txt", example_json)
data = secure.read_json_from_file("munckintime", "testing/output/testJson.txt")
print("Json in File is: {}".format(data))
