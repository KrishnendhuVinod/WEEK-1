n= int(input("Enter how many terms you want in fibonacci sequence : "))
a=0
b=1
count=0

if n<=0 :
    print("Please enter number greater than 0")
else :
   print("The fibonacci sequence : ")

for i in range(0, n):
    print(count,end=' ')
    a=b
    b= count
    count = a+b


