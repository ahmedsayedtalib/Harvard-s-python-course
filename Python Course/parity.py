# def main ():
#    x = int(input("Enter the value of x:- "))
#    if x % 2 == 0 :
#     print("Even Number")
#    else:
#     print("Odd Number")
#
# main()
#
# def is_even(n):
#     # if n % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return True if n % 2 == 0 else False
#
# is_even(13)
#
# if is_even(2343) == True :
#     print("Yes")
# else:
#     print("Oh No!")

name = input("Enter your name:- ")

# match name:
#     case "Ahmed":
#         print("Osman")
#     case "Ali":
#         print("Ahmed")
#     case "Khalid":
#         print("Waleed")
#     case "Padma":
#         print("Car")
#     case _:
#         print("Who?")

match name:
    case "Ahmed" | "Mohamed" | "Omer":
        print("Osman")
    case "Ali":
        print("Ahmed")
    case "Khalid":
        print("Waleed")
    case "Padma":
        print("Garma")
    case _:
        print("Who?")















