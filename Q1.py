quantity = int(input("Enter the quantity of the item: "))
if quantity >= 1000:
  rate = 3
else:
 rate = 5
extprice = quantity*rate
tax = extprice*0.07
total = extprice+tax
print("Quantity = " + str(quantity))
print("Unit Price $" + str(rate))
print("Extended Price $" + str(extprice))