import json
import jwt


def get_Ressources(filename):
    data = json.load(open(filename))
    return data

def encode_Data(data, private_key):
    return(jwt.encode(data, private_key, algorithm='RS256')) # In doubt use algorithm='RS256'

def decode_Data(encoded_Data, public_key):
    return(jwt.decode(encoded_Data, public_key, algorithm='RS256')) # In doubt use algorithm='RS256'

def get_Key(keyfile, keyname):
    return(keys[keyname].encode('ascii'))

#Load Keyfile, get Private and Public Key
keys = get_Ressources('tokenstore.json')
private_key = get_Key(keys, "private_key")
public_key = get_Key(keys, "public_key")

#Load Permissionsfile, get header and payload
permissions = get_Ressources("exampleData/examplePermissions.json")
header = permissions["header"]
payload = permissions["payload"]
data = {'header': header, "payload": payload}

#Encode Data
encoded_Data = encode_Data(data, private_key)

#Decode Data
decoded_Data = decode_Data(encoded_Data, public_key)

print (decoded_Data)
print (encoded_Data)
