# from scraping.scraper.models2 import ParsingRule
# from scraping.models import Car
from .utils import (parseStrToDate, cleanInt, getNthElem,
                    getBreadCrum, getKilometers, getChild, CleanBrand)
from enum import Enum


class RuleName(Enum):
    SELF_ELEM = 'SELF_ELEM'
    NEXT_ELEM = 'NEXT_ELEM'
    PREVIOUS_ELEM = 'PREVIOUS_ELEM',
    AS_TAG = 'AS_TAG',
    AS_TEXT = 'AS_TEXT',
    NONE = 'NONE'


class ParsingRule:

    def __init__(self, id_, class_name, tag_, custom_lambda, ruleName):
        self.id_ = id_
        self.class_ = class_name
        self.tag_ = tag_
        self.custom_lambda = custom_lambda
        self.ruleName = ruleName

    def parseValue(self, soup):
        if self.ruleName == RuleName.SELF_ELEM:
            # elem = soup.find(id=self.id_, class_=self.class_, tag_)
            # return self.RuleName(elem)
            print(1)
        elif self.ruleName == RuleName.NEXT_ELEM:
            elem = soup.find(self.tag_, class_=self.class_).find_next()
            return self.custom_lambda(elem)
        elif self.ruleName == RuleName.AS_TAG:
            elem = soup.find(id=self.id_, class_=self.class_)
            return self.custom_lambda(elem)
        elif self.ruleName == RuleName.AS_TEXT:
            elem = soup.find(self.tag_, class_=self.class_,string=self.id_).find_next()
            return self.custom_lambda(elem)
        elif self.ruleName == RuleName.NONE:
            return


# Check permissions to scrap this data
URL = "https://occasion.elite-auto.fr/annonce-occasion-renault-captur,212838.html"

vendorDict = {
    'aramisAuto': {
        'price': ParsingRule("price-total", 'price-tag__number', None, lambda arg: float(arg['data-price']), RuleName.AS_TAG),
        'km_number': ParsingRule(None, 'offer-car__model', None, getKilometers, RuleName.AS_TAG),
        'brand': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 2), RuleName.AS_TAG),
        'model': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 3), RuleName.AS_TAG),
        'car_type': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 4), RuleName.AS_TAG),
        'vendor': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, lambda arg: getBreadCrum(arg, 0), RuleName.AS_TAG),
        'reg_date': ParsingRule(None, 'far far-route', 'span', lambda date: parseStrToDate(date.contents[2].strip()), RuleName.NEXT_ELEM),
        'gear_box': ParsingRule(None, 'far far-boite', 'span', lambda arg: getChild(arg, 0), RuleName.NEXT_ELEM),
        'gear_number': ParsingRule(None, 'far far-boite', 'span', lambda arg: getChild(arg, 2), RuleName.NEXT_ELEM),
        'motor_type': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: getChild(arg, 2), RuleName.NEXT_ELEM),
        'petrol_type': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: getChild(arg, 0), RuleName.NEXT_ELEM),
        # TODO: Define color
        'color': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: getChild(arg, 0), RuleName.NONE),
        'doors_number': ParsingRule(None, 'far far-porte', 'span', lambda arg: getChild(arg, 0), RuleName.NEXT_ELEM),
        'vendor_ref': ParsingRule(None, 'cta-favorite btn-favorite btn-favorite--disable', None, lambda arg: arg['data-vehicle-id'], RuleName.AS_TAG),
        'owner_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: getChild(arg, 0), RuleName.AS_TAG),
        'reg_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: getChild(arg, 0), RuleName.NONE),
    },
    'carvana': {
        # 'price': ParsingRule("span", 'price', None, lambda w: int(w[:-1].replace(" ", "")), URL),
        # 'km_number': ParsingRule("span", 'item-value', 'Kilométrage', lambda w: int(w[:-2]), URL),
        # 'brand': ParsingRule("span", 'model', None, lambda w: w + '', URL),
        # 'model': ParsingRule("span", 'modelExtend', None, lambda w: w + '', URL),
        # 'reg_date': ParsingRule("span", 'item-value', 'Mise en circulation', parseStrToDate, URL),
    },
    'lacentrale': {
        'price': ParsingRule(None, 'cbm-price__newPrice', None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TAG),
        'km_number': ParsingRule('Kilométrage : ', 'optionLabel', 'span', lambda arg: cleanInt(arg.get_text()), RuleName.AS_TEXT),
        'brand': ParsingRule(None, 'cbm-breadcrumb__list', None, lambda arg: CleanBrand(getBreadCrum(arg, 2)), RuleName.AS_TAG),
        'model': ParsingRule(None, 'cbm-breadcrumb__list', None, lambda arg: getBreadCrum(arg, 3), RuleName.AS_TAG),
        'car_type': ParsingRule(None, 'cbm-breadcrumb__list', None, lambda arg: getBreadCrum(arg, 3), RuleName.AS_TAG),
        'reg_date': ParsingRule('Mise en circulation : ', 'optionLabel', 'span', lambda arg: parseStrToDate(arg.get_text()), RuleName.AS_TEXT),
        'gear_box': ParsingRule('Boîte de vitesse : ', 'optionLabel', 'span', lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'gear_number': ParsingRule(None, None, None, lambda arg: arg.contents[0].strip(), RuleName.NONE),
        'motor_type': ParsingRule('Version : ', 'optionLabel', 'span', lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'petrol_type': ParsingRule('Énergie : ', 'optionLabel', 'span', lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'color': ParsingRule('Couleur extérieure : ', 'optionLabel', 'span', lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'doors_number': ParsingRule('Nombre de portes : ', 'optionLabel', 'span', lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'vendor_ref':  ParsingRule(None, 'cbm-btn--1 cbm-btn__sellerLoc', None, lambda arg: arg['data-classified-id'], RuleName.AS_TAG),
        'owner_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), RuleName.NONE),
        'reg_number': ParsingRule(None, 'far far-motorisation', 'span', lambda arg: arg.contents[0].strip(), RuleName.NONE),
    }
}


def getDictionary(vendorName):
    # TODO: Throw exception if no dictionary was found
    return vendorDict[vendorName]
