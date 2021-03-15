item = (input("Enter the item(A or B): "))
quantity = int(input("Enter the quantity of the item: "))
if item == "A":
  unitprice = 10
else:
 unitprice = 20
extprice = quantity*unitprice
print("Item = " + str(item))
print("Unit Price $" + str(unitprice))
print("Extended Price $" + str(extprice))