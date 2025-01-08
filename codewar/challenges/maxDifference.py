# 3. Find the Maximum Difference

# اكتب دالة تأخذ مصفوفة من الأرقام وتعيد أكبر فرق بين أي رقمين فيها.
# مثال المدخل: [2, 8, 3, 1, 7]
# الناتج المتوقع: 7 (الفرق بين 8 و1)


def main():
    maxDifference = max_difference(1,2,3,4,5,8)
    print(maxDifference)


def max_difference(*num):
    maxDiff = max(num) - min(num)
    return maxDiff



if __name__ == "__main__":
    main()


