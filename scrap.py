<<<<<<< HEAD
import urllib2
from bs4 import BeautifulSoup
import re
from lxml import etree

print "Non Cuban"
quote_page ='http://www.puroexpress.com/Online_Shop/Service/Engine/OrderBy/Avail.Price/PrCategoryLink/134'
page = urllib2.urlopen(quote_page)
doc = etree.fromstring(page, parser=etree.HTMLParser())
x = doc.xpath("//span[contains('@id', 'normalPrice')]")
print x
#soup = BeautifulSoup(page, 'html.parser')
#price_box = soup.find_all('h6', attrs={'class':'name'})
#price_bo = soup.find_all(re.compile("normalPrice[0-9]*"))
#htmlparser = etree.HTMLParser() 
#tree = etree.parse(page, htmlparser) 
#x = tree.xpath("//span[contains('@id', 'normalPrice')]")
#td_empformbody = CSSSelector('span')
#print td_empformbody(tree)
#print x
#for i in price_box:
#	print i.a.text
#for j in price_bo:
#	print j.text
=======
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
>>>>>>> d0066f9765fc3c611c5ba58c3cbe2874e7ae5c88
