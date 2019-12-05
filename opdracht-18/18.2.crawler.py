from bs4 import BeautifulSoup
import requests

output_file = open("tor_links.txt", "w")

req = requests.get("https://onion.live/")
content = req.text
soup = BeautifulSoup(content, 'html.parser')
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if ".onion" in href:
        output_file.write(href + "\n")

output_file.close()
print("Done, saved {} links".format(counter))
