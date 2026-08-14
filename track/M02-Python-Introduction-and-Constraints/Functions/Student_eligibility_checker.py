def check_eligibility(marks, attendance, project_completed):
    if marks >= 60:
        if attendance >= 75:
            if project_completed == "yes":
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False

    if result == True:
        return "Eligible"
    else:
        return "Not Eligible"


# Read the student's details
marks = int(input())
attendance = int(input())
project_completed = input().strip().lower()

# Call the function and print the returned result
result = check_eligibility(marks, attendance, project_completed)
print(result)