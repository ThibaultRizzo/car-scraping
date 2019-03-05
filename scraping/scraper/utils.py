from datetime import datetime
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


def isInList(l, index):
    if index < len(l):
        return l[index]
    else:
        return None


def getChild(arg, index):
    print (arg)
    tmp_list = arg.contents
    if isInList(tmp_list, index) is not None:
        return tmp_list[index].strip()
    else:
        return None
