#This is a simple banking system implemented in python. 
#It used a account number and password to login in to the system.
# It performs the basic banking operations2221.

#bank operation

""""Use input validation ensuring it is what
 will want a user to input that is inputted"""
import random

import validation

import datafile


def init():

    #This is a function that initialized our system

    selectedOptionIsCorrect = False

    print ("Welcome to ApexBank of Nigeria")

    while selectedOptionIsCorrect == False:
        haveAccount = int(input("Do you have account with us: 1(yes) 2(no)\n" ))
        if (haveAccount == 1):
            selectedOptionIsCorrect = True
            
            login()

        elif(haveAccount == 2):
            selectedOptionIsCorrect = True
            register()
        
        else:
            print("Invalid option selected")


#Create a function for login into our system

def login():
    # account number  and password
    print("LOGIN TO YOUR ACCOUNT")

    user_inputted_account_number = input("Please Enter Your Account  NUmber. \n")
    isAccountNumberValid = validation.accountNumber_validation(user_inputted_account_number)
    
    if isAccountNumberValid:
        password = input( "Enter your password \n")

        user = datafile.verified_user(user_inputted_account_number,password)

        if user:
            bankOperation(user)

        
        print("invalid account number")

        login()
    else:
        print("Account Number Invalid: Check that you have up to 10 digits and only integer")
        init()
   


# create the function for registration 

def register():
    
    print("************ Register**************")
    first_name = input("please enter your first name \n" )
    last_name = input("please enter your first name \n" )
    email = input("please enter your email \n" )
    password = input("Creat a password \n")
    try:
        
        accountNumber = accountNumberGenerator()

    except ValueError:
        print("Account generation failed, No internet connection failure")
        init()
   

    is_user_created = datafile.create(accountNumber,first_name, last_name, email, password)

   

    print("You account has been created")

    print (f"You account number is {accountNumber} \n Please keep it self \n *********************Login************************")

    login()



#Create a function for the basic operation of our banking system

def bankOperation(user): 
    print("Welcome %s  %s" % ( user[0], user[1] ))

    balance = 10000
    
    selectedOption = input("What will you like to do? \n (1) deposite \n(2) withdrawal \n(3) Complaint \n(4) Logout \n(5) exit() \n")
    
    if (selectedOption == "1"):
        deposit()
        
    elif (selectedOption == "2"):
            
        withdrawal()
        
    elif (selectedOption == "3"):
            
        complaint()
        
    elif (selectedOption == "4"):
            
        logout()
        
    elif (selectedOption == "5"):
            
        exit()
        
    else:
        
        print("Invalid option selected")

        bankOperation(user)

def deposit():

    print("Deposit")


def withdrawal():

    print("Withdrawal")

def complaint():

    print("Complaint")

def logout():

    print("Logout")

def withdrawalOperation():

    exit("Exit")
        

# creating the function for the generation of account system
def accountNumberGenerator():
    
    return random.randrange(111111111,999999999)


print("*************************  ACTUAL BANKING OPERATION  ******************************")
init()