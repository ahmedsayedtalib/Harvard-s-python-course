# Write a function that repeatedly sums the digits of a number until a single-digit result is obtained.

# Example Input:
# 9876

# Expected Output:
# 3 (9 + 8 + 7 + 6 = 30 → 3 + 0 = 3)


def main():
    summ = digits_sum(9876)
    print(summ)

def digits_sum(num):  
    numbers = [i for i in str(num)]
    intNumbers = [int(i) for i in numbers]
    while len(intNumbers) != 1:
        reducedNumber = sum(intNumbers)
        intNumbers.clear()
        for i in str(reducedNumber):
            intNumbers.append(int(i))
    return reducedNumber
    





if __name__ == "__main__":
   main()

