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
