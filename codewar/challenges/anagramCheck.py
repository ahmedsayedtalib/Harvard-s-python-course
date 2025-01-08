# 9. Check Anagram

# اكتب دالة تتحقق إذا كانت كلمتان هما "Anagrams" (الكلمتان تحتويان على نفس الحروف بنفس التكرار).
# مثال المدخل: "listen" و"silent"
# الناتج المتوقع: True
import re

def main():
    checker = anagram_checker("nama","A+ma8n")
    print(checker)


def anagram_checker(txt1,txt2):
    seperator = r"[' ','+','-','.','_','0-9']"
    word1 = re.split(seperator,txt1.lower())
    word2 = re.split(seperator,txt2.lower())
    if sorted("".join(word1)) == sorted("".join(word2)):
        return True
    return False
    
    
    



if __name__ == "__main__":
    main()


