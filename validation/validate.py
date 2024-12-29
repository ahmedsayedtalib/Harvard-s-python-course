import re

email = input("Enter email address:- ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid") 

