# 2. Check for Palindrome
# اكتب دالة تتحقق إذا كانت الكلمة عبارة عن "Palindrome" (كلمة تُقرأ بنفس الشكل من الأمام والخلف).
# مثال المدخل: "radar"
# الناتج المتوقع: True

def main():
    palindromeWord = palindrome("radar")
    print(palindromeWord)


def palindrome(txt):
    word = list(reversed(txt))
    if "".join(word) == "".join(reversed(word)):
        return True
    return
    

    
    
if __name__ == "__main__":
    main()


