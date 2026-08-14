def display_invoice_total(quantity,price):
    total=quantity*price
    print("Total:",total)
quantity=int(input("Enter Quantity:"))
price=int(input("Enter Price:"))
display_invoice_total(quantity,price)