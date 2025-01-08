# 4. FizzBuzz Problem

# اكتب برنامج يطبع الأرقام من 1 إلى 50، ولكن:

#     إذا كان الرقم يقبل القسمة على 3 اطبع "Fizz".
#     إذا كان الرقم يقبل القسمة على 5 اطبع "Buzz".
#     إذا كان الرقم يقبل القسمة على 3 و5 معًا اطبع "FizzBuzz".

for i in range(1,51):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    
    print(i)
