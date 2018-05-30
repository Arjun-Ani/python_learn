import requests
import urllib2
from bs4 import BeautifulSoup
from lxml import html
e=0
f=0
link ="http://www.XXXXXXX.com/index.php?BackStructure=6"
response=requests.get(link)
page=html.fromstring(response.content)
#b=element.cssselect("[va]")
print page
x = page.xpath("///div[contains(@class,'product-block')]")
a=[]
b=[]
for i in x:
    y = i.xpath("///div[contains(@class,'product-meta clearfix')]/h6/a")
    z = i.xpath("///span[contains(@id,'normalPrice')]")
    for j in y:
      print j.text
        #  a.append(j.text)
      e=e+1
    for k in z:
       # b.append(k.text)
        f=f+1

#print a
#print b
#print e
#print f
# print i.text
#content=r.text
#soup = BeautifulSoup(content,'html.parser')
#title = soup.find_all('h6', attrs={'class': 'name'})
#title1 = soup.find_all('div')
#title1 = soup.find_all('span')
#print title1.span
#for i in title:
#    print i.a.text
#for j in title1:
#    print j.text
