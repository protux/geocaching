###################################################
#                                                 #
# Rätselrunde in der Nähe des Raketenspezialisten #
#                                                 #
# GC5Q7WC, GC5Q7WN, GC5Q7WQ, GC5Q7WV,             #
# GC5Q7X4, GC5???9, GC5Q7XF, GC?????              #
# GC5Q7XN,                                        #
#                                                 #
###################################################
import hashlib, sys

letters = "abcdef"
INDICES_BY_RIDDLE = {
    "1":"20,23,35,7,32,22,2,14,21,35,39,11".split(","),
    "2":"3,12,5,20,29,21,6,15,2".split(","),
    "3":"16,20,17,4,15,8,3,13,14,32,3".split(","),
    "4":"17,3,21,26,31,32,5,7,39".split(","),
    "5":"6,8,15,21,3,24,29,33".split(","),
    "6":"11,28,19,10,9,18,8,37".split(","),
    "7":"22,17,10,18,38,32,3,5,35,36".split(","),
    "8":"1,7,15,9,21,13,4,3,25,11,33".split(","),
    "9":"7,38,1,21,34,6,3,10,11,32,13".split(",")
}
def hashText(text, hashAlg):
    text = text.encode("UTF-8")
    
    if "sha1" == hashAlg:
        text = hashlib.sha1(text)
    else:
        raise ValueError("algorithm %s is not supported yet." % hashAlg)
    
    return text.hexdigest()
    
def getValuesByIndices(hashedText, indices):
    values = []
    
    for index in indices:
        value = hashedText[int(index) - 1]
        letterIndex = letters.find(value)
        if letterIndex > -1:
            value = str(letterIndex + 1)
        values += [value]
            
    return values
    
def calculateCoords(riddleIndex, resultDict):
    if riddleIndex == '1':
        return calculateRiddle1(resultDict)
    elif riddleIndex == '2':
        return calculateRiddle2(resultDict)
    elif riddleIndex == '3':
        return calculateRiddle3(resultDict)
    elif riddleIndex == '4':
        return calculateRiddle4(resultDict)
    elif riddleIndex == '5':
        return calculateRiddle5(resultDict)
    elif riddleIndex == '6':
        return calculateRiddle6(resultDict)
    elif riddleIndex == '7':
        return calculateRiddle7(resultDict)
    elif riddleIndex == '8':
        return calculateRiddle8(resultDict)
    elif riddleIndex == '9':
        return calculateRiddle9(resultDict)
    else:
        raise ValueError('for the riddle %s exists no calculator.' % riddleIndex)
    
def calculateRiddle1(resultDict):
    # N53° 0A.(B-C)(D-E)F E014° G(H-I).JKL
    # 20,23,35,7,32,22,2,14,21,35,39,11
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += str(int(resultDict['B']) - int(resultDict['C']))
    coords += str(int(resultDict['D']) - int(resultDict['E']))
    coords += resultDict['F']
    coords += ' E 014° '
    coords += resultDict['G']
    coords += str(int(resultDict['H']) - int(resultDict['I']))
    coords += '.'
    coords += resultDict['J']
    coords += resultDict['K']
    coords += resultDict['L']
    return coords
    
def calculateRiddle2(resultDict):
    # N 53° 0A.BCD E 014° 0E.FGH
    # 3,12,5,20,29,21,6,15 2
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += resultDict['C']
    coords += resultDict['D']
    coords += ' E 014° 0'
    coords += resultDict['E']
    coords += '.'
    coords += resultDict['F']
    coords += resultDict['G']
    coords += resultDict['H']
    return coords

def calculateRiddle3(resultDict):
    # N 53° 0A.BCD E 014° 0E.F(G-H)(I+J)
    # 16,20,17,4,15,8,3,13,14,32 3
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += resultDict['C']
    coords += resultDict['D']
    coords += ' E 014° 0'
    coords += resultDict['E']
    coords += '.'
    coords += resultDict['F']
    coords += str(int(resultDict['G']) - int(resultDict['H']))
    coords += str(int(resultDict['I']) + int(resultDict['J']))
    return coords

def calculateRiddle4(resultDict):
    # N 53° 0A.BCD E 014° 0(E+F).GHI
    # 17,3,21,26,31,32,5,7,39
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += resultDict['C']
    coords += resultDict['D']
    coords += ' E 014° 0'
    coords += str(int(resultDict['E']) + int(resultDict['F']))
    coords += '.'
    coords += resultDict['G']
    coords += resultDict['H']
    coords += resultDict['I']
    return coords
    
def calculateRiddle5(resultDict):
    # N 53° 0A.BCD E 014° 0E.FGH
    # 6,8,15,21,3,24,29,33
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += resultDict['C']
    coords += resultDict['D']
    coords += ' E 014° 0'
    coords += resultDict['E']
    coords += '.'
    coords += resultDict['F']
    coords += resultDict['G']
    coords += resultDict['H']
    return coords
    
def calculateRiddle6(resultDict):
    # N 53° 0A.B(C/4)D E014° 0E.FGH
    # 11,28,19,10,9,18,8,37
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += str(int(resultDict['C']) / int(4))
    coords += resultDict['D']
    coords += ' E 014° 0'
    coords += resultDict['E']
    coords += '.'
    coords += resultDict['F']
    coords += resultDict['G']
    coords += resultDict['H']
    return coords
    
def calculateRiddle7(resultDict):
    # N 53° 0A.BCD E 014° EF.GH(I-J)
    # 22,17,10,18,38,32,3,5,35,36
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += resultDict['C']
    coords += resultDict['D']
    coords += ' E 014° '
    coords += resultDict['E']
    coords += resultDict['F']
    coords += '.'
    coords += resultDict['G']
    coords += resultDict['H']
    coords += str(int(resultDict['I']) - int(resultDict['J']))
    return coords
    
def calculateRiddle8(resultDict):
    # N 53° 0A.B(C-D)E E 014° FG.H(I+J)K
    # 1,7,15,9,21,13,4,3,25,11,33
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += str(int(resultDict['C']) - int(resultDict['D']))
    coords += resultDict['E']
    coords += ' E 014° '
    coords += resultDict['F']
    coords += resultDict['G']
    coords += '.'
    coords += resultDict['H']
    coords += str(int(resultDict['C']) + int(resultDict['D']))
    coords += resultDict['K']
    return coords
    
def calculateRiddle9(resultDict):
    # N 53° 0A.BCD E 014° E(F-G).H(I-J)K
    # 7,38,1,21,34,6,3,10,11,32,13
    coords = 'N 53° 0'
    coords += resultDict['A']
    coords += '.'
    coords += resultDict['B']
    coords += resultDict['C']
    coords += resultDict['D']
    coords += ' E 014° '
    coords += resultDict['E']
    coords += str(int(resultDict['F']) - int(resultDict['G']))
    coords += '.'
    coords += resultDict['H']
    coords += str(int(resultDict['I']) - int(resultDict['J']))
    coords += resultDict['K']
    return coords
    
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("USAGE: %s <word> <hashalg> <riddle number>" % (sys.argv[0])) 
        
    print('Value: "%s"' % sys.argv[1])
    
    hashed = hashText(sys.argv[1], sys.argv[2])
    print('Hash: %s' % hashed)    
    result = getValuesByIndices(hashed, INDICES_BY_RIDDLE[sys.argv[3]])
    outStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultDict = dict()
    
    for index, resultNum in enumerate(result):
        resultDict[outStr[index]] = resultNum
        print("%s\t%s" % (outStr[index], resultNum))
    print(calculateCoords(sys.argv[3], resultDict))
