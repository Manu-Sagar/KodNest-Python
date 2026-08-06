limit=int(input())
target=int(input())
count=0
total=0
found=False
for i in range(1,limit+1):
    if(i%3==0):
        if(i==target):
            found=True    
        count+=1
        total+=i
if(found):
    print("Target Found")
else:
    print("Target not found")
print("Count of multiples:",count)
print("Sum of multiples:",total)