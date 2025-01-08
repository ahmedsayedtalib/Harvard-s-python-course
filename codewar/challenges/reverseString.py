# 1. Reverse a String

# اكتب دالة تقوم بعكس النصوص المدخلة.
# مثال المدخل: "hello"
# الناتج المتوقع: "olleh"

def main():
    reversedText = reverse_string("ahmed")
    print(reversedText)

def reverse_string(txt):
    reversedText = list(reversed(txt))
    return "".join(reversedText)

   


if __name__ == "__main__":
    main()