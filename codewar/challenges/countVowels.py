# 6. Count Vowels

# اكتب دالة تعد عدد الحروف المتحركة (a, e, i, o, u) في النصوص المدخلة.
# مثال المدخل: "education"

def main():
    vowelCount = vowel_letters("AhmedSayedTalibOsman")
    print(vowelCount)

def vowel_letters(txt):
    vowelLetters = []
    for i in txt.lower():
        if i in ["a","u","o","e","i"]:
            vowelLetters.append(i)
    return len(vowelLetters)

        
if __name__ == "__main__":
    main()

