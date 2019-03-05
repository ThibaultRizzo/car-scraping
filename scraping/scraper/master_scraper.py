from bs4 import BeautifulSoup
import requests
from django.db import IntegrityError

from scraping.scraper.models import Vendor
from scraping.scraper.app_dictionaries import (vendorDict, ParsingRule)
from scraping.models import Car

import concurrent.futures


def scrap():
    # Iterate on all of the websites
    # for each website, call car = scrapInfo()
    # so for each field of the car, call a dictionary that links it to a WordRef
    carRef = CarRef(dict_areva)
    car = carRef.getCar()
    # print(car.reg_date)
    car.save()


vendorList = (
    Vendor('aramisAuto', 'https://www.aramisauto.com',
           'https://www.aramisauto.com/achat/page=%d', 0, 'vehicle-info-link'),
    # Vendor('carvana', 'https://www.carvana.com', 'https://www.carvana.com/cars?page=%d',
    #        1, 'SingleClickLink__StyledLink-sc-1455iy6-0 cnENNQ'),
    # Vendor('lacentrale', 'https://www.lacentrale.fr',
    #        'https://www.lacentrale.fr/listing?page=%d', 0, 'linkAd')
)

URL_PAGE_LIMIT = 1

http = "http://3.17.154.4:8080"
https = "https://3.17.154.4:8080"
ftp = "ftp://10.10.1.10:8080"

proxy_dict = {
    "http": http,
    "https": https,
    "ftp": ftp
}


def scrapAllWebsites():
    # Clear all instances from the Car table
    Car.objects.delete_everything()

    # Iterates on all websites URL search pages
    for vendor in vendorList:
        # Get list of all car URLs
        urlList = getListOfAllUrls(vendor)
        print(list(urlList))
        with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
            # Iterates over list of urls
            for url in urlList:
                executor.submit(getAndSaveCar, url)
            print("Vendor %s has %d urls" % (vendor.name, len(urlList)))


def getAndSaveCar(url):
    # Get the Car class from each url
    car = getCarFromUrl(url, vendor.vendor_dictionary)
    car.save()


def getListOfAllUrls(vendorInfo):
    urlList = []
    it = vendorInfo.basePageNb
    while it < URL_PAGE_LIMIT:
        print(vendorInfo.searchUrl % it)
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
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # For each field, get the corresponding rule
        scrapedCar = Car()
        for key in scrapedCar.__dict__:
            # Get value with given dictionary
            if key in vendor_dict:
                value = vendor_dict[key].parseValue(soup)
                setattr(scrapedCar, key, value)
        scrapedCar.vendor_link = url
        return scrapedCar
    # If anything went wrong, we log and move on
    except:
        print("The following URL could not be parsed: " + url)
        pass
