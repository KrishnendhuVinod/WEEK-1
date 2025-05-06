#Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c*9)/5+32
#Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f-32)*5/9
try:
    print("Choose one of the options :")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    #Take choice from user
    choice = int(input("Enter your choice :"))
    
    #Convert Celsius to Fahrenheit
    if choice == 1:
        c= float(input("Enter the temperature in Celsius :"))
        print(f"{c}°C is equal to {celsius_to_fahrenheit(c)}°F")
        
    #Convert Fahrenheit to Celsius
    elif choice ==2:
        f= float(input("Enter temperature in Fahrenheit : "))
        print(f"{f}°F is equal to {fahrenheit_to_celsius(f)}°C")
    else :
        print("Invalid choice")
        
# Handle case when user enters non-numeric input
except ValueError:
    print("Invalid input")
# Handle any other unexpected error
except Exception as e:
    print(f"Unexpected runtime error occurs.")