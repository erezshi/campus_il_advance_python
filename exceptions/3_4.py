import string

sp = string.punctuation.replace('_', '')
# print(sp)

# s1 = "Erez12#@@3"

# for i in s1:
#     print(i in sp)

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"Index .{self._arg}. in username is IllegalCharacter"
    
    def get_arg(self):
        return self._arg

class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"User Name {self._arg} UsernameTooShort"
    
    def get_arg(self):
        return self._arg

class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"Username \'{self._arg}\' is Too Long"
    
    def get_arg(self):
        return self._arg

class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"Unqualified password enter.\nmust contain Digits, Upper Case lower case and a special carecter"
    
    def get_arg(self):
        return self._arg

class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"The Password you enter is Too Short\nShould be at list 8 charecters"
    
    def get_arg(self):
        return self._arg

class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    
    def __str__(self):
        return f"The Password you entered is Too Long\n Can't exceed 40 charecters"
    
    def get_arg(self):
        return self._arg


def check_input(username, password):
    
    def get_bool(str_item):
        res = [x in sp for x in str_item ]
        return res

    rules = [lambda x: any(x.isupper() for x in password), # must have at least one uppercase
        lambda x: any(x.islower() for x in password),  # must have at least one lowercase
        lambda x: any(x.isdigit() for x in password),  # must have at least one digit
        lambda x: any(get_bool(password))
        ]
    try:
        for (i, ch) in enumerate(username):
            if ch in sp:
                raise UsernameContainsIllegalCharacter(i)

        if len(username) < 3:
            raise UsernameTooShort(username)

        if len(username) > 16:
            raise UsernameTooLong(username)

        if not all(rule(password) for rule in rules):
            raise PasswordMissingCharacter(password)

        if len(password) < 8:
            raise PasswordTooShort(password)

        if len(password) > 40:
            raise PasswordTooLong(password)
    
    except UsernameContainsIllegalCharacter as e:
        print(e)
    
    except UsernameTooShort as e:
        print(e)
    
    except UsernameTooLong as e:
        print(e)

    except PasswordMissingCharacter as e:
        print(e)

    except PasswordTooShort as e:
        print(e)
    
    except PasswordTooLong as e:
        print(e)

    else:
        return "ok"



# for (i, ch) in enumerate("erez@#$#@"):
#     print(i, ch)

def main():
    # check_input("1", "2")
    # check_input("0123456789ABCDEFG", "2")
    # check_input("A_a1.", "12345678")
    # check_input("A_1", "2")
    # check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    # check_input("A_1", "abcdefghijklmnop")
    # check_input("A_1", "ABCDEFGHIJLKMNOP")
    # check_input("A_1", "ABCDEFGhijklmnop")
    # check_input("A_1", "4BCD3F6h1jk1mn0p")
    # check_input("A_1", "4BCD3F6.1jk1mn0p")

    def set_username():
        print('Enter username')
        user = input()
        return user

    def set_password():
        print("Enter password")
        password = input()
        return password


    user = set_username()
    password = set_password()
    check_input(user, password)
    

    # print(out)
    # couter = 0
    # while out != "ok":
    #     couter += 1
    #     if couter == 5 or out == "ok" :
    #         break
    #     out = check_input(set_username(),set_password())



main()


def tests(var="test"):
    # s = 'fooBar'
    s = 'BBbBBB'
    # s_split = s.split("")
    # l = [x.isupper() for x in s]
    l = [x for x in s]
    # print(any(['A','B','C','D']))
    res = any(x.isupper() for x in l) and any(x.islower() for x in l)



    print(res)




    # if (any(x.isupper() for x in s) and any(x.islower() for x in s):
    #     print() 
    print(any(s.isupper))

    # rules = [
    #     lambda s: any(x.isupper() for x in s) or 'upper',
    #     lambda s: any(x.islower() for x in s) or 'lower',
    #     lambda s: any(x.isdigit() for x in s) or 'digit',
    #     lambda s: len(s) >= 7                 or 'length',
    # ]


    # l = [0,0,1]
    # res = any(l)
    # print(res)
    import string
    password = "sdf$@dsfsD1df"
    sp = string.punctuation
    # print(s in sp)
    def get_bool(str_item):

        res = [x in sp for x in str_item ]
        return any(res)

    # print(get_bool(password))

    # res = lambda x: (x in sp for x in password) (password)
    # print(res)


    # print(sp in password)



    # res = lambda password: any(x in sp for x in password)
    # print(list(res))
    # string.punctuation
    rules = [lambda password: any(x.isupper() for x in password), # must have at least one uppercase
            lambda password: any(x.islower() for x in password),  # must have at least one lowercase
            lambda password: any(x.isdigit() for x in password),  # must have at least one digit
            lambda password: len(password) >= 7                   # must be at least 7 characters
            ]
    print(list(rules))
    res = all(rule(password) for rule in rules)
    print(res)
        # rules = [lambda password: any(x.isupper() for x in password), # must have at least one uppercase
        #     lambda password: any(x.islower() for x in password),  # must have at least one lowercase
        #     lambda password: any(x.isdigit() for x in password),  # must have at least one digit
        #     lambda password: any(x.isdigit() for x in password),
        #     lambda password: len(password) >= 8,                   # must be at least 8 characters
        #     lambda password: len(password) <= 40
        #     ]

    import string
    sp = string.punctuation
    s = "SSS1@SSS"
    # res = any(x.isupper() for x in s)
    # print(res)
    def get_bool(str_item):
        res = [x in sp for x in str_item ]
        return res

    rules = [lambda x: any(x.isupper() for x in s), # must have at least one uppercase
            lambda x: any(x.islower() for x in s),  # must have at least one lowercase
            lambda x: any(x.isdigit() for x in s),  # must have at least one digit
            lambda x: any(get_bool(s))
            # lambda x: any(lambda x: x in sp for x in s)
            # lambda s: len(s) >= 7                   # must be at least 7 characters
            ]


    l = [rule(s) for rule in rules]
    print(l)

    # print(rule(s))

    res = all(rule(s) for rule in rules)
    print(res)