class UnderAge(Exception):

    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"Sorry {self._arg} is too young...\nPlease come back in {18-self._arg} years "

    def get_arg(self):
        return self._arg


def send_invitations(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


send_invitations("Erez", 10)