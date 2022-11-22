import hashlib
import random
import base64
import math

class Crypt:
    source = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

    def __init__(self, key: str):
        self.key = key

    def encrypt(self, string):
        seed = self.__genSeed()
        key = self.__genKey(seed = seed)
        rotated = self.__rotate(key, self.__urlBase64Encode(string))
        return f'{seed}.{self.__urlBase64Encode(rotated)}'

    def decrypt(self, string):
        seed, encoded = string.split('.')
        key = self.__genKey(seed = seed)
        rotated = self.__rotate(key, self.__urlBase64Decode(encoded), True)
        return self.__urlBase64Decode(rotated)


    def __genSeed(self):
        return hashlib.md5(string = random.random().hex().encode('utf-8')).hexdigest()[2:6]

    def __genKey(self, seed: str):
        return hashlib.md5(string = (seed + self.key).encode('utf-8')).hexdigest()

    def __rotate(self, key: str, __str: str, reverse: bool = False):
        rotatedSource = self.__rotateSource(key = key)
        if (reverse == True):
            return self.__strtr(source = __str, replacefrom = rotatedSource, replaceto = self.source)

        return self.__strtr(source = __str, replacefrom = self.source, replaceto = rotatedSource)

    def __rotateSource(self, key: str):
        source = list(self.source)
        len = self.source.__len__() + 3
        tmpkey = key
        buf = []

        while (tmpkey.__len__() < len):
            tmpkey += key

        while (source.__len__()):
            pos = source.__len__()
            number = int(str(tmpkey[pos:pos+3]), base = 16) % source.__len__()
            buf.append(source.pop(number))

        return ''.join(buf)

    def __strtr(self, source: str, replacefrom: str, replaceto: str):
        replacefrom = list(replacefrom)
        replaceto = list(replaceto)
        strList = list(source)
        returnStr = []
        map = {}

        for idx, c in enumerate(replacefrom):
            map[c] = replaceto[idx]

        for c in strList:
            returnStr.append(map[c])

        return ''.join(returnStr)

    def __urlBase64Encode(self, __str: str):
        returnStr = base64.b64encode(__str.encode('utf-8')).decode('ascii')
        return returnStr.replace('+', '-').replace('/', '_').replace('=', '')

    def __urlBase64Decode(self, __str: str):
        replaced = __str.replace('-', '+').replace('_', '/')
        diff = (replaced.__len__() * 6) % 8
        replaced += '=' * (math.floor((8 - diff) / 2))
        return base64.b64decode(replaced.encode('ascii')).decode('utf-8')
