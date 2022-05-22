#import banking_system_login_modularised
import os 
import validation
user_db_path = '/home/ibnabbas1429/Desktop/python_projects/bankSystem_datafile/data/user_records/'


def create(accountNumber, first_name, last_name, email, password):
    #return successfulFileCreation 
    #create File and name it
    #add userdetail to file 
    #return true
    # if saving to file delete details file
    
    user_details = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    if find_user_account_number(accountNumber):
        return False

    if find_user_email(email):
        print("User already exist")
        return False
    # = open(user_db_path + str(accountNumber) + ".txt", "x" )
    successfulFileCreation = False

    try:
        
        f = open(user_db_path + str(accountNumber) + ".txt", "x" )
        
    except FileExistsError:

        is_data_in_file = read(user_db_path + str(accountNumber) + ".txt")
        if not is_data_in_file:
            delete(accountNumber)

        print("user already exist")   

    else:
        f.write(str(user_details))
        successfulFileCreation = True
        
    finally:
        f.close()
        return successfulFileCreation 

        
# -(username or emai;) and password
    

def read(accountNumber):
     #return("read data")
     #  search for the file if it exists
     #read the file and fetch the file
     #return true

    #optimising this code to read both a file with txt extension and the one without txt
    
    is_account_number_valid = validation.accountNumber_validation(accountNumber)
    try:
        if is_account_number_valid:
            f = open(user_db_path + str(accountNumber) + ".txt", "r" )
        else:
            f = open(user_db_path + str(accountNumber), "r" )
        
    except FileExistsError:
         print("user doesn't exist")
        
        
    except FileNotFoundError:

        print("user not Found")
    
    except TypeError:
        print("Invalid account number format")

    finally:
        return f.readline()
        return f"user with account {accountNumber} already exist "
        return False

    
def delete(accountNumber):
     # find user account number's
    # delete the user record/file
    # return true
    
    is_delete_successful = False
    if os.path.exists(user_db_path + str(accountNumber) + ".txt"):

        
        try:
            os.remove(user_db_path + str(accountNumber) + ".txt")
            is_delete_successful = True
               
        except FileNotFoundError:
            
            print("user not found")
        
        finally:
            return is_delete_successful 
        
   

def find_user_email(email):
    # searching a user using a particular parameter
    allUsers = os.listdir(user_db_path)

    for user in allUsers:
        user_list = str.split((read(user)), ",")      
        if email in user_list:
            print(email)
            return True

    return False

def find_user_account_number(accountNumber):
    # searching a user using a particular parameter
    allUsers = os.listdir(user_db_path)

    for user in allUsers:
             
        if  user == str(accountNumber)+ ".txt":
            return True
             
    return False
    

def verified_user(accountNumber, password):
    # Verified if the account number exists
    #Verified if the password inputted is correct
    if find_user_account_number(accountNumber):
        user = str.split(read(accountNumber), ",")
        if password == user[3]:
            return user

    return False
    
