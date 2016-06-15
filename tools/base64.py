import base64, sys

def decodeText(b64):
    return str(base64.b64decode(b64))
    
def decodeBinary(b64):
    return base64.b64decode(b64)
    
def encode(text):
    if type(text) == str:
        text = bytes(text, 'utf-8')
    return base64.b64encode(text)
