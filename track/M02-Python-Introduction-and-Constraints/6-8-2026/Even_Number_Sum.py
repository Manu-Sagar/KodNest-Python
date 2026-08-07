limit=int(input("Enter the limit:"))
sum=0
num=1
while num<=limit:
    if(num%2==0):
        sum=sum+num
    num=num+1
print("Sum of even numbers:",sum)