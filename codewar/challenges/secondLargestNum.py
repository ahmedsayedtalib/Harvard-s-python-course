
# 5. Find the Second Largest Number

# اكتب دالة تعيد ثاني أكبر رقم في مصفوفة.
# مثال المدخل: [10, 20, 5, 30, 25]
# الناتج المتوقع: 25


def main():
    secondLargestNum = second_largest(1,2,3,4,5,6,89,7,5,43,3,5,6757,968,25,41,563,57)
    print(secondLargestNum)

def second_largest(*num):
    removeMax = sorted(num)
    removeMax.pop()
    return max(removeMax)


if __name__ == "__main__":
    main()
