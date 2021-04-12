total = 0
tax = 0
def comptotal(qty, unitPrice):
  total = qty * unitPrice
    
  return total

def comptax(qty, unitPrice):
  tax = qty * unitPrice * 0.07
    
  return tax

qty = float(input("Enter the quantity: "))
unitPrice = float(input("Enter the unit price: "))
comptotal(qty, unitPrice)
total = comptotal(qty, unitPrice)
comptax(qty, unitPrice)
tax = comptax(qty, unitPrice)
print("Total: $" + str(total))
print("Tax: $" + str(round(tax,2)))