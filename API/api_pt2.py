import requests
import json

json_body = json.dumps({'postcodes':['DA1 3RB', 'DA7 4EU']})
headers = {'Content-Type': 'application/json'}
post_code_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data = json_body)
print(post_code_multi_req.json)