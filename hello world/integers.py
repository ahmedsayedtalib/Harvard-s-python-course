x = float(input("What is the value of x? "))
y = float(input("What is the value of y? "))

print(round(x/y,4))
print((x/y).__ceil__())
print((x/y).__floor__())
print((x/y).__round__(2))
print(f"{x/y:.2f}")
