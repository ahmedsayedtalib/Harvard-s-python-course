import re
import csv

email = input("Enter your email:- ").strip()

emailEval = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co|net|org|gov|edu)$"

if re.fullmatch(emailEval,email,re.IGNORECASE):
    print("Valid")
    validEmail = email
else:
    print("Invalid")


url = input("Enter the url here to search for username:- ").strip()

username = re.sub(r"(https?://)?([a-zA-Z0-9_.%+-])+\.[a-zA-Z0-9]+/","",url,re.IGNORECASE)

print(f"{username} is a valid user")

with open("validate.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["email","username"])
    info = {"email":validEmail,"username":username}
    writer.writerow(info)   