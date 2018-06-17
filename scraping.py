import requests
from bs4 import BeautifulSoup
url='https://www.nytimes.com/'
r=requests.get(url)
a=r.text
soup = BeautifulSoup(a,"html.parser")
title = soup.find('span', 'articletitle').string
