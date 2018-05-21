import json
import flask

from flask import Flask, request, jsonify
from etheronauth import chainhandler
from etheronauth import web3login

app = Flask(__name__)

@app.route('/token/request/', methods=['POST'])
def create_request():
    permission_id = handle_raw_input(request.get_json(force=True))
    pending_url = "/token/request/" + str(permission_id)
    response = json.dumps({'generated': {"href" : pending_url, "id" : permission_id}})
    return response, 200

@app.route('/token/request/<string:permission_id>', methods=['GET'])
def check_request(permission_id):
    token = chainhandler.request_token(account, permission_id)
    jwt = token["token"]
    pending_url = "/token/request/" + str(permission_id)
    job = {"job": {"@uri" : pending_url,  "id" : str(permission_id), "status": "PENDING"}, "token": "NULL"}
    if jwt != "0":
        job["job"]["status"] = "COMPLETED"
        job["token"] = jwt
        json_job = json.dumps(job)
        return json_job, 202
    else:
        json_job = json.dumps(job)
        return json_job


def handle_raw_input(json_payload):
    aud = json_payload['payload']['aud']
    #exp = json_payload['payload']['exp']
    #nbf = json_payload['payload']['nbf']
    #iat = json_payload['payload']['iat']
    #sub = json_payload['payload']['sub']
    permission_id = chainhandler.submit_request(account, aud=aud)
    return permission_id

if __name__ == '__main__':
    account = web3login.web3_silent_login("0x4F6b4c67eEE111497Ef2b85FC1d133D3Ca3FD51B", "TestTestTest")

    app.run(debug=True)
