#!/usr/bin/env python3

import requests
import sys
import json

if len(sys.argv) !=2:
    print("usage:", sys.argv[0], "<band name>")
    print("example:", sys.argv[0], "weezer")
    sys.exit()

# set number of tracks to "limit=5" in url
response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])

