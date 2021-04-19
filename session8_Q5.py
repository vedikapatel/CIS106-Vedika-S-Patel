prog = input("Do you want to compute income tax? (Yes/No) ")
while prog == "Yes":
  grossInc = float(input("Enter the Gross Income: "))
  if grossInc > 500000:
    taxRate = 30
    taxOwed = grossInc * taxRate / 100
  else:
    if grossInc > 200000 and grossInc < 500000:
      taxRate = 20
      taxOwed = grossInc * taxRate / 100
    else:
      taxRate = 15
      taxOwed = grossInc * taxRate / 100
  print("Gross Income: $" + str(grossInc))
  print("Tax Rate: " + str(taxRate))
  print("Tax owed: $" + str(taxOwed))
  prog = input("Do you want to do the computation again? (Yes or No) ")
