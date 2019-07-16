import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.aonprd.com/Corruptions.aspx?ItemName=Abolethn')
c = res.content


soup = BeautifulSoup(c)


print(soup.select('h1.title'))
