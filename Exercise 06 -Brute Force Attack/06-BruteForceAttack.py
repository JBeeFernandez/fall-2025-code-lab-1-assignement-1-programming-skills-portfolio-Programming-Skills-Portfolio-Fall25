# The password
no_clickbait_real_password = "12345"
login = 0
attempt = 0
limit = 5

while login == 0 and attempt < limit:
    
    yourpassword = input("Enter password: ")
    # if the password is correct
    if yourpassword == no_clickbait_real_password:
        login = 1
        # if it's wrong then removes an attempt
    else:
        attempt = attempt + 1
        remain = limit - attempt
        if remain > 0:
            print(f"TRY AGAIN! You only have {remain} attempts remaining. >:)")
if login == 1:
    print("Entering the super duper secret files huehuehue...")
else:
    print("Password Incorrect >:C. Authorities have been alerted")