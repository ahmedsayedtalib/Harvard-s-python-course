# 4. Matrix: Diagonal Sum
# Write a function that takes a square matrix (2D array) as input and calculates the sum of its diagonals (both primary and secondary).
# Example Input:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Expected Output:
# Sum = 25 (Primary diagonal: 1 + 5 + 9 = 15, Secondary diagonal: 3 + 5 + 7 = 10)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

primary_diagonal = matrix[0][0] + matrix[1][1] + matrix[2][2]
secondary_diagonal = matrix[0][2] + matrix[1][1] + matrix[2][0]
summation = primary_diagonal + secondary_diagonal

print(primary_diagonal)
print(secondary_diagonal)
print(summation)
