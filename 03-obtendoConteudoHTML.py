from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = "https://alura-site-scraping.herokuapp.com/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.alura.com.br/"

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    print(html)
except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)
