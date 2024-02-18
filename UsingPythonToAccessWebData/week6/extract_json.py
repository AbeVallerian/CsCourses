import json
import ssl
import urllib.request
from typing import Dict

ctx: ssl.SSLContext = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url: str = "http://py4e-data.dr-chuck.net/comments_1977928.json"
print("Retrieving", url)

uh = urllib.request.urlopen(url, context=ctx)
data: str = uh.read()
print("Retrieved", len(data), "characters")

items: Dict = json.loads(data)
sum: int = 0
for item in items["comments"]:
    sum += item["count"]
print(sum)
