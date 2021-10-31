#login
"""
This is a simple bank authentication system in python
"""
# using email or username and password as the authentication parameter 

#bank operation
import random

database = {}

def init():

    
    selectedOptionIsCorrect = False
    print ("Welcome to bankPHP")

    while selectedOptionIsCorrect == False:
        haveAccount = int(input("Do you have account with us: 1(yes) 2(no)\n" ))
        if (haveAccount == 1):
            selectedOptionIsCorrect = True
            #
            login()

        elif(haveAccount == 2):
            selectedOptionIsCorrect = True
            register()
        
        else:
            print("Invalid option selected")


# creat the registration


def login():
    print("LOGIN TO YOUR ACCOUNT")
    bankOperation()

def register():
    
    print("************ Register**************")
    first_name = input("please enter your first name \n" )
    last_name = input("please enter your first name \n" )
    email = input("please enter your email \n" )
    password = input("Creat a password \n")
    accountNumber = accountNumberGenerator()
    database[accountNumber] = [first_name, last_name, email, password]
    

    print("You account has been created")

    login()



def bankOperation():
    print("Welcome how can we help you")

def accountNumberGenerator():
    #print("This is you account number")
    return random.randrange(111111111,999999999)


print("*************************  ACTUAL BANKING OPERATION  ******************************")
init()
