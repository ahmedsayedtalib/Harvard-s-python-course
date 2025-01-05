import re

def main():
    revesre = reverse_word("hello, world.Ahmed ")
    print(revesre)

def reverse_word(txt):
    seperators = r"[,.,+ ]" 
    words = re.split(seperators,txt)
    newList = []
    for word in words:
        rev_word = "".join(reversed(word))
        newList.append(rev_word)
    return " ".join(newList)




if __name__ == "__main__":
    main()