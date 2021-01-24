#### 2.2.2
class BankAccount:
## Class method
    bank_name = "PayPy"

    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def print_balance(self):
        print("Current balance is: ", self.balance)


    
    def great(self, name):
        print("Welcome", name)


#2.2.2

class Dog:
    count_animals = 0

    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age  = age
        Dog.count_animals += 1
    
    def birthday(self):
        self._age += 1

    def get_age(self):
        print(f"{self._name} is {self._age} years old ")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        print("Animel name is: " + self._name)

def main():
    # erez_account = BankAccount()
    # erez_account.great("Erez")
    # dganit_account = BankAccount()
    # dganit_account.great("Dganit")

    # eyal = BankAccount()
    # eyal.deposit(1200)
    # eyal.withdraw(200)
    # eyal.print_balance()
#ex 2.2.2 OO Part A
    # tulip = Dog("Tulip", 3)
    # bond = Dog("Bond", 1)
    # tulip.birthday()
    # bond.birthday()
    # tulip.get_age()
    # bond.get_age()
    # transferred_account = BankAccount(5000)
    #  Account with no previous amount of money
    # no_prev_money_acc = BankAccount()

    # Account with previous amount of money

    # with_prev_money_acc = BankAccount(2000)

    # no_prev_money_acc.deposit(1)
    # with_prev_money_acc.deposit(1)
    # with_prev_money_acc.balance(0)

    # no_prev_money_acc.print_balance()
    # with_prev_money_acc.print_balance()
    # my_account = BankAccount()
    # my_account.deposit(200)
    # my_account.withdraw(20)
    # my_account._balance = 0
    # print(my_account.balance)
    # print(BankAccount.bank_name) # Access from the class itself 
    # BankAccount.bank_name = "PyBank" # Note! Cange this way will affect all instances of this class
    # my_account.bank_name = "PyPy" # Not recomanded this will create new variable and not apply to all instances \
    # if we need to change then better to do it from the Class itself
    # print(my_account.bank_name) # Access from instnace of the class
    # my_account
    


#ex 2.3.3 OO Part B
    print(Dog.count_animals)
    my_pet = Dog("Shifi")
    my_pet_noname = Dog()
    my_pet.get_name()
    my_pet_noname.get_name()
    my_pet.set_name("Jony")
    my_pet.get_name()
    print(Dog.count_animals)


main()



