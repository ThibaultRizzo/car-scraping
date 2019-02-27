from datetime import datetime
from django.test import TestCase

# Create your tests here.

import re
import requests
from bs4 import BeautifulSoup

URL = "https://occasion.elite-auto.fr/annonce-occasion-renault-captur,212838.html"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
el = soup.find(text=re.compile("Mise en circulation")
               ).findNext('span').get_text()
print(el)


d = datetime.strptime(el, '%d/%m/%Y')

print(d)
