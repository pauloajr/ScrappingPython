from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


def tratamentHTML(html):
    return " ".join(html.split()).replace("> <", "><")

url = "https://alura-site-scraping.herokuapp.com/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    # print(type(html))
    #byte para string
    html = html.decode("utf-8")
    # print(type(html))

    #eliminando os caracteres de estabulacao, quebra de linha, etc
    # print(tratamentHTML(html))

    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.img)
    # ira colocar as imagens
    #print(soup.img.attrs)
    # ira pegar os atributos
    soup.img.attrs.keys() #pega as chaves
    soup.img.attrs.values() #pega os valores

    # soup.img.attrs['src']
    print(soup.img['src']) # a mesma coisa soup.img.get('src')

    

except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
