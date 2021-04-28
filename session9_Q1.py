def compannInt(prinAmt, intRate):
  annInt = prinAmt * intRate
    
  return annInt

prinAmt = float(input("Please enter the principle amount. "))
intRate = float(input("Please enter the interest rate."))
sumInt = 0
for yr in range(1, 5 + 1, 1):
  annInt = compannInt(prinAmt, intRate)
  endBal = prinAmt + annInt
  sumInt = sumInt + annInt
  print("Year: " + str(yr))
  print("Beginning Balance: $" + str(prinAmt))
  print("Ending Balance: $" + str(endBal))
  yr = yr
  prinAmt = endBal
  sumInt = sumInt
print("Total interest rate: $" + str(sumInt))
