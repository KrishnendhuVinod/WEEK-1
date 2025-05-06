# Define a function to check if the string is palindrome
def is_palindrome(s):
    #Return true if the string is equal to its reverse
    return s == s[::-1]

#Take input from user , remove spaces and convert it into lowercase.
s = input("Enter the string : ").replace(" ","").lower()

#Call the fuction
if is_palindrome(s):
   print("The string is palindrome.")
else :
    print("The string is not palindrome")