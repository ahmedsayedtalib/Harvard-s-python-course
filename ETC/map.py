
def main():
    name("Ahmed","Sayed","Talib","Osman")


def name(*fullname):
    upperName = map(str.upper,fullname)
    print(*upperName)


if __name__ == "__main__":
    main()