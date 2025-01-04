import csv
import re

info = []

with open("validate.csv") as file:
    reader = csv.DictReader(file,fieldnames=["email","username"])
    for row in reader:
        info.append(row)


for i in info:
    username = i["username"]
    email = i["email"]
    finalValidate = (f"{username}, is a valid username found for the email account {email}")

    with open("finalValidate.txt","a") as file:
       file.write(f"{finalValidate} \n")