import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.peco-online.ro/index.php"

#send a POST request like the form submission
headers = {
    "carburant": "Benzina_Regular",                     #or Benzina_Premium, Motorina_Regular, Motorina_Premium, GPL, AdBlue, CNG
    "locatie": "oras",                                  #or judet
    "nume_locatie": "Bucuresti",                        #any city name from Romania
    "retele[]": ["Rompetrol","OMV", "Petrom", "MOL"]    #can add more brands
}

response = requests.post(url, data=headers)         #simulate the 'search' button
soup = BeautifulSoup(response.text, "html.parser")  #server returns a HTML page

#find the <script> tag that contains `rezultate = JSON.parse(...)`
script = soup.find("script", string=re.compile(r"rezultate\s*=\s*JSON\.parse"))

#extract the JSON string inside the call
match = re.search(r"JSON\.parse\('(.+?)'\)", script.string)

if match:
    raw_json_str = match.group(1).encode().decode('unicode_escape') #unescape \u0103, etc.
    rezultate = json.loads(raw_json_str)                            #converts JSON string into a Python list

    print("Found", len(rezultate), "results.\n")
    for i in rezultate:
        brand = i[0]
        lat = i[1]
        lon = i[2]
        city = i[3]
        address = i[4]
        price = i[5]
        print(f"{brand} - {city}, {address}: {price} lei/l")
else:
    print("No results found.")