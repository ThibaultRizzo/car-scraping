from django.test import TestCase

import re
import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://35.247.109.63:80',
    'https': 'https://134.209.108.146:31330',
}
URL = "https://www.goodbuyauto.it/compra/nissan-x-trail-1-6-dci-2wd-acenta-usata/1598374"
# r = requests.get(URL)
# soup = BeautifulSoup(r.text, 'html.parser')
# el = soup.find(string=re.compile("<!-- GOOGLE -->"))
# el2 = re.search(r"'name': '(.*?)'", el).group(1)


print("sdfg sdfgh serty345sdf".title())
