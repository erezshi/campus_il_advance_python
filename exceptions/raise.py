

def factorial(n):
    if n < 0:
        raise  ("can't enter negetive numbers")
    else:
        fact = 1
        for i in range(n, 0, -1):
            fact = fact * i
        return fact

# print(factorial(-1))


class FactofialArgumentError(Exception):

    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"Provided argument {self._arg} is not  positive integer."

    def get_arg(self):
        return self._arg



def factorial_new(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise FactofialArgumentError(n)
        
    except FactofialArgumentError as e:
        print(f"Provided argument {e.get_arg()} is not  positive integer.")

    else:
        fact = 1
        for i in range(n, 0, -1):
            fact = fact * i
        return fact

print(factorial_new(-1))
# print(isinstance(-1.0, int))