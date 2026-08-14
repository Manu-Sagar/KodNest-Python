from ast import operator
def calc(operator,num1,num2):
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    else:
        print("Invalid Operator")
operator=input("Enter Operator:")
num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
calc(operator,num1,num2)