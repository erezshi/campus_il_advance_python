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
        #super().__init__(name) ## can be use for mutilpe superclass 
        self._fur_color = fur_color

    def go_to_a_walk(self):
        self._fun += 2
        print("Waff waff My fun level is rising, and its:", self._fun)

    def __str__(self): # Here we ovewriten the __str__ magic method and istead printing the memory allocation we actually print 
        return f"My name is {self._name} and I am a dog!"

    def eat(self):
        super().eat() # So we don't overwrite the basic functionality of the method eat
        print("eating a bone!")
        
def main():
    my_dog = Dog("barky", "brown")
    my_dog.eat()

    print(my_dog)
    # print(dir(my_dog)) # This will ouput all the function available for my_dog instnace from super and sub class


main()


