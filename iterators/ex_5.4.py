from functools import reduce
from itertools import count
   

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

