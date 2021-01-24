class Animal:  #Superclass

    def __init__(self, name):
        self._name = name
        self._hunger = 0
        self._fun = 0

    def play(self):
        self._fun += 1

    def eat(self):
        if self._hunger > 0:
            self._hunger -= 1
    
    def go_to_toilet(self):
        self._hunger += 1




class Dog(Animal): #subclass

    def __init__(self, name, fur_color):
        Animal.__init__(self, name)
        self._fur_color = fur_color

    def go_to_a_walk(self):
        self._fun += 2
        print("Waff waff My fun level is rising, and its:", self._fun)


def main():
    tamagotchi = Animal('barky')
    tamagotchi.play()    
    flupapy = Dog("fluppy", "Brown")
    flupapy.play()
    flupapy.eat()
    flupapy.go_to_a_walk()
    print(isinstance(flupapy, Dog)) #True
    print(isinstance(flupapy, Animal)) # True
    print(issubclass(Dog, Animal)) # True
    print(issubclass(Animal, Dog)) # False
    # print(isinstance(2, int))
    # print(isinstance("text", int))
    

main()

