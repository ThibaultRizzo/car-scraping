import requests
import re
from bs4 import BeautifulSoup
from scraping.models import Car


class WordRef:
    def __init__(self, el, class_name, matchingStr, parsing_rule, url):
        self.url = url
        self.el = el
        self.class_name = class_name
        self.parsing_rule = parsing_rule
        self.matchingStr = matchingStr
        self.value = self.getValue()

    def getValue(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            if self.matchingStr is None:
                car_model = soup.find(self.el, class_=self.class_name)
            else:
                pre_car_model = soup.find(text=re.compile(self.matchingStr))
                car_model = pre_car_model.findNext(self.el)
            if car_model is not None:
                # print(self.parsing_rule(car_model.get_text()))
                return self.parsing_rule(car_model.get_text())
            else:
                return ""


class CarRef:
    def __init__(self, car_dict):
        self.car_dict = car_dict

    def getCar(self):
        # TODO: Find a way to put the html in cache (use a dictionary/set to be checked first)
        car = Car()
        for key in self.car_dict.keys():
            if key is not None:
                setattr(car, key, self.car_dict[key].value)
        car.car_type = "ert"
        car.vendor = "ert"
        print(self.car_dict["reg_date"].value)
        return car
