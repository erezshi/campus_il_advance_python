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
        while True:
            if self.check_id_valid(self._id):
                self._id += 1
                return self._id -1
            if self._id >= 999999999:
                raise StopIteration()
            self._id += 1

    def id_generator(self):
        while self._id <= 999999999:
            if self.check_id_valid(self._id):
                yield self._id
            self._id += 1


def main():

    # id = 123456780
    id = input("Enter ID:   ")
    var = input("Generator or Iterator? (gen/it):  ")
    # var = "gen"
    # gen_id = id_iter.id_generator()
    if var == "it":
        obj = iter(IDIterator(int(id)))
    elif var == "gen":
        obj = IDIterator(int(id)).id_generator()
    else:
        print("An invalid argument was entered...")


    try:
        for i in range(10):
        # for id in obj:
        #     print(id)
            print(next(obj)) #using next instead of for id in obj to catch the exception
    except StopIteration:
        print(f"you have reached id 999999999..ending loop")
    except UnboundLocalError as e:
        print(e)

main()

