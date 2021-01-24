

# def polidrom(var):
#     l = len(var)
#      s:[1] = s:[-1]
#      s:[2] = s:[] 

# s = "abcbd"
# print(s[-2])
def polidrom(arg):
    for n in range(len(arg)):
        t = n + 1
        if s[n] == s[-t]:
            print("pass")
            break
        else:
            return true

def testpol(arg):
    result = False
    for i in range(len(arg)):
        t = i + 1
        if arg[i] != arg[-t]:
            break
        else:
            result = True
    return result

# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# s = "ABCBA"
s ="ABCDEF"
ans = isPalindrome(s)

if ans:
    print("yes")
else:
    print("no")




# print(testpol("abcbb"))  
# isPalindrome("12321")  



        

