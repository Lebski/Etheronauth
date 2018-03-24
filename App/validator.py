import json
import flask

from flask import Flask, request, jsonify
from etheronauth import generator

app = Flask(__name__)

# JSON -> SIG
@app.route('/signToken', methods=['GET', 'POST'])
def make_Request():
    if request.method == 'POST':
        unsigned_Token = handle_input(request.get_json(force=True))
        
        return permission_id.hex()


    else:
        raise ValueError('You must use a POST-Request')

# JSON -> JWT
@app.route('/createJWT', methods=['GET', 'POST'])
def make_Request():

# JWT -> JSON
@app.route('/retrieveToken', methods=['GET', 'POST'])
def retrieve_Token():


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
    permission_id = request.data.decode('utf-8')
#    response = flask.jsonify(storeOnBlockchain.read_request(permission_id))
    response = storeOnBlockchain.read_request(permission_id)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4090)
