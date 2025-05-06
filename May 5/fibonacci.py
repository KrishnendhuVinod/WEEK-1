#Take input from the user 
n= int(input("Enter how many terms you want in fibonacci sequence : "))
a=0 #Initialize 1st term as 0
b=1 #Initialize 2nd term as 1
count=0 # Variable to store the current Fibonacci number

# Check the user input is valid 
if n<=0 :
    print("Please enter number greater than 0")
else :
   print("The fibonacci sequence : ")

#Loop to generate and print the Fibonacci sequence
for i in range(0, n):
    print(count,end=' ')
    #Update values
    a=b
    b= count
    count = a+b