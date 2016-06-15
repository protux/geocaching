import sys

ALPHABET_CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(rot, text):
    ciphertext = ''
    for char in text:
        index = str.find(ALPHABET, char)
        if index >= 0:
            charIndex = index + int(rot)
            if charIndex > 25:
                charIndex -= 26
            ciphertext += ALPHABET[charIndex]
        else:
            index = str.find(ALPHABET_CAPITAL, char)
            if index >= 0:
                charIndex = index + int(rot)
                if charIndex > 25:
                    charIndex -= 26
                ciphertext += ALPHABET_CAPITAL[charIndex]
            else:
                ciphertext += char
    return ciphertext

def tryAllKeys(text):
    if isinstance(text, str):
        textArray = text.split('\n')
    else:
        textArray = text
    #decryptedText = "original message:\n%s%s" % (text, "\n\n")
    decryptedText = ""
    
    for rot in range(1,26):
        decryptedText += "rot-key: %s%s" % (rot, "\n")
        for line in textArray:
            decryptedText += decrypt(rot, line) + "\n"
        decryptedText += "\n"
    return decryptedText
        
def decrypt(key, text):
    decryptedText = ""
    for c in text:
        try:
            index = ALPHABET.find(c)
            if index >= 0:
                decryptedText += ALPHABET[_getDecryptedIndex(index, int(key))]
            else:
                index = ALPHABET_CAPITAL.find(c)
                if index >= 0:
                    decryptedText += ALPHABET_CAPITAL[_getDecryptedIndex(index, int(key))]
                else:
                    decryptedText += c
            
        except:
            decryptedText += c 
    return decryptedText

def _getDecryptedIndex(index, key):
    index -= int(key)
    
    if index < 0:
        index += 26
    
    return index
