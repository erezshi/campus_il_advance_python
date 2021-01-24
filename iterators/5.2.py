from itertools import combinations, count

money_bills = {
    20 : 3,
    10 : 5,
    5 : 2,
    1 : 5
}
# money = []
# for k, v  in banknotes.items():
#     for i in range(v):
#         money.append(k)
money = [ k for (k, v) in money_bills.items() for i in range(v)  ]

# com_list = []
# for i in range(len(money)):
#     money_iter = combinations(money, i)
#     for com in money_iter:
#         if sum(com) == 100:
#             com_list.append(com)

# print(len(set(com_list)))


counter = count(start=0)
for i in range(len(money)):
    money_iter = combinations(money, i)
    comb = set(money_iter)
    for x in comb:
        if sum(x) == 100:
            next(counter)

            
print(next(counter))




