import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        handle_input(request.get_json(force=True))
    else:
        "please provide your input"
    return("Thank you for your participation")

def handle_input(request_json):
    print(request_json['payload']['sub'])

if __name__ == '__main__':
    app.run(debug=True)
