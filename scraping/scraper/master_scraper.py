from django.db import IntegrityError
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup
import concurrent.futures
import requests
import time

from scraping.scraper.models import Vendor
from scraping.scraper.app_dictionaries import (vendorDict, ParsingRule)
from scraping.models import Car
from carstatistic.models import CarStatistic, CarStatisticTitle


URL_PAGE_LIMIT = 20

http = "http://3.17.154.4:8080"
https = "https://3.17.154.4:8080"
ftp = "ftp://10.10.1.10:8080"

vendorList = (
    Vendor('goodbuyauto.it', 'https://www.goodbuyauto.it', 'https://www.goodbuyauto.it/compra?page=%d',
           1, lambda soup: map(lambda arg: arg.find('a'), soup.find_all(
               class_="carsmall_container catalog"))),
    Vendor('lacentrale', 'https://www.lacentrale.fr', 'https://www.lacentrale.fr/listing?page=%d',
           0, lambda soup: soup.find_all('a', class_='linkAd')),
    Vendor('aramisAuto', 'https://www.aramisauto.com',
           'https://www.aramisauto.com/achat/?page=%d', 0, lambda soup: soup.find_all('a', class_='real-link vehicle-info-link')),
    # Vendor('carvana', 'https://www.carvana.com', 'https://www.carvana.com/cars?page=%d',
    #        1, 'SingleClickLink__StyledLink-sc-1455iy6-0 cnENNQ'),
)

proxy_dict = {
    "http": http,
    "https": https,
    "ftp": ftp
}


def scrapAllWebsites():
    start = time. time()  # Used to measure time of execution
    # Clear all instances from the Car table
    print('Starting the scraping process...')
    Car.objects.delete_everything()
    print('Car table cleared...')

    # Iterates on all websites URL search pages
    for vendor in vendorList:
        # Get list of all car URLs
        urlList = getListOfAllUrls(vendor)
        print("****** Vendor %s, Size of url list: %d" %
              (vendor.name, len(urlList)))
        # with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        # Iterates over list of urls
        carList = []
        # executor.map(lambda url: carList.append(getCarFromUrl(
        #     url, vendor.vendor_dictionary)), urlList)
        for url in urlList:
            car_scraped = getCarFromUrl(url, vendor)
            # Need to validate the model before including it to the list
            try:
                car_scraped.full_clean()
            except ValidationError as e:
                # Do something based on the errors contained in e.message_dict.
                # Display them to a user, or handle them programmatically.
                print(
                    "Skipping this URL: %s because the scraped car is missing some fields" % url, e)
                continue
            carList.append(car_scraped)
        # executor.submit(getAndSaveCar, url, vendor)
        # print(*carList, sep=", ")
        Car.objects.save_as_batch(carList)

    CarStatistic.objects.processCarStatistics((
        CarStatisticTitle.NB_REF_CAR,
        CarStatisticTitle.NB_RTL,
        CarStatisticTitle.AVG_CAR_PRC
    ))
    end = time. time()
    print("Scraping operation took %d seconds to complete" % (end - start))


def getAndSaveCar(url, vendor):
    # Get the Car class from each url
    return getCarFromUrl(url, vendor.vendor_dictionary)


def getListOfAllUrls(vendorInfo):
    urlList = []
    it = vendorInfo.basePageNb
    while it <= URL_PAGE_LIMIT:
        r = requests.get(vendorInfo.searchUrl % it)
        soup = BeautifulSoup(r.text, 'html.parser')
        tmpAHrefList = vendorInfo.hrefLambda(soup)
        tmpList = map(lambda arg: vendorInfo.baseUrl +
                      arg['href'], tmpAHrefList)
        if tmpList is None:
            break
        urlList += tmpList
        it += 1
    return set(urlList)


# def getUrlList(urlList, vendorInfo, it):
#     print("Getting url")
#     r = requests.get(vendorInfo.searchUrl % it)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     tmpAHrefList = vendorInfo.hrefLambda(soup)
#     tmpList = map(lambda arg: vendorInfo.baseUrl +
#                   arg['href'], tmpAHrefList)
#     if tmpList is None:
#         return None
#     urlList += tmpList


def getCarFromUrl(url, vendor):
    # Scrap the URL
    vendor_dict = vendor.vendor_dictionary
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # For each field, get the corresponding rule
        scrapedCar = Car()
        for key in scrapedCar.__dict__:
            # Get value with given dictionary
            if key in vendor_dict:
                try:
                    value = vendor_dict[key].parseValue(soup)
                    setattr(scrapedCar, key, value)
                except:
                    print("The key %s was not found on url %s" % (key, url))
                    setattr(scrapedCar, key, None)
        scrapedCar.vendor_link = url
        scrapedCar.vendor = vendor.name
        return scrapedCar
    # If anything went wrong, we log and move on
    except:
        print("An error happened for url %s" % url)
        pass
