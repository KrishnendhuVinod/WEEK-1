#import neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#Create class
class Data:
    #Initialize constructor
    def __init__(self):
        self.data=None
    
    #Method for loading file
    def load(self):
        self.data = pd.read_csv("cs.csv")
        print("Data loaded successfully ")
        print(self.data)

    #Method for processing data
    def process(self):
        if self.data is None or self.data.empty:
            print("No data")
            return
        while True:
            print("PROCESS DATA ")
            print("1. Show summary\n"\
            "2. Add column\n"\
           "3. Duplicate row\n"\
            "4. Drop column\n"\
            "5. Exit")

            choice = input("Choose option: ")
            #Shows summary of dataset
            if choice == '1':
                print("\nSummary statistics:")
                print(self.data.describe())
            #Add column
            elif choice =='2':
                col_name = input("Enter the name for new column: ")
                value = []
                print("Enter values:")
                for i in range(len(self.data)):
                  v = input(f"Row {i}: ")
                  value.append(v)
                self.data[col_name] = value
                print("New column added!")
                print(self.data)
            #duplicate row
            elif choice =='3':
                 print("current row indices are :",list(self.data.index))
                 duprow=int(input("Enter the row to duplicate :"))
                 if duprow not in self.data.index:
                    print("No such row")
                    return
                 row_dupli = self.data.iloc[duprow]
                 self.data = pd.concat([self.data, pd.DataFrame([row_dupli])], ignore_index=True)
                 print("Duplicate row successfully :")
                 print(self.data)
            #drop column
            elif choice =='4':
                col=input("Enter the column name to drop : ")
                if col not in self.data.columns:
                    print("Not found")
                    return
                else:
                    self.data = self.data.drop(columns=[col])
                    print(f"Column '{col}' dropped.")
                    print(self.data)
            elif choice=='5':
                print("EXITING..")
                break
            else:
                print("Invalid ")
    #method for plotting 
    def plot(self):
        print("PLOT MENU")
        print("1.Line plot\n" \
        "2.Bar plot\n" \
        "3.Scatter plot\n" \
        "4.Exit")

        p=input("Enter your choice :")
        x_col = input("Enter column name for X-axis: ")
        y_col = input("Enter column name for Y-axis: ")
        if p=='1':
                plt.plot(self.data[x_col], self.data[y_col])
        elif p=='2':
                plt.bar(self.data[x_col], self.data[y_col])
        elif p=='3':
                plt.scatter(self.data[x_col], self.data[y_col])
        elif p=='4':
            print("Exiting...")
            return
        else:
                print("Invalid choice")
                return
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"{y_col} vs {x_col}")
        plt.show()

#Create object
d=Data()

while True:
    print("\nDATA ANALYSIS SYSTEM")
    print("1. Load CSV file")
    print("2. Process Data")
    print("3. Plot Data")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        filename = input("Enter CSV filename: ")
        d.load()
    elif choice == '2':
        d.process()
    elif choice == '3':
        d.plot()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
            

