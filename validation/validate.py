import re

email = input("Enter your email:- \n").strip()
eval = r"[a-zA-Z0-9_.%+-]+@\w+\.(com|net|edu|org|gov|co)$"

if re.fullmatch(eval,email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")