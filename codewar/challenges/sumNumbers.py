# 10. Sum of Digits

# اكتب دالة تأخذ رقمًا صحيحًا وتعيد مجموع أرقامه.
# مثال المدخل: 12345
# الناتج المتوقع: 15


def main():
    sumNumber = sum_numbers(2143545)
    print(sumNumber)

def sum_numbers(num):
    array = [int(i) for i in str(num)]
    return sum(array)
    


if __name__ == "__main__":
    main()