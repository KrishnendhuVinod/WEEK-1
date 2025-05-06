#Set correct username and password 
crct_username = "Boby"
crct_password = "Boby123"

#Initialize attempt counters 
attempts=0
attempts_limit=3

try:
    #Loop until user reaches the limit
    while attempts < attempts_limit:
        #Take username and password from the user
        username = input("Enter the username : ")
        password = input("Enter your password : ")

        #Check if the username or password is blank
        if not username or not password :
            print("Username or password cannot be blank.")
            attempts +=1 #Increment attempts
            continue
        
        #Check if the username and password matches
        elif username == crct_username and password == crct_password :
            print("LOGIN SUCCESSFULLY!")
            break #Exit the loop
             
        else:
            attempts +=1 #Increment the attempts 
            #Notify if the username or password is incorrect
            print(f"Incorrect Username or Password. You have only {attempts_limit - attempts} attempt(s) left.")
    
    #If the user reaches the limit block them with a warning message
    if attempts==attempts_limit :
        print("Too many failed attempts. Try again after 30 minutes")
#Catch any unexpected runtime error
except Exception as e:
    print(f"Unexpected error {e} occurs.")