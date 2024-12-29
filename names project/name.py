names = []

for name in range(4):
    name = input("Enter name:- \n")
    names.append(name)
    with open("names.csv","a") as file:
        file.write(f"{name} \n")
