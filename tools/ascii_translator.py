import sys, re
from os.path import isfile

def getTextFromFile(path):
    with open(path) as f:
        return f.readlines()

def getTextFromFile(path):
    with open(path) as f:
        return f.readlines()[0]

def getSingleAsciiCodes(text):
    return re.split('[^0-9]+', text)

def translateAscii(asciiArray):
    message = ''
    for ascii in asciiArray:
        message += chr(int(ascii))
    return message
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: %s <file or ascii>" % sys.argv[0])
        exit(1)
    
    text = sys.argv[1]
    if isfile(text):
        text = getTextFromFile(text)
    asciiCodes = getSingleAsciiCodes(text)
    print("".join(asciiCodes))
    print(translateAscii(asciiCodes))
