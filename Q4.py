nameapl = str(input("Enter the appliance name: "))
apl = float(input("Enter the price of appliance: $"))
if apl >= 1000:
  wrt = apl*0.1
else:
  wrt = apl*0.05
total = apl+wrt
print("Name: " + str(nameapl))
print("Price of the appliance $" + str(apl))
print("Warrentee Cost $" + str(wrt))
print("Total $" + str(total))