import requests
url="https://ataturk.now.sh/en"
response=requests.get(url)
data=response.json()
print(data)
