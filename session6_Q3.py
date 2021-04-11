def compcost(gal):
  cost = gal * 2.5
    
  return cost

def compmpg(miles, gal):
  mpg = miles / gal
    
  return mpg

desCity = str(input("Enter Destination: "))
miles = float(input("Enter miles: "))
gal = float(input("Enter gallons: "))
compmpg(miles, gal)
mpg = compmpg(miles, gal)
cost = compcost(gal)
print("Destination city: " + desCity)
print("Miles travelled: " + str(miles))
print("Cost of gas: $" + str(cost))
