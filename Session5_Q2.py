partnum = int(input("Enter the part number "))
qty = input("Enter quantity to purchase ")

if partnum == 10 or partnum ==55:
  unitprice = 1.00
elif partnum == 99:
  unitprice = 2.00
elif partnum == 70 or partnum ==80:
  unitprice = 3.00
else:
  unitprice = 5.00

total = float(qty) * unitprice

print ("Part number:   ", partnum)
print ("Unit price:    ", unitprice)
print ("Total:         ", total)