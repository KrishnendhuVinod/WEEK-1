#Create a class named Bank
class Bank:
    #Initialize Constructor
    def __init__(self):
        name = input("Enter your name : ")
        self.name = name
        self.balance = 0
        print("Account is created Successfully!")
    
    #Method for depositing
    def deposit(self):
        amount=float(input("Enter the amount you want to deposit: "))
        if amount< 0:
            print("Invalid")
        else :
          self.balance+=amount
          print(f"{amount} deposited .")

    #Method for withdrawing
    def withdraw(self):
        w=float(input("Enter the amount you want to withdraw : "))
        if w>=self.balance :
            print("Insufficient balance .")
            return
        else :
            self.balance-=w
            print("Amount have been withdrawed.")

    #Method of checking balance 
    def bal(self):
        print("Your account balance is %f" %self.balance)
        return
    
#Create object
ac=Bank()

#Initialize loop
while True:
 print("Select your option")
 print("1.Deposit\n" \
   "2. Withraw\n" \
   "3. Check Balance\n" \
   "4. Exit")
 
 choice= input("Enter your option : ")
 if choice=='1':
     ac.deposit()
 elif choice =='2':
     ac.withdraw()
 elif choice =='3':
     ac.bal()
 elif choice=='4':
     print("Exiting")
     break
 else :
     print("Invalid choice")


        

