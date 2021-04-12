def compdisAmt(qty, price, disRate):
  disAmt = qty * price * disRate / 100
    
  return disAmt

def compdisPrice(qty, price, disAmt):
  disPrice = qty * price - disAmt
    
  return disPrice

qty = float(input("Enter the Quantity: "))
price = float(input("Enter the price: "))
disRate = float(input("Enter the discount rate: "))
compdisAmt(qty, price, disRate)
disAmt = compdisAmt(qty, price, disRate)
compdisPrice(qty, price, disAmt)
disPrice = compdisPrice(qty, price, disAmt)
print("Discount amount: $" + str(disAmt))
print("Discounted price: $" + str(disPrice))