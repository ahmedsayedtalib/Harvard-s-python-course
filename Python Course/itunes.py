import requests # type: ignore
import sys
import json


if len(sys.argv)!=2:
    sys.exit("Too few arguments")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1]) 
o = response.json()

for result in o["results"]:
    print(result["trackName"],result["artistName"],sep=", Artist:- ")
    
    
    
    
    
    
    
    # print(response.json())

