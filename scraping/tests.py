from itertools import cycle
from lxml.html import fromstring
from datetime import datetime
from django.test import TestCase

# Create your tests here.

import re
import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://35.247.109.63:80',
    'https': 'https://134.209.108.146:31330',
}
URL = "https://www.carvana.com/cars?page=10"
url_test = 'https://httpbin.org/ip'
# response = requests.get(URL, proxies=proxies)
# print(response)
# r = requests.get(URL, proxies=proxies)
# soup = BeautifulSoup(r.text, 'html.parser')


# el = soup.find(text=re.compile("Mise en circulation")
#                ).findNext('span').get_text()
# el = soup.find()
# el = soup.find("span", class_="far far-boite").find_next().contents[0]
# el = soup.find('span', class_='far far-boite').find_next().contents[2].strip()


# print(filterel(' ', ''))
# print(soup)
# print(int("".join(filter(lambda x: x.isdigit(), el))))

req = requests.get(URL).text
print(req)


def get_proxies():
    # url = 'https://free-proxy-list.net/'
    us_url = 'https://www.us-proxy.org/'
    response = requests.get(us_url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


# proxies = get_proxies()
# proxy_pool = cycle(proxies)
# # url = 'https://httpbin.org/ip'
# for i in range(1, 11):
#     # Get a proxy from the pool
#     proxy = next(proxy_pool)
#     print(proxy)
#     print("Request #%d" % i)
#     try:
#         response = requests.get(URL, proxies={"http": proxy, "https": proxy})
#         print(list(response))
#         print(response.json())
#     except:
#         # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
#         # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
#         print("Skipping. Connnection error")
