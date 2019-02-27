from scraping.scraper.models import CarRef
from scraping.scraper.app_dictionaries import (dict_areva)
from scraping.models import Car


def scrap():
    # Iterate on all of the websites
    # for each website, call car = scrapInfo()
    # so for each field of the car, call a dictionary that links it to a WordRef
    carRef = CarRef(dict_areva)
    car = carRef.getCar()
    # print(car.reg_date)
    car.save()
