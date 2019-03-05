from datetime import datetime
from django.test import TestCase

# Create your tests here.

import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.goodbuyauto.it/compra?page=20"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
# el = soup.find(text=re.compile("Mise en circulation")
#                ).findNext('span').get_text()
el = soup.find_all('div', class_='carsmall_container catalog' )

lambdaClass = 'carsmall_container catalog'
list_el = list(map(lambda arg: arg.find('a'), soup.find_all(class_=lambdaClass)))

#print (list_el)

hrefLambda = lambda lambdaClass,soup: list(map(lambda arg: arg.find('a'), soup.find_all(class_=lambdaClass)))

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

print(cleanInt(soup.find('p', class_="t-small",string='Chilometri').find_next().get_text()))
# list_el= soup.find_all('a', class_='linkAd')
# print(list_el)


# el = soup.find('span', class_='far far-boite').find_next().contents[2].strip()


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

