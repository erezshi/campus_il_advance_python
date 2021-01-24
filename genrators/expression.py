# new_generator = (expression for item in sequence if condition) # Must me round perentesis

# Do not try this at home:
# huge_list = [n for n in range(10 * 10) if is_print(n)]
# for prime_number in huge_list:
#     print(prime_number)
def is_prime(num):
    res = False
    for i in range(2,num):   
        if (num % i) == 0:
            # print(num,"is not a prime number")
            # print(i,"times",num//i,"is",num)
            break
        else:
            res = True
    return res
# print(is_prime(12))

prime_generator = (n for n in range(10 ** 10) if is_prime(n))
# for prime_number in prime_generator:
#     print(prime_number)

# print(prime_generator)
print(next(prime_generator))
print(next(prime_generator))
print(next(prime_generator))
print(next(prime_generator))
print(next(prime_generator))
print(next(prime_generator))
gen = (i / 2 for i in [0, 9, 21, 32])
print(next(gen))
print(next(gen))

