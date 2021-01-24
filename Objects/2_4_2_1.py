class BigThing:
    def __init__(self, var):
        self._var = var

    def size(self):
        if isinstance(self._var, int):
            print(len(self._var))
        elif isinstance(self._var, str):
            print(len(self._var))
        elif isinstance(self._var, list):
            print(len(self._var))  
        elif isinstance(self._var, dict):
            print(len(self._var))


class BigCat(BigThing):

    def __init__(self, var, weight):
        BigThing.__init__(self, var)
        self._weight = weight
    
    def size(self):
        super().size()
        # if self._weight > 15 and self._weight < 21:
        if self._weight in range(0,21):
            return "Fat"
        elif self._weight > 20:
            return "Very Fat"
        else:
            return "OK"


def main():
    # my_thing = BigThing("Mitzy")
    # print(my_thing.size())
    cutie = BigCat([1,2,2,4], 20)
    print(cutie.size())

main()
# class A:
#     def explore(self):
#         print("explore() method from class A")

# class B(A):
#     def explore(self):
#         super().explore()  # calling the parent class explore() method
#         print("explore() method from class B")


# b_obj = B()
# b_obj.explore()