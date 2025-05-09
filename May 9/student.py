#Create class 
class Students:
    #Initialize constructor
    def __init__(self):
        self.student=[] #Inititialize list for storing students data
    
    #Method to add student
    def add(self):
        name=input("Enter the name of the student for adding in the list : ")
        roll=int(input("Enter roll number : "))
        c=input("Enter class :")
        course=input("Enter course ")
        self.name=name
        self.roll=roll
        self.c=c
        self.course=course
        #Create dictionary to save student details
        data={
            "name": name,
            "roll": roll,
            "class" : c,
            "course" : course}
        
        self.student.append(data)
        print("Student is added successfully !")

    #Method for removing
    def remove(self):
        rn=input("Enter the name of student to remove :")
        for a in self.student:
         if a['name']==rn:
            self.student.remove(a)
            print(f"Student named {rn} is removed . ")
            return
        print("Stusent not found")

    #Method for searching student
    def search(self):
        s=int(input("Enter the Roll number of the student to search :"))
        
        for i in self.student:
           if i['roll'] == s:
               print("Student is found")
               print(f"Name :{i['name']}, Roll no:{i['roll']}, Class :{i['class']}, Course :{i['course']}")
               return
           else:
               print("NO student found")

    #Method for displaying all students detail
    def display(self):
        print("Print Students list")
        for j in self.student:
            print(f"Name : {j['name']}, Roll No: {j['roll']}, Class : {j['class']}, Course :{j['course']}")
            
#Create object
std=Students()
while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. Add student\n" \
    "2. Remove Student\n" \
    "3. Search student\n" \
    "4. Display list of students\n" \
    "5.Exit")

    choice=input("Enter your choice :")
    if choice =='1':
        std.add()
    elif choice =='2':
        std.remove()
    elif choice=='3':
        std.search()
    elif choice =='4':
        std.display()
    elif choice =='5':
        print("EXITING...")
        break
    else:
        print("Invalid choice")
                

