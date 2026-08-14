n=int(input("Enter the number of students:"))
registrations=set()
for _ in range(n):
    student_id = input("Enter id:").strip()
    registrations.add(student_id)

search_id = input("Enter id to search:").strip()

unique_count = len(registrations)
duplicate_count = n - len(registrations)

print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")