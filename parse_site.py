from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('https://gorodarus.ru/goroda-po-alfavitu.html').read()
soup = BeautifulSoup(response, 'lxml')
for row in soup.find_all('td'):
    print(row)

