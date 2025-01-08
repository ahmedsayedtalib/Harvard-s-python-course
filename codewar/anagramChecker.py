# 6. Anagram Checker

# Write a function to determine if two strings are anagrams of each other. Two strings are anagrams if they use the same characters in the same quantity, but in a different order.

# Example Input:
# "listen", "silent"

# Expected Output:
# True


def main():
    print(anagram("silent","listen"))

def anagram(txt1,txt2):
    firstWord = txt1.split()
    secondWord = txt2.split()
    firstWordList = []
    secondWordList = []
    for word in firstWord:
        for i in sorted(word):
            firstWordList.append(i)
    for word in secondWord:
        for i in sorted(word):
            secondWordList.append(i)
    firstWord = "".join(firstWordList)
    secondWord = "".join(secondWordList)
    if firstWord.lower() == secondWord.lower():
        print(f"First word is:- {firstWord.title()}")
        print(f"Second word is:- {secondWord.title()}")
        return True
    else:
        return False
  
   

        




if __name__ == "__main__":
    main()