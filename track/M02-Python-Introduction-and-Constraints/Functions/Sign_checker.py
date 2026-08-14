def check_sign(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
num=int(input("Enter Number:"))
print(check_sign(num))