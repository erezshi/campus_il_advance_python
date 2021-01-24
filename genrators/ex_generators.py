#first part
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

#2nd part
def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h,m,s)


def gen_years(start=2021):
    year = start
    while True:
        yield year
        year +=1


def gen_months():
    for month in range(1, 13):
        yield month



# get_time = gen_time()
# print(next(get_time))
# print(next(get_time))
# print(next(get_time))
# print(next(get_time))
# print(next(get_time))

# for gt in gen_time():
#     print(gt)

# years = gen_years()
# print(next(years))
# print(next(years))
# print(next(years))
# print(next(years))

def gen_days(month, leap_year=False):
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

# for day in gen_days(2, False):
#     print(day)
    


# for m in gen_months():
#     print(m)

# Leap Years are any year that can be exactly divided by 4 (such as 2016, 2020, 2024, etc)
#  	not	except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
#  	 	yes	except if it can be exactly divided by 400, then it is (such as 2000, 2400)




def gen_date():
    def is_leap_year(year):
        if year % 4 == 0 and not year % 100 == 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    # print(is_leap_year(2400))
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, leap_year=is_leap_year(year)):
                for gt in gen_time():
                    # yield "%04d:%02d:%02d %s" % (year,month,day,gt)
                    yield "%02d:%02d:%04d %s" % (day,month,year,gt)



date_generator = gen_date()
# print(next(date_generator))
# print(next(date_generator))
def generator_interval(n):
    counter = 0
    for date in date_generator:
        counter += 1
        if counter % n == 0:
            yield date


# for y in generator_interval(1000000):
#     print(y)

genx = generator_interval(1000000)
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))
print(next(genx))



# counter = 0 
# for date in date_generator:
#     print(date)
#     counter += 1


# def print_interval(n):
#     counter = 0
#     for n in range(n):
#         counter += 1
#         if counter == 10:
#             print(counter)
#             counter = 0
    # print("hi")
    # next(date_generator)
    # if counter == 0:
    #     print(next(date_generator))
# next(date_generator)
# print(next(date_generator))
# print(next(date_generator))
# for date in date_generator:
#     printne

# print(next(date_generator))
# print(next(date_generator))

# def gen_interval(start):
#     counter = start
#     if 


# gen = gen_interval(1000000)

# main():
#     for 

# it_count = 0
# for date in gen_date():
#     print(next(date))
    # it_count =+ 1
    # if it_count == 100:
    #     print(next(date))
# print(next(gen_date()))
# print(next(gen_date()))
# print(next(gen_date()))

#     
# years = gen_years()
# print(next(years))
# print(next(years))
# print(next(years))
# print(next(years))

# mingen = gen_secs()
# print(mingen)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

