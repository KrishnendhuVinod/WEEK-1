#Function to add 2 numbers
def add(a,b):
    return a+b
#Function to subtract 2 numbers
def sub(a,b):
    return a-b
#Function to multiply 2 numbers
def mult(a,b):
    return a*b
#Function to divide 2 numbers
def div(a,b):
    if b==0 :
        return "Invalid"
    return a/b

# Prompt user to enter numbers
print("Enter numbers :")
a = float(input("Enter a : "))
b = float(input("Enter b :"))

#Display operations
print("Select operator")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

#Take a choice from the user 
choice = input("Enter the choice :")

#Do operation based on the choice
if choice=='1':
    print(a ,"+" ,b ,"=" , add(a,b))
elif choice=='2':
    print(a , "-" , b , "=" , sub(a,b))
elif choice=='3':
    print(a , "*" , b , "=" , mult(a,b))
elif choice=='4':
    print(a , "/" , b , "=" , div(a,b))
else:
    print("Invalid choice")