from itertools import count 
# 4.1.2
# def translate(sentence):
#     words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
#     word_generator = (word for word in sentence.split())
#     str1 = ''
#     for i in word_generator:
#         str1 += words[i] + ' '
  
#     return str1

# print(translate("el gato esta en la casa"))

#ex 4.1.3
def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    return next((a for a in count(n + 1) if is_prime(a)))



print(first_prime_over(200))

# from itertools import count 
# gen = (a for a in count(10 + 1))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    countries_and_capitals = (l.replace("\n", ("")).split(",") for l in single_line_gen)
    capitals_dict = dict(countries_and_capitals)

    # print(next(single_line_gen))
    # print(next(single_line_gen))
    # print(next(single_line_gen))
    # print(next(single_line_gen))
    # print(next(countries_and_capitals))
    # print(next(countries_and_capitals))

    print(capitals_dict["Japan"])



# # בהרצת הקוד יתקבל הפלט:
# France,Paris
# Israel,Jerusalem
# Italy,Rome
# Japan,Tokyo


def city_generator():
    print("Starting")
    yield "London"
    yield "Berlin"
    yield "Amsterdam"

def add_jerusalem_generator():
    yield from city_generator()
    yield "Jerusalem"


patriot = add_jerusalem_generator()
print(next(patriot))
print(next(patriot))
print(next(patriot))
print(next(patriot))

def func3():
     return 1
     return 2
print(func3())
print(func3())

def gen3():
     yield 1
     yield 2
x = gen3()
print(next(x))
print(next(x))

def gen4():
    x = 0
    while x < 3:
        yield x
        x += 1
s = gen4()
print(next(s))
print(next(s))
print(next(s))

# ex 4.3.4

def get_fibo(fib):
    x, y = 0, 1
    z = 0
    while x <= fib:
        yield x
        z = x + y
        x = y
        y = z


xgen = get_fibo(50)
# print(next(xgen))
# print(next(xgen))
# print(next(xgen))
for n in xgen:
    print(n)

def gen_secs():
    n = 0
    while n <= 59:
        yield n
        n += 1

def gen_minutes():
    n = 0
    while n <= 59:
        yield n
        n += 1

def gen_hours():
    n = 0
    while n <= 23:
        yield n
        n += 1

def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                # print("%02d:%02d:%02d")
                yield "%02d:%02d:%02d" % (h,m,s)


# get_time = gen_time()
# print(next(get_time))

# for gt in gen_time():
#     print(gt)


def gen_years(start=2021):
    year = start
    while True:
        yield year
        year +=1

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):

    def get_days():
        if month == 2 and leap_year:
            return 29
        elif month == 2 and not leap_year:
            return 28
        elif month in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30

    days = get_days() + 1
    for day in range(1, days):
        yield day

for day in gen_days(2, False):
    print(day)
    
    #     return
    # if month in [1,3,5,7,8,10,12]:
    #     for day in range(1, 32): # case for 31 days
    #         yield day
    # elif month in [4,6,9,11]:
    #     for day in range(1, 31): # case for 30 days
    #         yield day
    # elif month == 2 and leap_year: 
    #     for day in range(1, 30): # Case leap year 29 days
    #         yield day
    # else:
    #     for day in range(1, 30): # Case leap year 29 days
    #         yield day
    
    # for day in range(1, 30): # Case leap year 29 days
    #         yield day



for m in gen_months():
    print(m)
years = gen_years()
print(next(years))
print(next(years))
print(next(years))
print(next(years))

mingen = gen_secs()
print(mingen)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

