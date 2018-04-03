import json
import flask

#from web3 import Web3
from flask import Flask, request, jsonify
from etheronauth import generator
from etheronauth import storeOnBlockchain

app = Flask(__name__)

# JSON -> SIG
@app.route('/validateToken', methods=['GET', 'POST'])
def validateToken():
    if request.method == 'POST':
        permission_id_text = request.data
        verify(permission_id_text)
        return True
    else:
        raise ValueError('You must use a POST-Request')

def verify(permission_id):
    #permission_id = Web3.toBytes(hexstr=permission_id_text)
    #get JSON Token from Blockchain
    response = storeOnBlockchain.read_request(permission_id)
    #Generate JWT from JSON
    response["payload"]["verifier"] = storeOnBlockchain.get_coinbase()
    JWT = generator.encode_Data(response["payload"]).decode('utf-8')
    print(JWT)
    #Take tho whole token because order matters
    #Sign the JSON-Token on the Blockchain
    storeOnBlockchain.store_signature(permission_id, JWT)
    print ("stored")



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4777)
