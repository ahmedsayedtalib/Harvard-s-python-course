# 9. Check if Two Numbers Have the Same Digits
# Write a function that checks if two numbers contain the exact same digits (in any order).
# Example Input:
# 12345, 54321
# Expected Output:
# True


def main():
    checker = same_digits(1234897605,5697804321)
    print(checker)

"""The below function checks if 2 numbers have the same number of digits and the same set of numbers"""
"""If the 2 numbers meet the check condition, the function returns True, else returns False"""
def same_digits(num1,num2):
    if sorted(str(num1)) == sorted(str(num2)):
        return True
    return False
   


    
    


if __name__ == "__main__":
    main()