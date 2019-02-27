from bs4 import BeautifulSoup
import requests

from scraping.scraper.models import CarRef
from scraping.scraper.app_dictionaries import (vendorDict)
from scraping.models import Car


def scrap():
    # Iterate on all of the websites
    # for each website, call car = scrapInfo()
    # so for each field of the car, call a dictionary that links it to a WordRef
    carRef = CarRef(dict_areva)
    car = carRef.getCar()
    # print(car.reg_date)
    car.save()


vendorUrlList = {
    'aramisAuto': ('https://www.aramisauto.com/achat/page=%d', 0, 'vehicle-info-link'),
    'elite-auto': ('https://recherche.elite-auto.fr/?p=%d', 1, 'visuel-prod'),
    'lacentrale': ('https://www.lacentrale.fr/listing?page=%d', 0, 'linkAd')
}


def scrapAllWebsites():
    # Iterates on all websites URL search pages
    for vendor, vendorInfo in vendorUrlList.items():
        # Get list of all car URLs
        urlList = getListOfAllUrls(vendorInfo)

        # Iterates over list of urls
        for url in urlList:
            # Get the Car class from each url
            car = getCarFromUrl(url, vendor)
            car.save()
        print("Vendor %s has %d urls" % (vendor, len(urlList)))


def getListOfAllUrls(info):
    urlList = []
    it = info[1]
    while it < 20:
        r = requests.get(info[0] % it)
        soup = BeautifulSoup(r.text, 'html.parser')
        tmpList = soup.find_all('a', class_=info[2])
        if tmpList is None:
            break
        urlList += tmpList
        it += 1
    return urlList


def getCarFromUrl(url, vendor):
    # Scrap the URL
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # For each field, get the corresponding value
    # TODO: Change the logic of CarRef
    carRef = CarRef(vendorDict[vendor])
    return carRef.getCar()
