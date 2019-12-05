import requests
from bs4 import BeautifulSoup

request = requests.get("https://onion.live")
content = request.text

soup = BeautifulSoup(content, 'html.parser')
links = soup.find_all('a')

for link in links:
	print(link.get('href'))
