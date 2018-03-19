import requests
import json
url = 'http://127.0.0.1:5000'

data = json.load(open("exampleData/examplePermissions.json"))
file = open("exampleData/examplePermissions.json", "r")
data =  file.read()

header={ "Content-Type": "application/json" }
response = requests.post(url, data=data, headers=header)
print(response.status_code)
print(response.text)
