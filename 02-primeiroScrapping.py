from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas

url = "https://www.alura.com.br/"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
html = response.read()
print(html)