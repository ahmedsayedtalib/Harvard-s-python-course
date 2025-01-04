
def main():
    fullname("ahmed sayed talib osman")


def fullname(*name):

    upperName = [word.title() for word in name]

    print(*upperName)

main()