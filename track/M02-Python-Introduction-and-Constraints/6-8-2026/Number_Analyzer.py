num=int(input("Enter the Number:"))
positive_count=0
negative_count=0
zero_count=0
total=0
for i in range(0,num):
    val=int(input())
    if(val>0):
        positive_count+=1
    elif(val<0):
        negative_count+=1
    else:
        zero_count+=1
    total+=val
print("Positive Count:",positive_count)
print("Negative Count:",negative_count)
print("Zero Count:",zero_count)
print("Total:",total)