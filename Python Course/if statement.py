# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
#
# if x > y :
#     print(f"{x} is greater than {y}")
# elif x < y :
#     print(f"{x} is less than {y}")
# elif x == y:
#     print("Equals")
# else:
#     print('HAHA')
#
#
# name1 = "Ahmed"
# name2 = "Ahmed"
#
# if name1 != name2:
#     print("Names are not the same")
# else:
#     print("Names are the same")
#
#
# num1 = 10
# num2 = 20
#
# if num1 == num2 or num1 > num2:
#     print("Big Boy")
# else:
#     print("Y")
#
score = int(input("Score: "))

if score > 100:
    print("Re-enter a valid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score < 0:
    print("Re-enter a valid score")
else:
    print("Grade: F")
