
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd


url = "https://alura-site-scraping.herokuapp.com/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    cards = []
    card = {}

    # pesq = soup.find('div', {"class":"value-card"}).getText()
    # print(pesq)

    anuncio = soup.find('div', {"class":"well card"})
    valor = anuncio.find('p', class_="txt-value").getText()
    card['value'] = valor
    
    infos = anuncio.find('div', {"class": "body-card"}).findAll('p')
    
    # separar em vetores e pegar o ultimo array
    # info.get('class')[0].split('-')[-1]

    for info in infos:
        card[info.get('class')[0].replace("txt-","")] = info.get_text()

    items = anuncio.find('div', {"class": "body-card"}).ul.findAll('li', class_="txt-items")
    items.pop()

    acessorios = []

    for item in items:
        acessorios.append(item.get_text().replace("► ",""))

    card['items'] = acessorios    

    # dataset = pd.DataFrame(card)
    dataset = pd.DataFrame.from_dict(card, orient = 'index').T
    # exportando em csv
    # dataset.to_csv('caminho', sep=';', index = False, encoding = 'utf-8-sig')
    print(dataset)



    
  

except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
