import requests
import json 
res = requests.get('http://127.0.0.1:8000/ticker/aapl')
response = json.loads(res.text)
print(response)