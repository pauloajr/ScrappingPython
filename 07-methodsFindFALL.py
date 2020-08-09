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
    
    # soup.img === soup.find('img')

    # Passando uma lista de argumentos de TAGS
    lista = soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5'])
    # ele vai pesquisar os 5

    # Pesquisando utilizando atributos como argumento
    todosOsP = soup.findAll('p', {"class":"nome da class"})

    #Pesquisando pelo valor da TAG 
    pesq = soup.findAll('p', text = "Belo Horizonte - MG")

    #Utilizando diretamente os atributos
    pesq = soup.findAll('img', alt="Foto") #id=""

    for i in pesq:
        #print(i.get('src'))
        i.get('src')


    # Pesquisando o metodo classes
    pesq = soup.findAll('p', class_="nome da class")


    # Obtendo todo o conteudo de uma pagina
    pesq = soup.findAll(text = True)
    print(pesq)

except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
