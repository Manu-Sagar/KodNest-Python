student_count=int(input("Enter Student Count:"))

passed_count=0
failed_count=0
total_marks=0
for i in range(student_count):
    marks=int(input("Enter the marks:"))
    total_marks+=marks
    if(marks>=40):
        passed_count+=1
    else:
        failed_count+=1
    
print("Total marks:",total_marks)
print("Passed_count:",passed_count)
print("Failed_count:",failed_count)