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

    # SOUP.HTML EQUIVALE find('html')
    # print(soup.title)
    # soup.html.head.title === soup.title
    print(soup.title.get_text())
    # <title>ESSE TEXTO</title> .get_text()
    print(soup.h5.getText())
    # <h5> <p> <div> ESSE TEXTO .getText()
    
    # soup.get_text(separator=' || ', strip=True)



    #Com este tipo de tratamento, podemos gerar uma lista com o conteúdo de cada tag explorada. Para isto, basta acrescentar, ao final do código acima, o método split(' || '):

except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
