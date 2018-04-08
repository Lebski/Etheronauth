import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(fernet_obj, input):
    token = fernet_obj.encrypt(input)
    #print(token)
    return token

def decrypt(fernet_obj, token):
    output = fernet_obj.decrypt(token)
    #print(output)
    return output

def generate_key(pw_string, salt=b"salt_etheronauth"):
    password = str.encode(pw_string)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print (key)
    return key

def get_salt():
    return os.urandom(16)


if __name__ == "__main__":
    print("This is the testing func")
    key = Fernet.generate_key()
    fernet_obj = Fernet(key)
    input = str.encode("Hello Hello Major Timo")
    token = encrypt(fernet_obj, input)
    print("Testing Encryption with string: \"Hello Hello Major Timo\"")
    print("Returns {}".format(token))
    output = decrypt(fernet_obj, token)
    print("Decrypts to {}".format(output))

    #salt = get_salt()
    key = generate_key("Hallo")
    fernet_obj = Fernet(key)
    input = str.encode("Hello Hello Major Timo")
    token = encrypt(fernet_obj, input)
    print("Testing Encryption with string: \"Hello Hello Major Timo\"")
    print("Returns {}".format(token))
    key = generate_key("Hallo")
    output = decrypt(fernet_obj, token)
    print("Decrypts to {}".format(output))
