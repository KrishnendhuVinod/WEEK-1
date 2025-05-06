secret_no = 4   # Set the secret number
guess =""       # Variable to store user guesses
guess_count = 0 #Counter to track the number of guesses
guess_limit = 5 #Maximum number of guesses
out_of_guess = False  # Flag to check if the user runs out of guesses


print("Number Guessing Game ")
print("HINT : The secret number is between 1 and 10")

#Loops until the user guesses correctly or runs out of guesses
while guess != secret_no and not out_of_guess:
    if guess_count<guess_limit:
    # Take user input and increment guess count
     guess= float(input("Enter your guess : "))
     guess_count+=1
    else :
    # If the guess limit is reached, set out_of_guess to true
       out_of_guess=True

if out_of_guess:
   print("Out of tries . YOU LOSE!!")
else:
 print("YOU WIN!!!")

