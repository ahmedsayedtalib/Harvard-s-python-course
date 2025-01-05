# 5. Palindrome Checker

# Write a function to check whether a given string is a palindrome. Ignore spaces, punctuation, and capitalization.

# Example Input:
# "A man, a plan, a canal, Panama"

# Expected Output:
# True
import re

def main():
    print(palindrome_checker("abanaba"))

def palindrome_checker(txt):
    seperator = r"[+ ]"
    word = re.split(seperator,txt)
    oneWord = "".join(word).lower()
    print(oneWord)
    print("".join(reversed(oneWord)))
    if oneWord == "".join(reversed(oneWord)):
        return True
    else:
        return False

if __name__ == "__main__":
    main()