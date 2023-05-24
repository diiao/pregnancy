import requests,json

# 'ssh -R6001:127.0.0.1:5000 -o ServerAliveInterval=60 -o ServerAliveCountMax=3 admin@yuxue0824.com'

headers = {'Content-Type': 'application/json'}
data = {'list': 1}
json_data = json.dumps(data)
r = requests.post('https://pregnancy.yuxue0824.com/article',headers=headers,data=json_data)

print(r.json())