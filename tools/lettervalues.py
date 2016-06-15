import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def count(message, extras=dict(), offset=0, direction='1', includeNumerics=False):
    message = message.lower()
    extras = cleanExtras(extras)
    totalSigns = len(message)
    relevantSigns = 0
    totalValue = 0
    if includeNumerics:
        extras.update(_getNumericDict())
    
    for char in message:
        value = getValue(char, extras, offset, direction)
        totalValue += value
        if value != 0:
            relevantSigns += 1
    
    return {'totalSigns':totalSigns, 'relevantSigns':relevantSigns, 'totalValue':totalValue}

def extractExtrasDict(extras):
    result = dict()
    if len(extras) == 0:
        return result
    split = re.split('\r\n|\n',extras)
    for extra in split:
        splEx = extra.split(':=')
        if len(splEx) == 2 and len(splEx[0]) == 1 and len(splEx[1]) > 0:
            res = re.search('^[-]?[0-9]+$', splEx[1])
            if res != None and len(res.group(0)) > 0:
                result[splEx[0]] = int(splEx[1])

    return result

def _getNumericDict():
    numerics = dict()
    for count in range(0, 10):
        numerics[str(count)] = count
    return numerics

def getValue(sign, extras, offset, direction):
    value = ALPHABET.find(sign) + 1
    if value > 0:
        value += offset
        if direction == '2':
            value = 27 - value
        return value
    elif sign in extras:
        return extras[sign]
    else:
        return 0
    
def cleanExtras(extras):
    cleanExtra = dict()
    for extra in extras.items():
        if len(extra[0]) == 1 and type(extra[1]) == int:
            cleanExtra[extra[0]] = extra[1]
    return cleanExtra
