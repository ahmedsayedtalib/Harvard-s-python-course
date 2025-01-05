# 3. Array Manipulation: Find Missing Number

# Given an array of integers from 1 to n, where one number is missing, write a function to find the missing number.

# Example Input:
# [1, 2, 4, 5, 6] (n = 6)

# Expected Output:
# 3

array = [1,2,4,5,6]
n = max(array)
print(n)
for i in range(1,n+1):
    if i not in array:
        print(i)
