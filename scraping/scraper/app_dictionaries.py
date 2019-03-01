# from scraping.scraper.models2 import ParsingRule
# from scraping.models import Car
from .utils import (parseStrToDate, cleanInt, getNthElem,
                    getBreadCrum, getKilometers)
from enum import Enum


class Rule(Enum):
    SELF_ELEM = 'SELF_ELEM'
    NEXT_ELEM = 'NEXT_ELEM'
    PREVIOUS_ELEM = 'PREVIOUS_ELEM',
    AS_TAG = 'AS_TAG',
    NONE = 'NONE'


class ParsingRule:

    def __init__(self, id_, class_name, tag_, custom_lambda, rule):
        self.id_ = id_
        self.class_ = class_name
        self.tag_ = tag_
        self.custom_lambda = custom_lambda
        self.rule = rule

    def parseValue(self, soup):
        if self.rule == Rule.SELF_ELEM:
            # elem = soup.find(id=self.id_, class_=self.class_, tag_)
            # return self.rule(elem)
            print(1)
        elif self.rule == Rule.NEXT_ELEM:
            elem = soup.find(self.tag_, class_=self.class_).find_next()
            return self.custom_lambda(elem)
        elif self.rule == Rule.AS_TAG:
            elem = soup.find(id=self.id_, class_=self.class_)
            return self.custom_lambda(elem)
        elif self.rule == Rule.NONE:
            print('skip')


# Check permissions to scrap this data
URL = "https://occasion.elite-auto.fr/annonce-occasion-renault-captur,212838.html"

vendorDict = {
    'aramisAuto': {
        'price': ParsingRule("price-total", 'price-tag__number', None, lambda arg: float(arg['data-price']), Rule.AS_TAG),
        'km_number': ParsingRule(None, 'offer-car__model', None, getKilometers, Rule.AS_TAG),
        'brand': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 2), Rule.AS_TAG),
        'model': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 3), Rule.AS_TAG),
        'car_type': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 4), Rule.AS_TAG),
        'vendor': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 0), Rule.AS_TAG),
        'reg_date': ParsingRule(None, 'far far-route', 'span', lambda date: parseStrToDate(date.contents[2].strip()), Rule.NEXT_ELEM),
        'gear_box': ParsingRule(None, 'far far-boite', 'span', lambda arg: arg.contents[0].strip(), Rule.NEXT_ELEM),
        'gear_number': ParsingRule(None, 'far far-boite', 'span', lambda arg: arg.contents[2].strip(), Rule.NEXT_ELEM),
        'motor_type': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[2].strip(), Rule.NEXT_ELEM),
        'petrol_type': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NEXT_ELEM),
        'color': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
        'doors_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
        'vendor_link': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
        'vendor_ref': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
        'owner_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
        'reg_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
        'created': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), Rule.NONE),
    },
    'elite-auto': {
        # 'price': ParsingRule("span", 'price', None, lambda w: int(w[:-1].replace(" ", "")), URL),
        # 'km_number': ParsingRule("span", 'item-value', 'Kilométrage', lambda w: int(w[:-2]), URL),
        # 'brand': ParsingRule("span", 'model', None, lambda w: w + '', URL),
        # 'model': ParsingRule("span", 'modelExtend', None, lambda w: w + '', URL),
        # 'reg_date': ParsingRule("span", 'item-value', 'Mise en circulation', parseStrToDate, URL),
    },
    'lacentrale': {
        # 'price': ParsingRule("span", 'price', None, lambda w: int(w[:-1].replace(" ", "")), URL),
        # 'km_number': ParsingRule("span", 'item-value', 'Kilométrage', lambda w: int(w[:-2]), URL),
        # 'brand': ParsingRule("span", 'model', None, lambda w: w + '', URL),
        # 'model': ParsingRule("span", 'modelExtend', None, lambda w: w + '', URL),
        # 'reg_date': ParsingRule("span", 'item-value', 'Mise en circulation', parseStrToDate, URL),
    }
}


def getDictionary(vendorName):
    # TODO: Throw exception if no dictionary was found
    return vendorDict[vendorName]
