import requests

post_code_req = requests.get('https://api.postcodes.io/postcodes/da13rb')

print(post_code_req.headers)
print(post_code_req.content)
postcode = post_code_req.json()

