# key words True False None...
# Literals 
#     strings
#     builad nimaric
#     bulians

# dic = {1: 'jon', 2: 'smith'}
# print(dic.keys())
# print(dic.values())
# for k, v in dic.items():
#     print(v)

# vals = [ k  for k, v in dic.items()]
# print(vals)

class Animel:
    
    def __init__(self, name, age=1):
        self._name = name
        self._age = age

    def get_age(self, age=1):
        self._age = age

    def print_details(self):
        print(f'Name: {self._name}\nAge: {self._age}')



anime1 = Animel('Tulip')
anime1.get_age(10)
anime1.print_details()

class Dog(Animel):
    def __init__(self, purcolor):
        super().__init__(self, name, age=1)
        




# controle flow

for i in range(1,11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

a = 10
b = 20 
if a < b:
    print(f"{a} is less then {b}")
elif a == 20:
    print(f"{a} is equal t0  {b}")
else:
    print(f"{a} is grater than {b}")


#3 Go over the promotion manager project

#4 common interview question
for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBazz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Fibonacci Sequence
a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b

#5 data types tuple 

#list comprehension
# square = [numXnum for num in  list]
# 
# 7 genarator
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield f"{i+1}: {a}"
        a, b = b, a + b

for item in fib(10):
    print(item) 


#8 OOP

class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"My name is: {self.name}")

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super().__init__(name)
        self.hero_name = hero_name

    def print_name(self):
        super().print_name()
        print(f"...And I am {self.hero_name}")

o1 = Person("Bob")
o1.print_name()
o2 = SuperHero("bobi","super_bob")
o2.print_name()

#9

