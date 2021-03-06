from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def tratamentHTML(html):
    return " ".join(html.split()).replace("> <", "><")

url = "https://alura-site-scraping.herokuapp.com/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    # print(html)
    #byte para string
    html = html.decode("utf-8")

    #vamos colocar tudo para uma lista
    print(html.split())

    # string
    # print(type(html))

    #eliminando os caracteres de estabulacao, quebra de linha, etc
    print(tratamentHTML(html))
except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
