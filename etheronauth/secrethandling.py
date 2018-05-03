import base64
import os
import json

from etheronauth import globalvars
from etheronauth import log
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

def read_bytes_from_file(pw_string, filename):
    filepath = filepath = get_dir() + filename
    key = generate_key(pw_string)
    fernet_obj = Fernet(key)
    try:
        pw_File = open(filepath, "rb")
        data = pw_File.read()
        pw_File.close()
    except IOError as e:
        log.out.error('File {} could not be written'.format(filepath))
        print (e)
        return False
    file = decrypt(fernet_obj, data)
    return file

def write_bytes_to_file(pw_string, filename, data):
    filepath = get_dir() + filename
    key = generate_key(pw_string)
    fernet_obj = Fernet(key)
    enc_file = encrypt(fernet_obj, data)
    try:
        out_file = open(filepath, "wb")
        out_file.write(enc_file)
        out_file.close()
        return True
    except IOError as e:
        log.out.error('File {} could not be written'.format(filepath))
        print (e)
        return False

def read_json_from_file(pw_string, filepath):
    data = read_bytes_from_file(pw_string, filepath)
    data_string = data.decode()
    json_obj = json.loads(data_string)
    return json_obj

def write_json_to_file(pw_string, filepath, data):
    string = json.dumps(data)
    byte_string = string.encode()
    write_bytes_to_file(pw_string, filepath, byte_string)

def get_dir():
    return globalvars.__path__ + "resources/"
