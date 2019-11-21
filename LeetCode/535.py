import random
import string

class Codec:
    alphabet = string.ascii_letters + "0123456789"
    def __init__(self):
        self.encodeDict = {}
        self.decodeDict = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        code = ""
        while code not in self.decodeDict:
            code = ''.join(random.choice(self.alphabet) for _ in range(6))
            self.encodeDict[longUrl]=code
            self.decodeDict[code]=longUrl
        return "http://tinyurl.com/"+code
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl[-6:]
        return self.decodeDict[code]


# Your Codec object will be instantiated and called as such:
url = "http://www.google.com"
codec = Codec()
x= (codec.encode(url))
print(codec.decode(x))