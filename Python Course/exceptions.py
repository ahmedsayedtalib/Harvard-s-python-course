#print("Hello, world) this is a syntax error, where a programmer has to manually fix the error

# try:
#     num1 = int(input("Enter the number:- "))
#     print(f"num1 value is {num1}")
# except ValueError:
#     print("Really?!")
# else:
#     print(f"num1 is {float(num1)}")
#the else is an important block in the try error handler,
# the try except are used to handle runtime errors with better efficiency, the error message is written by the programmer making fixing it more easy

while True:
    try:
        x = int(input("Enter the value of x"))
    except ValueError:
        print("x is not integer")
    else:
        break
    # we use else to break the code if condition is met