#Type of exceptions
#Syntax Errors 
# 1. We need to fix the issue
#Runtime Errors
# Code examlpe
# number = input("Enter a number: ")
# result = 2 + int(number)
# print(result)

# Enter a number: asdas
# Traceback (most recent call last):
#   File "/Users/erezsh/work/campus_il/exceptions/3_1.py", line 6, in <module>
#     result = 2 + int(number)
# ValueError: invalid literal for int() with base 10: 'asdas'

# Exception 
# buildin exceptions 
# IndexError - if we try to access a location not exist in list 
# KeyError - if we try to access key that don't exist in dictionaty 
# ImportError - if we try to import library tath don't exist

# ValueError inharit from superclass Exception that inharit from BaseException 
print(issubclass(ValueError, Exception))
print(issubclass(ValueError, BaseException))
Exception hierarchy
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
Traceback 



