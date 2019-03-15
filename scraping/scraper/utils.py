from datetime import datetime
import re
# Utility methods


def joinString(w, list):
    l = w.split()
    res = ''
    for it in list:
        res = res + ' ' + l[it]
    return res[1::]  # Removes separator inserted during first iteration


def parseStrToDate(str):
    datetime.strptime(str, '%d/%m/%Y')


def cleanInt(str):
    '''
    Removes all non numeric characters from string, concatenates then parse the whole number to int
    '''
    clean_int_list = filter(lambda x: x.isdigit(), str)
    return int("".join(clean_int_list))


def getNthElem(elem, index, separator):
    return elem.get_text().split(separator)[index]


def getBreadCrum(elem, index):
    tmp = elem.contents[index].get_text()
    if tmp[-1] == "/":
        return tmp[:-1]
    else:
        return tmp


def getKilometers(elem):
    v = isInList(elem.contents, 3)
    if v is not None:
        return cleanInt(getNthElem(v, 1, '-'))
    else:
        return 0


def get_brand(elem):
    return re.search(r"'brand': '(.*?)'", elem).group(1)


def get_model(elem):
    return re.search(r"'name': '(.*?)'", elem).group(1)


def getRegDate(elem):
    try:
        return parseStrToDate('01/01/'+str(cleanInt(elem.get_text())))
    except:
        print('Could not retrieve reg date from the following element', elem)
        return None


def isInList(l, index):
    if index < len(l):
        return l[index]
    else:
        return None


def getChild(arg, index):
    tmp_list = arg.contents
    if isInList(tmp_list, index) is not None:
        return tmp_list[index].strip()
    else:
        return None
