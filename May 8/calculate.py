import pandas as pd
import csv
import numpy as np

#read file
df=pd.read_csv("Salesfile.csv")

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
    col_name=input("Enter the name for new column:")
    value=[]
    print("Enter values :")
    for i in range(len(df)):
        v=input(f"Row{i} : ")
        value.append(v)
    df[col_name]= value
    print("New column added")
    print(df)


#function for calculating mean,median and standard deviation
def cal():
    clmn=df.select_dtypes(include=[np.number]).columns.tolist()
    if not clmn:
        print("No numeric columns are there")
        return
    print("Numeric column names are :",clmn)
    inp =input("Enter the column name you want to calculate :")
    if inp not in clmn:
        print("Enter valid column name")
        return
    cl_data=df[inp].dropna()
    mean_cl=np.mean(cl_data)
    median_cl=np.median(cl_data)
    sd_cl=np.std(cl_data)
    print(f"Mean :{mean_cl}")
    print(f"Median :{median_cl}")
    print(f"Standard Deviation :{sd_cl}")
    
while True:
    print("Select any one of the given choices ")
    print(
    "1.Display custom number of rows and columns\n" \
    "2. Check for missing values\n" \
    "3.Fill missing values\n" \
    "4.Dulicate Row\n" \
    "5. Add column\n" \
    "6.Calculate mean,median and standard deviation\n" \
    "7.Exit")

    choice = input("Enter your choice :")

    if choice == '1':
        dis_col_row()
    elif choice == '2':
        print(f"Missing values per column : {df.isnull().sum()}")
        print(f"Missing values per rows : {df.isnull().sum(axis=1)}")
    elif choice =='3':
        df_fill=df.fillna("NULL")
        print("Table after filling the missing values :")
        print(df_fill)
    elif choice=='4':
        dup_row()
    elif choice=="5":
        add_col()
    elif choice =='6':
        cal()
    elif choice =='7':
        print("Exiting")
        break
    else:
        print("invalid choice")






        
