from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas

url = "https://alura-site-scraping.herokuapp.com/hello-world.php"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
html = response.read()

#ID soup.find('h1', id='oid')

soup = BeautifulSoup(html, 'html.parser')

# resposta = soup.find_all("span",{"class":"card-curso__nome"})
# print(resposta[1].text)

#ID         soup.find('h1', id='oid')
# resposta = soup.find("strong", {"class":"pagina-categoria__nome"}).get_text()
# print(resposta)

resposta = soup.find('h1', {'class': 'sub-header'}).get_text()
print(resposta)