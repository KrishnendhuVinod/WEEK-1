secret_no = 4
guess=""
guess_count = 0
guess_limit = 5
out_of_guess = False
print("Number Guessing Game ")
print("HINT : The secret number is between 1 and 10")

while guess != secret_no and not out_of_guess:
    if guess_count<guess_limit:
     guess= float(input("Enter your guess : "))
     guess_count+=1
    else :
       out_of_guess=True

if out_of_guess:
   print("Out of tries . YOU LOSE!!")
else:
 print("YOU WIN!!!")

