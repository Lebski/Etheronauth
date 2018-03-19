import json

from flask import Flask, request
from etheronauth import storeOnBlockchain

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        permission_id = handle_input(request.get_json(force=True))
        #return permission_id.hex()

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
    return permission_id



if __name__ == '__main__':
    app.run(debug=True)
