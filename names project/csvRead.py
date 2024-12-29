import csv
 
names = []

with open("names.csv","r") as file:
    read = csv.reader(file)
    for row in read:
        firstName = row[0]
        lastName = row[1]
        fullName = {}
        fullName["first"] = firstName
        fullName["last"] = lastName
        names.append(fullName)
        
for name in sorted(names,key= lambda last: last["last"]):
    org = (f"{name['first']} is the son of {name['last']}")
    with open("org.txt","a") as orgFile:
        orgFile.write(f"{org} \n")
