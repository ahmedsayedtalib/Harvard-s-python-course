# 7. Binary Search

# Write a function to implement binary search. 
# The function should take a sorted array and a target number as input and return the index of the target number or -1 if not found.
# Example Input:
# arr = [1, 3, 5, 7, 9], target = 5
# Expected Output:
# 2

def main():
    checker = binary_search()
    print(checker)

def binary_search():
    array = [1,3,5,7,9]
    lastIndex = len(array) - 1
    midIndex = lastIndex // 2
    target = 7
    for i in sorted(array):
        if target == array[midIndex]:
            return array.index(target)
        elif target < array[midIndex]:
            midIndex = array.index(midIndex) // 2
        elif target > array[midIndex]:
            midIndex = lastIndex // 2
    return -1




if __name__ == "__main__":
    main()

