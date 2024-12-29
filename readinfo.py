import csv

with open("userInfo.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        age = row[1]
        with open("readable.txt","a") as writeFile:
            writeFile.write(f"{name} is {age} years old \n")
