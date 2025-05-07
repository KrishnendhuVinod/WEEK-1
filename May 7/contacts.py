#Import JSON module
import json
c = {} #Initialize dictionary to store contacts

#Define function to display contact
def dis_contact():
    if not c:
        print("No contacts found")
    else:
         print("Your Contacts ")
         for name,phone in c.items():
            print(f"{name} : {phone}")

#Initialize loop for prompting user to give input
while True:
  print("PICK ANY OF THE GIVEN OPTIONS ")
  print("1. Add contact\n" \
        "2. Save contact\n" \
        "3. Load contact\n" \
        "4. Display contact\n"\
        "5. Exit")
  choice = input("Enter your choice : ")
  #Take inputs from user
  if choice == '1':
        name = input("Enter the name : ")
        phone = int(input("Enter the phone number :"))
        c[name] = phone
  #Save contacts into a file
  elif choice =='2':
      f= open("contact.txt","w")
      json.dump(c,f) #Write dictionary 'c' to file in JSON format
      f.close()
      print("Contacts are saved in the contact.txt file")
  #Load contacts from file
  elif choice =='3':
      x=open("contact.txt","r")
      c = json.load(x) #Read JSON data from file and load it to dictionary 'c'
      x.close()
      print("Contacts are loaded")
  #Call function to display contact
  elif choice =='4':
      dis_contact()
  #Exit
  elif choice =='5':
      print("Exiting")
      break #Break the loop
  else :
      print("Invalid choice")
      
      

      
        
        
