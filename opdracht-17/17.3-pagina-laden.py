import requests

response = requests.get("https://www.tweakers.net/")
content = response.text
print(content)
