# 7. Merge Two Sorted Arrays

# اكتب دالة تقوم بدمج مصفوفتين مرتبتين في مصفوفة واحدة مرتبة.
# مثال المدخل: [1, 3, 5] و[2, 4, 6]
# الناتج المتوقع: [1, 2, 3, 4, 5, 6]


def main():
    sortedArrays = sorted_arrays([1,3,5,7,9],[2,4,6,8,9])
    print(sortedArrays)
def sorted_arrays(arr1,arr2):
    sortedArray1 = list(sorted(arr1))
    sortedArray2 = list(sorted(arr2))
    finalArray = sortedArray1+sortedArray2
    return sorted(finalArray)
 

if __name__ == "__main__":
    main()
