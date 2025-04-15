# Full name: David Nguyen
# GSU Email: tnguyen648@student.gsu.edu

while True:
    # Ask user to enter a password.
    Password = input("Enter your password:")
    # Verify if the password has at least 15 characters.
    if len(Password) >= 15:
        print("Correct, Password contains at least 15 characters.")
    else:  
        print("Try again, Password must be at least 15 characters long.")
    # Verify if the password starts with a letter.
    if Password [0].isalpha ():
        print ("Correct, Password starts with a letter.")
    else:
        print ("Try again, password does not start with a letter.")
    # Verify if the password has at least one lower case letter.
    check_lower = False
    for chr in Password:
        if chr.islower ():
            check_lower = True
            break
        
    if check_lower == False:
        print ("Try again, There is no lowercase letter in the password.")
    else:
        print ("Correct, Password contain at least one lowercase letter.")
    # Verify if the password has at least one upper case letter.
    check_upper = False
    for chr in Password:
        if chr.isupper ():
            check_upper = True
            break
    
    if check_upper == False:
        print ("Try again, There is no uppercase letter in the password.")
    else:
        print ("Correct, Password contain at least one uppercase letter.")
    # Verify if the password has at least one number.
    Num = False
    for chr in Password:
        if chr.isdigit ():
            Num = True
            break
    if Num == False:
        print ("Try again, There is no number in the password.")
    else:
        print ("Correct, Password contain at least one number")
    # Verify if the password excludes any of these special characters: @ / ( ) " ' `
    ban_char = '@/()"\'`'
    has_banChar = False
    for chr in Password:
        if chr in ban_char:
            has_banChar = True
            break
    
    if has_banChar == False:
        print ("Correct, there are no @ / ( ) \" ' ` in the password.")
    else:
        print ("Try again, Password must not contain: @ / ( ) \" ' `")
    
    if (len (Password) >= 15 and Password[0].isalpha() and check_lower == True and check_upper == True and Num == True and has_banChar == False):
        # Ask user to type a valid password a second time and verify if it is the same as previous one.
        confirm_password = input("Re-enter your password to confirm:")
        if Password == confirm_password:
            print("Password successfully created!")
            break  
        else:
            print("Passwords do not match. Try again.")
    else:
        print("Try again, Password does not meet all requirements.")









     
        
