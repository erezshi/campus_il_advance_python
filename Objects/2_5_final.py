class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("message")



class Dog(Animal):
    def __init__(self,name, hunger):
        Animal.__init__(self, name, hunger)
        self._type = "Dog"

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

    # def get_name(self):
    #     super().get_name()

    # def is_hungry(self):
    #     super().is_hungry()

    # def feed(self):


class Cat(Animal):
    def __init__(self,name, hunger):
        Animal.__init__(self, name, hunger)
        self._type = "Cat"

    
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self,name, hunger, stink_count=6):
        Animal.__init__(self, name, hunger)
        self._type = "Skunk"
        self._stink_count = stink_count
    
    def talk(self):
        print("tssss")

    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def __init__(self,name, hunger):
        Animal.__init__(self, name, hunger)
        self._type = "Unicorn"
    
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self,name, hunger, color="Green"):
        Animal.__init__(self, name, hunger)
        self._type = "Dragon"
        self._color = color

    def talk(self):
        print("Raaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 500)
    # new animals
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)

    zoo_lst =  [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinky_jr, clair, mcfly]

    for animal in zoo_lst:
        while animal.is_hungry():
            while animal.is_hungry():
                animal.feed()
            print(f"{animal._type} {animal._name}" )
            animal.talk()
            if isinstance(animal, Dog):
                animal.fetch_stick()
            elif isinstance(animal, Cat):
                animal.chase_laser()
            elif isinstance(animal, Skunk):
                animal.stink()
            elif isinstance(animal, Unicorn):
                animal.sing()
            else:
                animal.breath_fire()
    print(f"Thank you for visiting: {Animal.zoo_name}")



            
    #     print(animal.get_name())
    # print(dir(brownie))
    # print(brownie.__class__.__name__)
    # print(brownie._type)


main()
















class BankAccount:
    def __init__(self):
        self._bank_name = "Discount"
        # self._type = "My_bank"

class NewBankAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self._sub_name = "NewBank"

def main_test():
    client = NewBankAccount()
    print(client._bank_name)
    print(client._sub_name)
# main_test()


