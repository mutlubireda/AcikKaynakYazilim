import requests
url = "https://hp-api.onrender.com/api/spells"
response = requests.get(url)
data = response.json()
print(data)