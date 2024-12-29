import csv

names = []

while True:
    try:
       name = input("Name:- \n")
       age = int(input("Age:- \n"))
       info = {"name":name,"age":age}
       with open("userInfo.csv","a") as file:
          writer = csv.DictWriter(file, fieldnames=["name","age"])
          writer.writerow(info)
       names.append(info)
    except ValueError:
       print("Enter a valid value for name & age")
    else:
       break
print(names)

    

    
    