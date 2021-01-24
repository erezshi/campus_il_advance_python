#How to handle exception
# Can write if statments to catch and andle 
# or guess the execptions

# try:
#     "Here we put the code that migh breach"
# except ExceptionName:
#     "Here we add code in case of exception"
# else:
#     "This code will run only if try run succesfully"
# finally:
#     "This will always run"


number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
try:
    print("The result is: " + str(number_1 / number_2))
except ZeroDivisionError as e:
    print("Cannot divide the provided input.")
    print(e)
except ValueError as e:
    print("can't use literals.")
    print(e)

