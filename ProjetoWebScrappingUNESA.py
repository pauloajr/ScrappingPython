import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = "https://portal.estacio.br/plantaocoronavirus/atendimento-remoto"
headers = {'User-Agent': 'Mozilla/5.0'}

def tratamentHTML(html):
    return " ".join(html.split()).replace("> <", "><")

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()

    html = html.decode("utf-8")
    html = tratamentHTML(html)

    soup = BeautifulSoup(html, 'html.parser')

    setor = soup.find("div", id="basicsAccordion")

    nomes = setor.findAll("div", class_="card-header card-collapse__header")
    
    for nome in nomes:
        print(nome.getText())


except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)