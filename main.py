from bs4 import BeautifulSoup as BS
import requests
p = 0
r0 = requests.get('https://www.olx.ua/d/uk/list/q-iphone-mini-12/?page=')
soup0 = BS(r0.content, 'html.parser')
buylist0 = soup0.findAll('a', class_="css-rc5s2u")
for buy0 in buylist0:
    ref0 = buy0["href"]
    n0 = buy0.text
    buyref0 = ('https://www.olx.ua' + ref0)
    print((n0)[:-11])
    print('-------------')
    print(buyref0)
    print('-------------')
    print('current page = 1')
    print('=============')
while True:
    url = ('https://www.olx.ua/d/uk/list/q-iphone-mini-12/?page=' + str(p))
    r = requests.get(url)
    soup = BS(r.content, 'html.parser')
    buylist = soup.findAll('a', class_="css-rc5s2u")
    if (len(buylist)):
        for buy in buylist:
                ref = buy["href"]
                n = buy.text
                buyref = ('https://www.olx.ua' + ref)
                print((n)[:-11])
                print('-------------')
                print(buyref)
                print('-------------')
                print('current page = ' + str(p))
                print('=============')
    p += 1
    if p == 26:
        break

