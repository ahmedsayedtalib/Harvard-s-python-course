balance = 2000


def main():
    print("Balance:-",balance)
    deposit(8500)
    witdraw(2000)
    print("Balance:-",balance)
    
def deposit(n):
    global balance
    balance += n
    return n 

def witdraw(n):
    global balance
    balance -= n
    return n

if __name__ == "__main__":
    main()