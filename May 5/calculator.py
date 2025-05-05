def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0 :
        return "Invalid"
    return a/b

print("Enter numbers :")
a = float(input("Enter a : "))
b = float(input("Enter b :"))

print("Select operator")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter the choice :")

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