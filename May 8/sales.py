#import libraries
import pandas as pd
import csv

df=pd.read_csv("Salesfile.csv")#read file

#function for selecting row and column
def dis_col_row():
    no_col = int(input("Enter the number of columns :"))
    if no_col<=0 or no_col>len(df.columns):
        print(f"Enter valid number. The total number of columns are {len(df.columns)} ")
        return
    no_row=int(input("Enter the number of rows : "))
    if no_row<=0 or no_row>len(df):
        print(f"Enter valid number. The total number of rows are {len(df)}")
        return
    print(df.iloc[:no_row,:no_col])
    
#function for displaying column type
def dis_coltype():
    print(f"Available columns are : ",list(df.columns))
    column=input("Enter the column name : ")
    if column in df.columns:
        print(f"The data type of the {column}column is : {df[column].dtype}")
        return
#function for filtering
def filter():
    print("Available colummns : ",list(df.columns))
    c=input("Enter the column for filtering : ")
    if c not in df.columns:
        print("Invalid")
        return
    r=input("Enter the value in row to filter :")
    fil=df[df[c]==r]
    print("After filtering :",fil)

#function for duplicating rows
def dup_row():
    global df
    print("Current row indices are : ",list(df.index))
    duprow=int(input("Enter the row to duplicate :"))
    if duprow not in df.index:
        print("No such row")
        return
    row_dupli=df.iloc[duprow]
    df=pd.concat([df,pd.DataFrame([row_dupli])],ignore_index=True)
    print("Duplicate row successfully :")
    print(df)

#function for adding new column
def add_col():
    global df
    col_name=input("Enter the name for new column")
    value=[]
    print("Enter values :")
    for i in range(len(df)):
        v=input(f"Row{i} : ")
        value.append(v)
    df[col_name]= value
    print("New column added")
    print(df)

while True:
    print("Select any one of the given choices ")
    print("1. Display the shape of dataset\n" \
    "2.Display custom number of rows and columns\n" \
    "3. Display data type of column \n" \
    "4.Information about dataset\n" \
    "5. Check for missing values\n" \
    "6.Fill missing values\n" \
    "7.Filter\n" \
    "8.Sort\n" \
    "9.Dulicate Row\n" \
    "10 Add column\n" \
    "11.Exit")

    choice = input("Enter your choice :")

    if choice == '1':
        print(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    elif choice == '2':
          dis_col_row()
    elif choice == '3':
        dis_coltype()
    elif choice == '4':
        print(f"Info about dataset is : ")
        df.info()
    elif choice == '5':
        #Check missing values in row and column
        print(f"Missing values per column : {df.isnull().sum()}") 
        print(f"Missing values per rows : {df.isnull().sum(axis=1)}")
    elif choice =='6':
        df_fill=df.fillna("NULL")
        print("Table after filling the missing values :")
        print(df_fill)
    elif choice =='7':
        filter()
    elif choice =='8':
        x = input("Enter the column name to sort :")
        sort=input("Enter 'a' for sorting in ascending order and 'd' for descending order :")
        ascending=True if sort =='a' else False
        s_df=df.sort_values(by=x,ascending=ascending)
        print(s_df)
    elif choice=='9':
        dup_row()
    elif choice=="10":
        add_col()
    elif choice =='11':
        print("Exiting")
        break
    else:
        print("invalid choice")






        
