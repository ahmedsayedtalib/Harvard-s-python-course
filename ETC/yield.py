def main():
    number = int(input("Number:- "))
    for s in sheep(number):
        print(s)

def sheep(n):
    
    for i in range(n):
        yield  "🐏" * i # return with large amount of n range will hang due to memory limitation, use yield istead





    
if __name__ == "__main__":
    main()