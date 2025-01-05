import sys
import requests
import json

if (len(sys.argv)) > 1:
    country = sys.argv[1]
else:
    country = input("Enter the country name:- \n")

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data,indent=2))
else:
    print("An error occured, please check the spelling")