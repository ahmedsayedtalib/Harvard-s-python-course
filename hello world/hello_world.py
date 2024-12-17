name = input("What is your name? ").strip().title() #Best
name = name.strip() # removes the whitespaces
name = name.capitalize() # capitalize the first letter
name = name.title() # capitalize the first letter of each word
name = name.strip().capitalize().title() # All in one


print("hello, " + name)

print("Hello,",name," \nNew line")

print("Hello, ", end="")

print(name)

print (f"Hello, {name}") #weird!, but true

first, last = name.split(" ")

print(f"Hello, {last}")
