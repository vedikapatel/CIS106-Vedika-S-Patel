ln = str(input("Enter your Last Name: "))
numdep = int(input("Enter the number of dependents: "))
grsinc = float(input("Enter your gross income $"))
adjinc = grsinc-numdep*12000
if adjinc > 50000:
  taxrate = 0.20
else:
  taxrate = 0.10
inctax  = adjinc*taxrate
if inctax < 0:
  inctax = 100
print("Last Name: " + str(ln))
print("Gross Income $" + str(grsinc))
print("Number of dependents: " + str(numdep))
print("adjusted Gross Income $" + str(adjinc))
print("Income Tax $" + str(inctax))