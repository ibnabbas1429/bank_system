#Creating the system layout of basic Operations

#creating each session with a function
def init():
    "This function start the system"
     
    print ("Welcome to bankPHP")

    
    haveAccount = int(input("Do you have account with us: 1(yes) 2(no)\n" ))
    if (haveAccount == 1):
        
        login()

    elif(haveAccount == 2):
        register()
        
    else:
        print("Invalid option selected")



#the initialisation system


#the login system
def login():
    "This function enable users to login into the system"

#the registration system

def register():
    "This function enable a user to register"

#the banking operation system

def bankOperation():
    "This function enable customers to carried out each banking operation"
