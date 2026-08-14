skills=[]
for i in range(5):
    skills.append(input())

skills_tuple=tuple(skills)
print(f"Complete Record: {skills_tuple[:]}")
print(f"First Three: {skills_tuple[:3]}")
print(f"Last Two:{skills_tuple[-2:]}")
print(f"Alternate Skills: {skills_tuple[::2]}")
print(f"Reverse Skills: {skills_tuple[::-1]}")