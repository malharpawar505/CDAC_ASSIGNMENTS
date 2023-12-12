
#Step1:
import requests
import html5lib
from bs4 import BeautifulSoup


#step2

req= requests.get("https://www.passiton.com/inspirational-quotes")
#print(req.content)

ggno
sp = BeautifulSoup(req.content,"html5lib")
#print(sp.prettify())


tbl= sp.find('div',attrs={'id':'all_quotes'})

#print(tbl)
rows= tbl.findAll('div',attrs={'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'})
cnt =0
for r in rows:
    cnt+=1
    print(cnt,". ",r.img["alt"].split('#')[0])
    print("----------------------------------")