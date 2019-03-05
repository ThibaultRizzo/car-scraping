import requests
import re
from bs4 import BeautifulSoup
from scraping.models import Car
from scraping.scraper.app_dictionaries import getDictionary


# class ParsingRule:

#     def __init__(self, id_, class_name, tag_, rule):
#         self.id_ = id_
#         self.class_ = class_name
#         self.tag_ = tag_
#         self.rule = rule

#     def parseValue(self, soup):
#         if self.rule == Rule.SELF_ELEM:
#             print(1)
#         elif self.rule == Rule.NEXT_ELEM:
#             print(2)


class Vendor:
    def __init__(self, name, baseUrl, searchUrl, basePageNb, hrefClass, hrefLambda):
        self.name = name
        self.baseUrl = baseUrl
        self.searchUrl = searchUrl
        self.basePageNb = basePageNb
        self.hrefClass = hrefClass
        self.hrefLambda = hrefLambda
        self.vendor_dictionary = getDictionary(name)


# class ParsingRule:

#     def __init__(self, id_, class_name, tag_, rule):
#         self.id_ = id_
#         self.class_ = class_name
#         self.tag_ = tag_
#         self.rule = rule

#     def parseValue(self, soup):
#         if self.rule == Rule.SELF_ELEM:
#             print(1)
#         elif self.rule == Rule.NEXT_ELEM:
#             print(2)

    # def getValue(self):
    #     r = requests.get(self.url)
    #     if r.status_code == 200:
    #         soup = BeautifulSoup(r.text, 'html.parser')
    #         if self.matchingStr is None:
    #             car_model = soup.find(self.el, class_=self.class_name)
    #         else:
    #             pre_car_model = soup.find(text=re.compile(self.matchingStr))
    #             car_model = pre_car_model.findNext(self.el)
    #         if car_model is not None:
    #             # print(self.parsing_rule(car_model.get_text()))
    #             return self.parsing_rule(car_model.get_text())
    #         else:
    #             return ""


# class CarRef:
#     def __init__(self, car_dict):
#         self.car_dict = car_dict

#     def getCar(self):
#         # TODO: Find a way to put the html in cache (use a dictionary/set to be checked first)
#         car = Car()
#         for key in self.car_dict.keys():
#             if key is not None:
#                 setattr(car, key, self.car_dict[key].value)
#         car.car_type = "ert"
#         car.vendor = "ert"
#         print(self.car_dict["reg_date"].value)
#         return car
