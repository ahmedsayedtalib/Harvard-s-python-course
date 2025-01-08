
# 8. Find the First Non-Repeating Character
# Write a function to find the first non-repeating character in a string and return its index. 
# If all characters repeat, return -1.
# Example Input:
# "swiss"

def main():
    checker = non_repeating("Ahmad")
    print(checker)


def non_repeating(txt):
    word = txt

    for index,char in enumerate(word.lower()):
        if word.lower().count(char) == 1:
            return index
        else:
            index += 1
    return -1


if __name__ == "__main__":
    main()