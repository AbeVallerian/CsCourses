import json
import ssl
import urllib.error
import urllib.parse
import urllib.request
from typing import Dict

api_key: int = 0

if api_key == 0:
    api_key = 42
    serviceurl: str = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl: str = "https://maps.googleapis.com/maps/api/geocode/json?"

ctx: ssl.SSLContext = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address: str = "Tallinn University"

parms: Dict = dict()
parms["address"] = address
if api_key is not False:
    parms["key"] = api_key
url: str = serviceurl + urllib.parse.urlencode(parms)

print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)
data: str = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js: Dict = json.loads(data)
except:
    js: Dict = None

if not js or "status" not in js or js["status"] != "OK":
    print("==== Failure To Retrieve ====")
    print(data)

print(json.dumps(js, indent=4))

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print("lat", lat, "lng", lng)
location = js["results"][0]["formatted_address"]
print(location)
