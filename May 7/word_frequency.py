
import string

# Open and read the text file
f = open("Myfile.txt","r")
data = f.read() #Store the file in the variable
f.close()

print(data)
 
 #Remove all the punctuations in the text
for char in string.punctuation:
    data = data.replace(char,"")

clean_data = data #Strore the cleaned data in a variable 

#Convert the string into words and store it in a variable
word_list=clean_data.split()
c = {}  # create an empty dictionary to store frequency

#Check is the word is already in the dictionary
for key in word_list:
    if key in c:
        c[key]+=1
    else:
        c[key]=1

#Loop through each word and its frequency
for key,value in c.items():
    print(f"{key} : {value}")