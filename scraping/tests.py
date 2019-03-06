
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
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

url_soup = 'https://www.lacentrale.fr/auto-occasion-annonce-69104073258.html'
r = requests.get(url_soup)
soup = BeautifulSoup(r.text, 'html.parser')
# el = map(.find('a')['href'], soup.find_all(class_="carsmall_container catalog"))
# list_el = map(lambda arg: arg.find('a')['href'], soup.find_all(
#     class_="carsmall_container catalog"))
elem = soup.find(class_='g8qpqa-0 iYKarG')
# elem = soup.find('span', class_='g8qpqa-0 iYKarG',
#                              string=self.id_).find_next()
print(elem)

# response = requests.get(URL, proxies=proxies)
# print(response)
# r = requests.get(URL, proxies=proxies)
# soup = BeautifulSoup(r.text, 'html.parser')

URL = "https://www.goodbuyauto.it/compra?page=20"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
# el = soup.find(text=re.compile("Mise en circulation")
#                ).findNext('span').get_text()
el = soup.find_all('div', class_='carsmall_container catalog')

lambdaClass = 'carsmall_container catalog'
list_el = list(map(lambda arg: arg.find(
    'a'), soup.find_all(class_=lambdaClass)))

#print (list_el)


def hrefLambda(lambdaClass, soup): return list(
    map(lambda arg: arg.find('a'), soup.find_all(class_=lambdaClass)))


def cleanInt(str):
    '''
    Removes all non numeric characters from string, concatenates then parse the whole number to int
    '''
    clean_int_list = filter(lambda x: x.isdigit(), str)
    return int("".join(clean_int_list))


#print(list(map(lambda arg: 'hello' + arg['href'],hrefLambda(lambdaClass, soup))))

URL = "https://www.goodbuyauto.it/compra/ford-c-max-1-6-tdci-115cv-titanium-usata/2179942"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

# print(cleanInt(soup.find('p', class_="t-small",
#                          string='Chilometri').find_next().get_text()))
# list_el= soup.find_all('a', class_='linkAd')
# print(list_el)


# el = soup.find('span', class_='far far-boite').find_next().contents[2].strip()

# print(filterel(' ', ''))
# print(soup)
# print(int("".join(filter(lambda x: x.isdigit(), el))))


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
            print(proxy)
    return proxies

    # prox = Proxy()
    # prox.proxy_type = ProxyType.MANUAL
    # prox.http_proxy = "35.247.109.63:80"
    # prox.socks_proxy = "ip_addr:port"
    # prox.ssl_proxy = "ip_addr:port"

    # capabilities = webdriver.DesiredCapabilities.CHROME
    # prox.add_to_capabilities(capabilities)

    # driver = webdriver.Chrome(desired_capabilities=capabilities)

    # headers = {'Host': 'www.vignanam.org',
    #            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10',
    #            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #            'Accept-Language': 'en-US,en;q=0.5',
    #            'Accept-Encoding': 'gzip, deflate',
    #            'Connection': 'keep-alive',
    #            'Cookie': 'visid_incap_1642409=B+YoelHCSKKN5z/Phs0zXCsF9VsAAAAAQUIPAAAAAACXaWvcNDXdMzcOky/SvffB; incap_ses'
    #                      '_715_1642409=kyFvSyJuuBVpNuh+aTHsCSsF9VsAAAAAKV6TIWTPSZmb+mOZWeuNHA==',
    #            'Upgrade-Insecure-Requests': '1'}

    # session = IncapSession()
    # headers = {
    #     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    # }
    # response = session.get(URL, headers=headers, bypass_crack=True)

    # print(response.text)

    def getProxyUrl():
        proxies = get_proxies()
        proxy_pool = cycle(proxies)
        # # url = 'https://httpbin.org/ip'
        for i in range(1, 11):
            # Get a proxy from the pool
            proxy = next(proxy_pool)
            print(proxy)
            print("Request #%d" % i)
            try:
                response = requests.get(URL, headers=headers, proxies={
                                        "http": proxy, "https": proxy})
                print(response)
            except:
                # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
                # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
                print("Skipping. Connnection error")

    def setupSelenium(proxy):
        # PROXY = "%s:%d" % (ip, port)  # IP:PORT or HOST:PORT
        PROXY = proxy
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)

        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get(URL)

    def setupProxy(proxy):
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = proxy
        prox.socks_proxy = proxy
        prox.ssl_proxy = proxy

        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)

        return webdriver.Chrome(desired_capabilities=capabilities)

    # def testSelenium():

    #     driver = webdriver.Chrome()
    #     wait = WebDriverWait(driver, 10)
    #     driver.get(URL)

    #     for item in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".company-details"))):
    #         company_name = item.find_element_by_id("company-name-1").text
    #         ceo_name = item.find_element_by_id("ceo-name-1").text
    #         print(company_name, ceo_name)

    #     driver.quit()

    # testSelenium()

# # print(filterel(' ', ''))
# print(el)
# # print(int("".join(filter(lambda x: x.isdigit(), el))))


# # d = datetime.strptime(el, '%d/%m/%Y')
# dico = {'el': 'elo'}
# if 'id' not in dico:
#     print(dico['id'])
# else:
#     print('Nop')
# # print(d)
