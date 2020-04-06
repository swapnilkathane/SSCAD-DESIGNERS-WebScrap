import requests
from bs4 import BeautifulSoup

res=requests.get('https://sscad.github.io/')
soup=BeautifulSoup(res.text, 'html.parser')
soup.prettify()
product=soup.find_all('div',class_='portfolio-info')
#print(product)
print('List of products of SSCAD DESIGNERS is : ')
for i in product:
    print(i.h4.a.text)
Member=soup.find_all('div', class_='member')
print('Core team members in SSCAD DESIGNERS are  ')
#print(Member)
for j in Member:
    print(j.h4.text,end=" ")
    print(j.span.text)