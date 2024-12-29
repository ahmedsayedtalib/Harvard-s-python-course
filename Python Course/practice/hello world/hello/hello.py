
def main():
    hello()

def hello(to="world"):

    name = input("Enter the name of the student:- ")

    if name == '':
       print(f'Hello',to)

    else:
       print(f'Hello, {name}')



if __name__ == "__main__":
    main()
