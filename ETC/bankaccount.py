class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance += n

    def withdraw(self,n):
        self._balance -= n



def main():
    acocunt = Account()
    print("Balance:- ", acocunt.balance)
    acocunt.deposit(8500)
    acocunt.withdraw(2000)
    print("Balance:- ", acocunt.balance)



if __name__ == "__main__":
    main()