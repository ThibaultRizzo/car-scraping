import requests
import re
from bs4 import BeautifulSoup
from scraping.models import Car
from scraping.scraper.app_dictionaries import getDictionary


class Vendor:
    def __init__(self, name, baseUrl, searchUrl, basePageNb, hrefClass):
        self.name = name
        self.baseUrl = baseUrl
        self.searchUrl = searchUrl
        self.basePageNb = basePageNb
        self.hrefClass = hrefClass
        self.vendor_dictionary = getDictionary(name)
