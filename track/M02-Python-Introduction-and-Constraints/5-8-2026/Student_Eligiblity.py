Marks=int(input("Enter the Marks: "))
Attendance=int(input("Enter the Attendance: "))
Project_Status=input("Enter the Project Status: ")
if(Marks>=60 and Attendance>=75):
    if(Project_Status=="Done"):
        print("Student is Eligible")
    else:
        print("Student is Not Eligible")
else:
    print("Student is Not Eligible")
    