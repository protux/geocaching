#/bin/python
import sys, re
from os.path import isfile

def splitItems(text):
    regex = re.compile(r'[^a-zA-Z0-9]+')
    return regex.split(text.strip())

def clearDuplicates(items, oldItems):
    checked = set()
    unique = []
    duplicates = []

    items = removeCommentsAndEmptyLines(items)
    items = splitItems(items)
    oldItems = removeCommentsAndEmptyLines(oldItems)
    oldItems = splitItems(oldItems)

    for item in items:
        if item not in checked and item not in oldItems:
            unique.append(item)
            checked.add(item)
        else:
            duplicates.append(item)

    return buildOutputDict(unique, duplicates)

def buildOutputDict(uniques, duplicates):
    output = dict()
    output['dupcount'] = len(duplicates)
    if len(duplicates) > 0:
        output['dups'] = duplicates
    output['cleaned'] = uniques
    return output

def handleOutput(uniqueItems, duplicates):
    if len(duplicates) > 0:
        print("%s duplicate(s) found." % len(duplicates))
        print("Duplicates: %s" % ",".join(duplicates))
        saveCleanList(uniqueItems)
        print("Clean list is written to %s.out" % sys.argv[1])
    else:
        print("No duplicates found.")
        
def saveCleanList(uniqueItems):
    if len(sys.argv[1]) > 20:
        filename = 'removed_duplicates'
    else:
        filename = sys.argv[1]
        
    file = open(filename + '.out', 'w')
    file.write("\n".join(uniqueItems))
    file.close()

def stripPathFromFilename(file):
    lastSlashIndex = file.rfind('/')
    return file[lastSlashIndex + 1:]

def getTextFromFile(path):
    with open(path) as f:
        return "\n".join(f.readlines())

def getNewItems(args):
    text = args[1]
    if isfile(text):
        text = getTextFromFile(text)
    text = removeCommentsAndEmptyLines(text)
    return splitItems(text)

def removeCommentsAndEmptyLines(text):
    lines = text.split("\n")
    new = []
    for line in lines:
        commentIndex = line.find('#')
        if commentIndex > -1:
            line = line[:commentIndex].strip()
        if len(line) > 0:
            new += [line]
            
    return '\n'.join(new)
    
def getOldItems(args):
    if len(args) == 3:
        alreadyLogged = args[2]
        if isfile(alreadyLogged):
            alreadyLogged = getTextFromFile(alreadyLogged)
        return splitItems(alreadyLogged)
    else:
        return []

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        raise ValueError("Usage: %s <file or text (new TBs)> [<file or text (already logged TBs)>]" % sys.argv[0])
    
    items = getNewItems(sys.argv)
    oldItems = getOldItems(sys.argv)
    
    clearDuplicates(items, oldItems)
