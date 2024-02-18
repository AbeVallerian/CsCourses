import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

ctx: ssl.SSLContext = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

POSITION: int = 18
N_REPEAT: int = 7

url: str = "http://py4e-data.dr-chuck.net/known_by_Imani.html"
for i in range(N_REPEAT):
    html: str = urllib.request.urlopen(url, context=ctx).read()
    soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

    tags = soup("a")
    for i, tag in enumerate(tags):
        if i == POSITION - 1:
            print(tag.get("href", None))
            url = tag.get("href", None)
            continue
