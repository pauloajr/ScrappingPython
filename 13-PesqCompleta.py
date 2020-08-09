
from urllib.request import Request, urlopen, urlretrieve
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd


def uri(numero):
    if numero == "" or numero == "1":
        return "https://alura-site-scraping.herokuapp.com/index.php"
    else:
        return "https://alura-site-scraping.herokuapp.com/index.php?page=" + str(numero)

url = "https://alura-site-scraping.herokuapp.com/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}


def exportarCard(anuncio):
    card = {}
    valor = anuncio.find('p', class_="txt-value").getText()

    # valor
    card['value'] = valor
    
    # informacao
    infos = anuncio.find('div', {"class": "body-card"}).findAll('p')
    for info in infos:
        card[info.get('class')[0].replace("txt-","")] = info.get_text()

    items = anuncio.find('div', {"class": "body-card"}).ul.findAll('li', class_="txt-items")
    items.pop()

    acessorios = []

    for item in items:
        acessorios.append(item.get_text().replace("► ",""))

    card['items'] = acessorios    

    photo = anuncio.find('img', alt='Foto').get('src')
    nomePhoto = './img/' + photo.split('/')[-1]
    # print(nomePhoto)

    urlretrieve(photo, nomePhoto)

    card['image'] = nomePhoto

    # print(card)

    return card


try:
    cards = []

    for i in range(1,26):
        print(i)
        req = Request(uri(i), headers=headers)
        response = urlopen(req)
        html = response.read()
        html = html.decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')

        anuncios = soup.find('div', {'id': 'container-cards'}).findAll('div', class_="card")

        for anuncio in anuncios:
            cards.append(exportarCard(anuncio))

    dataset = pd.DataFrame(cards)
    dataset.to_csv('./tabela.csv', sep=';', index = False, encoding = 'utf-8-sig')
    print(dataset)
    
  

except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
