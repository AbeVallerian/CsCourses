import ssl
from typing import List
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx: ssl.SSLContext = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url: str = "http://py4e-data.dr-chuck.net/comments_1977925.html"
html: str = urlopen(url, context=ctx).read()
soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

sum: int = 0
tags: List = soup("span")
for tag in tags:
    sum += int(tag.contents[0])
print(sum)
