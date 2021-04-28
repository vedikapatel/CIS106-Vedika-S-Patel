def compExtPrice(qty, price):
  extPrice = int(qty) * int(price)
  return extPrice

f = open("session9_Q4.txt", "r")

totExtPrice = 0

totCount = 0

item = f.readline()
totCount +=1

while item != "":
  qty = f.readline()
  price = f.readline()
  print()
  print("Item:", item)
  print("Quantity:", qty)
  print("Price of an item: $"+ str(format(float(price),'0,.2f')))
  extPrice = compExtPrice(qty, price)
  print("Extended Price: $"+ str(format(float(extPrice),'0,.2f')))
  totExtPrice += extPrice
  item = f.readline()
  if(item != ""):
    totCount +=1 
f.close()
print()
print("Total of all Extended Price: $"+ str(format(float(totExtPrice),'0,.2f')))
print("Total Number of Orders: "+ str(totCount))
avgOrder = totExtPrice / totCount
print("Average Order: $"+ str(format(float(avgOrder),'0,.2f')))