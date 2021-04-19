prog = input("Do you want to do this program? (Y or N) ")
while prog == "Y":
  item = input("Enter the item: ")
  price = float(input("Enter the price: "))
  qty = int(input("Enter quantity: "))
  extPrice = qty * price
  if extPrice > 10000:
    disAmt = extPrice * 0.1
  else:
    if extPrice > 5000:
      disAmt = extPrice * 0.05
    else:
      disAmt = extPrice * 0.02
  disPrice = extPrice - disAmt
  tax = disPrice * 0.07
  print("Extended Price: $" + str(extPrice))
  print("Discounted Amount: $" + str(disAmt))
  print("Discounted Price: $" + str(disPrice))
  print("Tax: $" + str(round(tax,2)))
  prog = input("Do you want to do this program? (Y or N) ")
