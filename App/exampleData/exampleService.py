import requests
import json
import pprint
pp = pprint.PrettyPrinter(depth=2)
RequestUrl = 'http://127.0.0.1:5000/makeRequest'

data = json.load(open("exampleData/examplePermissions.json"))
file = open("exampleData/examplePermissions.json", "r")
data =  file.read()

header={ "Content-Type": "application/json" }
response = requests.post(RequestUrl, data=data, headers=header)
permission_id = response.text
print(response.status_code)
print(response.text)
RequestUrl = 'http://127.0.0.1:5000/readToken'
read_response = requests.get(RequestUrl, data= permission_id).json()
print (pp.pprint(read_response))
