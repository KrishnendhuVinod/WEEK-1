
#Take input from user
x = input("Enter the text :")

#Open a file in write mode
y= open("x.txt","w")
i= y.write(x) #Write the user input and store it in i
y.close() #Close the file

print("Your file is saved as x.txt")

#Open the file in read mode
f=open("x.txt","r")
print("The file contains : ",f.read()) #Read the data in the file and print
f.close() #Close the file