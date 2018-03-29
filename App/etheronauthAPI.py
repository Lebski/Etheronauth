import json
import flask
import requests
from web3 import Web3

from flask import Flask, request, jsonify
from etheronauth import storeOnBlockchain
from etheronauth import generator

app = Flask(__name__)

@app.route('/makeRequest', methods=['GET', 'POST'])
def make_Request():
    if request.method == 'POST':
        permission_id = handle_input(request.get_json(force=True))
        RequestUrl = 'http://127.0.0.1:4777/validateToken'
        requests.post(RequestUrl, data=permission_id)
        return permission_id.hex()

    else:
        "please provide your input"
    return("Thank you for your participation")

def handle_input(request_json):
    sub = request_json['payload']['sub']
    exp = request_json['payload']['sub']
    nbf = request_json['payload']['sub']
    iat = request_json['payload']['sub']
    audience = request_json['payload']['sub']
    permission_id = storeOnBlockchain.make_request(sub=sub, audience=audience, exp=exp, nbf=nbf, iat=iat)
    #store_token(permission_id.hex())
    return permission_id

@app.route('/readToken', methods=['GET', 'POST'])
def read_token(permission_id=None):
    permission_id = request.data.decode('latin')
    permission_id_bytes = Web3.toBytes(hexstr=permission_id)
    token = storeOnBlockchain.read_request(permission_id_bytes)

    #turning dict into flask-specific json-object
    #response = flask.jsonify(token)



    #JWT = generator.encode_Data(token["payload"]).decode('utf-8')
    #JWT1 = JWT.split('.')[0:1]
    #JWT2 = JWT.split('.')[1:2]
    #new = JWT1[0] + "." + JWT2[0] + "." + str(token["signature"])
    #print (JWT1)
    #print (new)
        #turning dict into string
    response = json.dumps(token)
    return response

if __name__ == '__main__':
    app.run(debug=True)
