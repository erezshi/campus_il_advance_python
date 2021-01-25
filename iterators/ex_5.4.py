from functools import reduce
from itertools import count

# c = count(1)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
   

class IDIterator:
    def __init__(self, id=100000000):
        self._id = id
        # self.id_index = -1
         
    def check_id_valid(self, id_number):
        id_multiple = [ int(n[1]) * 2 if n[0] % 2 == 0 else int(n[1]) for n in enumerate(str(id_number), start=1) ]
        id_multiple = list(map(str, id_multiple)) # back to str
        id_plus = [ int(n[0]) + int(n[1]) if len(n) > 1 else int(n) for n in id_multiple ] 
        sum_id = reduce(lambda x, y: x + y, id_plus) # just for fun I used it instead of sum function
        if sum_id % 10 == 0:
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._id >= 999999999:
            raise StopIteration()
        # for id in count(self._id):
        #     if not self.check_id_valid(id):
        #         # self._id += 1
        #         continue  
        #     else:
        #         return self._id
        self._id += 1
        return self._id

        # return self.check_id_valid(self._id)



def main():
    id_iter = IDIterator(123456780)
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    print(next(id_iter))
    


main()


# for n in enumerate(id, start=1):
#     # print(n)
#     if n[0] % 2 == 0:
#         print(f"should {n[1]} should be multiple")
#         print()

# id_multiple = map(lambda parameter_list: expression)

# id_multiple = [ int(n[1]) * 2 if n[0] % 2 == 0 else int(n[1]) for n in enumerate(id, start=1) ]
# print(id_multiple)
# id_multiple = list(map(lambda n: int(n[1]) * 2 if n[0] % 2 == 0 else int(n[1]), enumerate(id, start=1)))
# print(id_multiple)

# x = 123
# print(str(x[0]))
# def add(list):


# l_int = [9, 24, 4, 4, 1, 6, 4, 4, 3, 10, 2, 6, 5]
# l_str = list(map(str, l_int))
# print(l_str)
# # for n in l_str:
# #     # print(len(n))
# #     if len(n) > 1:
# #         # print(n[0])
# #         print(int(n[0]) + int(n[1]))
# #         # print()
# l3 = [ int(n[0]) + int(n[1]) if len(n) > 1 else int(n) for n in l_str ] 
# print(l3)


# res = list(map(lambda item: item * 2, l))
# print(res)

# print(list(123))
# n = list(n)


# from functools import reduce
# # l = [9, 5, 4, 4, 1, 6, 4, 4, 3, 1, 2, 6, 5]
# l = [1,2,3,4,5,6,7,8,2]
# res = reduce(lambda x, y: x + y, l)
# print(res)



# def check_id_valid(self, id_number):
#         id_multiple = [ int(n[1]) * 2 if n[0] % 2 == 0 else int(n[1]) for n in enumerate(str(id_number), start=1) ]
#         id_multiple = list(map(str, id_multiple)) # back to str
#         id_plus = [ int(n[0]) + int(n[1]) if len(n) > 1 else int(n) for n in id_multiple ] 
#         sum_id = reduce(lambda x, y: x + y, id_plus) # just for fun I used it instead of sum function
#         if sum_id % 10 == 0:
#             return True
#         else:
#             return False


# print(check_id_valid(123456780))
# print(check_id_valid(123456782))
