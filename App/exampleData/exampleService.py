import requests
url = 'http://127.0.0.1:5000'

data = '{ "payload":{ "iss":"0.2",      "sub":"0x93794c6778F1C64b0f7CFBE1A7271c1749D8707d",      "aud":"0.2",      "exp":"0x93794c6778F1C64b0f7CFBE1A7271c1749D8707d",      "nbf":"0.2",      "iat":"0x93794c6778F1C64b0f7CFBE1A7271c1749D8707d",      "jti":"0.2"    },    "signature": "" }'

header={ "Content-Type": "application/json" }
response = requests.post(url, data=data, headers=header)
print(response.status_code)
print(response.text)
