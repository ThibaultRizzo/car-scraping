from bs4 import BeautifulSoup
import requests

from scraping.scraper.models import Vendor
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


vendorList = (Vendor('aramisAuto', 'https://www.aramisauto.com', 'https://www.aramisauto.com/achat/page=%d', 0, 'vehicle-info-link'),
              Vendor('elite-auto', 'https://recherche.elite-auto.fr',
                     'https://recherche.elite-auto.fr/?p=%d', 1, 'visuel-prod'),
              Vendor('lacentrale', 'https://www.lacentrale.fr',
                     'https://www.lacentrale.fr/listing?page=%d', 0, 'linkAd')
              )

URL_PAGE_LIMIT = 1


def scrapAllWebsites():
    # Iterates on all websites URL search pages
    for vendor in vendorList:
        # Get list of all car URLs
        urlList = getListOfAllUrls(vendor)

        # Iterates over list of urls
        for url in urlList:
            # Get the Car class from each url
            car = getCarFromUrl(url, vendor.vendor_dictionary)
            car.save()
        print("Vendor %s has %d urls" % (vendor, len(urlList)))


def getListOfAllUrls(vendorInfo):
    urlList = []
    it = vendorInfo.basePageNb
    while it < URL_PAGE_LIMIT:
        r = requests.get(vendorInfo.searchUrl % it)
        soup = BeautifulSoup(r.text, 'html.parser')
        tmpList = map(lambda arg: vendorInfo.baseUrl + arg['href'],
                      soup.find_all('a', class_=vendorInfo.hrefClass))
        if tmpList is None:
            break
        urlList += tmpList
        it += 1
    return urlList


def getCarFromUrl(url, vendor_dict):
    # Scrap the URL
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # For each field, get the corresponding rule
    scrapedCar = Car()
    for key in scrapedCar.__dict__:
        # Get value with given dictionary
        if key in vendor_dict:
            value = vendor_dict[key].parseValue(soup)
            setattr(scrapedCar, key, value)
    return scrapedCar
    # If anything went wrong, we log and move on
