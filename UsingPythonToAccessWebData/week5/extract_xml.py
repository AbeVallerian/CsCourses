import ssl
import urllib
import xml.etree.ElementTree as ET
from typing import List

ctx: ssl.SSLContext = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url: str = "http://py4e-data.dr-chuck.net/comments_1977927.xml"
print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data: str = uh.read()
print("Retrieved", len(data), "characters")
tree = ET.fromstring(data)

counts: List = tree.findall(".//count")
sum: int = 0
for count in counts:
    sum += int(count.text)
print(sum)
