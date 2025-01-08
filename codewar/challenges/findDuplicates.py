# 8. Find Duplicates in an Array

# اكتب دالة تعيد جميع الأرقام المتكررة في مصفوفة.
# مثال المدخل: [1, 2, 3, 2, 4, 5, 3]
# الناتج المتوقع: [2, 3]


def main():
    duplicatedNumbers = duplicate_numbers(12346245399)
    print(duplicatedNumbers)

def duplicate_numbers(num):
    listedNums = [i for i in str(num)]
    repeatedNums = list()
    for i in enumerate(listedNums):
        if listedNums.count(i[1]) != 1:
            repeatedNums.append(i[1])
    return list(set(repeatedNums))
            






if __name__ == "__main__":
    main()

    



