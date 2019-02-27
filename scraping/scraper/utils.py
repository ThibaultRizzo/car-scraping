from datetime import datetime
# Utility methods


def joinString(w, list):
    l = w.split()
    res = ''
    for it in list:
        res = res + ' ' + l[it]
    return res[1::]  # Removes separator inserted during first iteration


def parseStrToDate(str):
    print("Date " + str)
    print(datetime.strptime(str, '%d/%m/%Y'))
    datetime.strptime(str, '%d/%m/%Y')
