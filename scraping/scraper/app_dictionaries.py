from .models import WordRef
from .utils import (joinString, parseStrToDate)


# Check permissions to scrap this data
URL = "https://occasion.elite-auto.fr/annonce-occasion-renault-captur,212838.html"

dict_areva = {
    'price': WordRef("span", 'price', None, lambda w: int(w[:-1].replace(" ", "")), URL),
    'km_number': WordRef("span", 'item-value', 'Kilométrage', lambda w: int(w[:-2]), URL),
    'brand': WordRef("span", 'model', None, lambda w: w + '', URL),
    'model': WordRef("span", 'modelExtend', None, lambda w: w + '', URL),
    'reg_date': WordRef("span", 'item-value', 'Mise en circulation', parseStrToDate, URL),
}
