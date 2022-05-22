def accountNumber_validation(user_inputted_account_number):
    #if account number is not empty
    #if account number is 10 digits
    #if ccount is an integer
    if user_inputted_account_number :
        if len(str(user_inputted_account_number == 10)):
            try: 
                int(user_inputted_account_number)
                return True
            except ValueError:
                #print("Invalid Account number, Account number should an integer")
                return False

            except TypeError:
                
                print("Invalid account number format")
                return False 

            login()
        else:
            print("Account Number cannot be more than 10 digits")
            return False
    else:
        print("Account number is required field")
        return False
