# from scraping.scraper.models2 import ParsingRule
# from scraping.models import Car
from .utils import (parseStrToDate, cleanInt, getNthElem,
                    getBreadCrum, getRegDate, getKilometers, getChild, get_brand, get_model)
from enum import Enum
import re


class RuleName(Enum):
    SELF_ELEM = 'SELF_ELEM'
    NEXT_ELEM = 'NEXT_ELEM'
    PREVIOUS_ELEM = 'PREVIOUS_ELEM',
    AS_TAG = 'AS_TAG',
    AS_TEXT = 'AS_TEXT',
    AS_INPUT = 'AS_INPUT',
    FROM_TEXT = 'FROM_TEXT',
    NONE = 'NONE'


class ParsingRule:

    def __init__(self, id_, class_name, tag_, string_, custom_lambda, ruleName):
        self.id_ = id_
        self.class_ = class_name
        self.tag_ = tag_
        self.string_ = string_
        self.custom_lambda = custom_lambda
        self.ruleName = ruleName

    def parseValue(self, soup):
        try:
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
                elem = soup.find(self.tag_, class_=self.class_,
                                 string=self.id_).find_next()
                return self.custom_lambda(elem)
            elif self.ruleName == RuleName.AS_INPUT:
                elem = soup.find(self.tag_, {'name': self.class_, 'type': self.id_})[
                    'value']
                return self.custom_lambda(elem)
            elif self.ruleName == RuleName.FROM_TEXT:
                elem = soup.find(string=re.compile(self.string_))
                return self.custom_lambda(elem)
            elif self.ruleName == RuleName.NONE:
                return
        except:
            print("Something went wrong while retrieving the parsed value")
            raise


vendorDict = {
    'aramisAuto': {
        'price': ParsingRule("price-total", 'price-tag__number', None, None, lambda arg: float(arg['data-price']), RuleName.AS_TAG),
        'km_number': ParsingRule(None, 'offer-car__model', None, None, getKilometers, RuleName.AS_TAG),
        'brand': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, None, lambda arg: getBreadCrum(arg, 2), RuleName.AS_TAG),
        'model': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, None, lambda arg: getBreadCrum(arg, 3), RuleName.AS_TAG),
        'car_type': ParsingRule("wo-breadcrumbs", 'breadcrumb', None, None, lambda arg: getBreadCrum(arg, 4), RuleName.AS_TAG),
        'reg_date': ParsingRule(None, 'far far-route', 'span', None, lambda date: parseStrToDate(date.contents[2].strip()), RuleName.NEXT_ELEM),
        'gear_box': ParsingRule(None, 'far far-boite', 'span', None, lambda arg: getChild(arg, 0), RuleName.NEXT_ELEM),
        'gear_number': ParsingRule(None, 'far far-boite', 'span', None, lambda arg: getChild(arg, 2), RuleName.NEXT_ELEM),
        'motor_type': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: getChild(arg, 2), RuleName.NEXT_ELEM),
        'petrol_type': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: getChild(arg, 0), RuleName.NEXT_ELEM),
        # TODO: Define color
        'color': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: getChild(arg, 0), RuleName.NONE),
        'doors_number': ParsingRule(None, 'far far-porte', 'span', None, lambda arg: getChild(arg, 0), RuleName.NEXT_ELEM),
        'vendor_ref': ParsingRule(None, 'cta-favorite btn-favorite btn-favorite--disable', None, None, lambda arg: arg['data-vehicle-id'], RuleName.AS_TAG),
        'owner_number': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: getChild(arg, 0), RuleName.AS_TAG),
        'reg_number': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: getChild(arg, 0), RuleName.NONE),
    },
    'lacentrale': {
        'price': ParsingRule(None, 'cbm-price__newPrice', None, None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TAG),
        'km_number': ParsingRule('Kilométrage : ', 'optionLabel', 'span', None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TEXT),
        'brand': ParsingRule('hidden', 'brand', 'input', None, lambda arg: arg.lower(), RuleName.AS_INPUT),
        'model': ParsingRule('hidden', 'model', 'input', None, lambda arg: arg.lower(), RuleName.AS_INPUT),
        'car_type': ParsingRule('hidden', 'version', 'input', None, lambda arg: arg.lower(), RuleName.AS_INPUT),
        'reg_date': ParsingRule('Mise en circulation : ', 'optionLabel', 'span', None, lambda arg: parseStrToDate(arg.get_text()), RuleName.AS_TEXT),
        'gear_box': ParsingRule('Boîte de vitesse : ', 'optionLabel', 'span', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'gear_number': ParsingRule(None, None, None, None, lambda arg: arg.contents[0].strip(), RuleName.NONE),
        'motor_type': ParsingRule('Puissance din : ', 'optionLabel', 'span', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'petrol_type': ParsingRule('Énergie : ', 'optionLabel', 'span', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'color': ParsingRule('Couleur extérieure : ', 'optionLabel', 'span', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'doors_number': ParsingRule('Nombre de portes : ', 'optionLabel', 'span', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'vendor_ref':  ParsingRule(None, 'cbm-btn--1 cbm-btn__sellerLoc', None, None, lambda arg: arg['data-classified-id'], RuleName.AS_TAG),
        'owner_number': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: arg.contents[0].strip(), RuleName.NONE),
        'reg_number': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: arg.contents[0].strip(), RuleName.NONE),
    },
    'goodbuyauto.it': {
        'price': ParsingRule(None, 'text-head-2 text-weight-semibold', 'span', None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TAG),
        'km_number': ParsingRule('Chilometri', 't-small', 'p', None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TEXT),
        'brand': ParsingRule(None, 'text-weight-light car-text visible-xs', 'h1', '<!-- GOOGLE -->', lambda el: get_brand(el), RuleName.FROM_TEXT),
        'model': ParsingRule(None, 'text-weight-light car-text visible-xs', 'h1', '<!-- GOOGLE -->', lambda el: get_model(el), RuleName.FROM_TEXT),
        'car_type': ParsingRule('Allestimento', 't-small', 'p', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        # TODO : Convertir le mois en date
        'reg_date': ParsingRule('Immatricolazione', 't-small', 'p', None, lambda arg: getRegDate(arg), RuleName.AS_TEXT),
        'gear_box': ParsingRule('Cambio', 't-small', 'p', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'gear_number': ParsingRule('Marce', 't-small', 'p', None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TEXT),
        'motor_type': ParsingRule('Potenza', 't-small', 'p', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'petrol_type': ParsingRule('Alimentazione', 't-small', 'p', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'color': ParsingRule('Colore', 't-small', 'p', None, lambda arg: arg.get_text(), RuleName.AS_TEXT),
        'doors_number': ParsingRule('Porte', 't-small', 'p', None, lambda arg: cleanInt(arg.get_text()), RuleName.AS_TEXT),
        'vendor_ref':  ParsingRule('hidden', 'sku', 'input', None, lambda arg: arg.lower(), RuleName.AS_INPUT),
        'owner_number': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: arg.contents[0].strip(), RuleName.NONE),
        'reg_number': ParsingRule(None, 'far far-motorisation', 'span', None, lambda arg: arg.contents[0].strip(), RuleName.NONE),
    }
}


def getDictionary(vendorName):
    # TODO: Throw exception if no dictionary was found
    return vendorDict[vendorName]
