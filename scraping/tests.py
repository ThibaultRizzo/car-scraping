from datetime import datetime
from django.test import TestCase

# Create your tests here.

import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.aramisauto.com/voitures/chevrolet/captiva/ltz/rv334964"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
# el = soup.find(text=re.compile("Mise en circulation")
#                ).findNext('span').get_text()
el = soup.find(id="price-total").get_text()
# el = soup.find('span', class_='far far-boite').find_next().contents[2].strip()


# print(filterel(' ', ''))
print(el)
# print(int("".join(filter(lambda x: x.isdigit(), el))))


# d = datetime.strptime(el, '%d/%m/%Y')
dico = {'el': 'elo'}
if 'id' not in dico:
    print(dico['id'])
else:
    print('Nop')
# print(d)
