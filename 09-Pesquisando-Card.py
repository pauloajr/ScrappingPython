from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


url = "https://alura-site-scraping.herokuapp.com/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    pesq = soup.findAll('div', {"class":"well card"})
    print(pesq)
    
    cards = []
    card = {}

except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
