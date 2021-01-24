import functools

with open('names.txt', 'r') as f:
    outlist = [word.strip() for word in f.readlines()]
    def findlongest(a, b):
        if len(a) > len(b):
            return a
        else:
            return b
    longname = functools.reduce(findlongest, outlist)

    def findlongest2(words):
        wordsize = [ len(word) for word in words ]
        # longname = functools.reduce(lambda word: len(word) < max(wordsize), outlist)
        longname = list(filter(lambda word: len(word) == max(wordsize), words))

        return longname[0]


    # print(longname)

    # totalchars = list(map(lambda x: len(x) + x, outlist))
    def add(words):
        numchar = 0
        for word in words:
            numchar += len(word)

        return numchar

    # numchar = map(lambda w: w += len(w), outlist)
    # print(numchar)

    print(add(outlist))
    # print(totalchars)

    def lengthword(words):
        names = {}
        for word in words:
            # print(f"{word} {len(word)}")
            names[word] = len(word)
            words_lengh = [v for k, v in names.items()]
            smallest_number = min(words_lengh)
            smallest_word = [k for k, v  in names.items() if v == smallest_number] 

                
        # print(type(names))
        print(words_lengh)
        print(smallest_number)
        print(smallest_word)

    def name_length(names):
        with open('name_length.txt' , 'a+') as f:
            for name in names:
                f.write(f"{str(len(name))}\n" )    
                # f.write(str(len(name)))   
                #  
    def get_number(n):
        L = list(filter(lambda name: len(name) == n, outlist))

        return L
        # for name in outlist:
        #     if len(name) == n:
        #         print(name)





    # lengthword(outlist)
    # name_length(outlist)
    # print(get_number(4))
    print(findlongest2(outlist))





