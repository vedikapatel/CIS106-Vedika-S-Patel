def compcom(sales):
  if sales > 100000.0:
    com = sales * 0.1
  else:
    com = sales * 0.05
    
  return com

def compnextYrTarget(sales):
  nextYrTarget = sales * 0.05 + sales
    
  return nextYrTarget

lastName = input("Enter sales person last name: ")
sales = float(input("Enter the sales: $"))
compcom(sales)
com = compcom(sales)
compnextYrTarget(sales)
nextYrTarget = compnextYrTarget(sales)
print("Sales person last name: " + lastName)
print("Commission: $" + str(com))
print("Next year's target: $" + str(nextYrTarget))