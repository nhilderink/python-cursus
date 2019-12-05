from bs4 import BeautifulSoup
import requests

output_file = open("tor_links.txt", "w")
url = "https://onion.live/?page="

for i in range(10):
    print("Load page {}".format(i))
    req = requests.get(url.format(i))

    content = req.text
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if ".onion" in href:
            print(href)
            output_file.write(href + "\n")

output_file.close()
print("Done")
