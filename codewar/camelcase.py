import re


def main():
    cS = camel_case("a-Pippi_is_pippi")
    print(cS)
    newDef = new_seperator("a-b-c")
    print(newDef)


def camel_case(text):
    seperators = r"[','','-'','_']"
    for sep in seperators:
        if sep in text:
            word = text.split(sep)
            capWord = [c.title() for c in word[1:]]
            print(word)

            if len(word) == 3:
                return "".join(word).upper()
            elif word[0].isupper():
                return word[0]+"".join(capWord)
            else:
                firstName = word[0].lower()
                return firstName + "".join(capWord)
    return text


def new_seperator(txt):
    seperator = r"[,_-]"
    word = re.split(seperator,txt)
    cS = [i.title() for i in word]
    camelCase = "".join(cS[1:])
    for _ in txt:
        if len(word) == 3:
            return "".join(word).upper()
        else:
            return word[0]+camelCase

    return ""


if __name__ == "__main__":
    main()








