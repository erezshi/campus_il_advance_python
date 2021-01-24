
# def combine_coins(coin, numbers):
#     output = ''
#     for num in numbers:
#         output += coin + str(num) + ', '
#     return output[:-2]



# print(combine_coins("$", range(5)))

# def square(num):
#     return num ** 2

list_of_numbers = [2, 3, 4, 5]
# result = map(square, list_of_numbers)
result = map(lambda n: n ** 2, list_of_numbers)
print(list(result))

# def multiply_num(a, b):
#     return a * b

L1 = [2, -2, 5, 8]
L2 = [1, 3, 2,-1]
# result = map(multiply_num, L1, L2)
result = map(lambda a, b: a * b, L1, L2)
print(list(result))


#Filter
#filter(filter_function, sequence) 
# the filter function will return only what filter_function evaluate as true and create iterator out if it
import os
my_files = os.listdir('/Users/erezsh/Downloads')
def is_pdf_file(filename):
    return filename.endswith(".pdf")

print(is_pdf_file('test.pdf'))

result = filter(is_pdf_file, my_files)
print(list(result))

import functools
# def add(x, y):
#     return x + y

shopping_list = [200, 120, 330, 50]
# functools.reduce(function, sequence [,initializer])
# print(functools.reduce(add, shopping_list, 15))
print(functools.reduce(lambda x, y: x + y, shopping_list, 15))
import functools
def f(a, b):
    if a < b:
        return a
    else:
        return b

print(functools.reduce(f, [44, 11, 34, 55, 100, 210]))



#Lambda function
print((lambda x, y: x + y) (2, 5))
import functools


shopping_list = [200, 120, 330, 50]
# functools.reduce(function, sequence [,initializer])
# print(functools.reduce(lambda x, y: x + y, shopping_list))

#save lamda to variable (Not parctical but can be done)
new_add = lambda x, y: x + y
print(new_add(5, 2))

#Quiz
print((lambda y, x: x in y) ([1,2,6,9], 9)) # print True

#When we use lambda?
#we use lamdbda if we need one action but of few actions we should use normal function
#use lambda as argument to another function man filter and reduce is a good example for such actions
my_list = [0,1,2,3,4,5,6,7]
print(list(filter(lambda x: x % 2 == 0, my_list)))

sorted(secuence [,key])
#we like to sort the list by the 2nd element of each tuple
list_of_tupels = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(sorted(list_of_tupels, key=lambda x: x[1]))

#Use it as element in list 
calc_sqrt_list = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4 ]
for func in calc_sqrt_list:
    print(func(3))


#List comprehension


#new_list = [expression for item in secuence]
my_money_list = [x ** 2 for x in range(100)]
print(my_money_list)

letters = ['a', 'b', 'c']
upper_letters = [x.upper() for x in letters]
print(upper_letters)

list1 = [1, 2, 3]
list2 = [5, 6, 7]
mult_list = []

# for x in list1:
#     for y in list2:
#         mult_list.append(x * y)

# print(mult_list)
#Instead
mult_list = [ x * y for x in list1 for y in list2 ]
print(mult_list)

#condition
my_list = [1, 2, 3, 4, 5]
squared_list = [x * x for x in my_list if x % 2 == 0]
print(squared_list)

#nested if 
nested_list = [x * 2 for x in range(10) if x > 3 if x < 7]
print(nested_list)

even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(even_odd_list)

numbers= [1, 2, 3, 4]
list_of_lists = [[2 * x, x] for x in numbers]# we have 2 elememts in the inner list 2*x , x
print(list_of_lists)

#more example list dict set ... https://book.pythontips.com/en/latest/comprehensions.html


def combine_coins(coin, numbers):
    output = ''
    for num in numbers:
        output += coin + str(num) + ', '
    return output[:-2]

map

print(combine_coins("$", range(5)))

def combine_coins(coin, numbers): return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))
print(combine_coins("$", range(5)))


