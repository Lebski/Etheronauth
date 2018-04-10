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
    return key

def get_salt():
    return os.urandom(16)

def read_bytes_from_file(pw_string, filepath):
    key = generate_key(pw_string)
    fernet_obj = Fernet(key)
    pw_File = open(filepath, "rb")
    data = pw_File.read()
    pw_File.close()
    file = decrypt(fernet_obj, data)
    return file

def write_bytes_to_file(pw_string, filepath, data):
    key = generate_key(pw_string)
    fernet_obj = Fernet(key)
    enc_file = encrypt(fernet_obj, data)
    out_file = open(filepath, "wb")
    out_file.write(enc_file)
    out_file.close()

#def read_json_from_file():
