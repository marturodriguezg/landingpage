import requests
payload = {'user': 'Maria', 'email': 'ma@gmail.com'}
rsp = requests.get('https://www.google.com.ar', params=payload)
print(rsp.status_code)
print(rsp.text)
print(rsp.json())
