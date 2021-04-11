def compgrossPay(hoursWork, payRate):
  if hoursWork > 40:
    grossPay = (hoursWork - 40) * payRate * 1.5 + 40 * payRate
  else:
    grossPay = hoursWork * payRate
    
  return grossPay

def comppayRate(jobCode):
  if jobCode == "L":
    payRate = 25.0
  else:
    if jobCode == "A":
      payRate = 30.0
    else:
      if jobCode == "J":
        payRate = 50.0
      else:
        print(Invalid)
    
  return payRate

lastName = input("Enter Last Name: ")
jobCode = input("Enter Job Code (L, A, or J): ")
hoursWork = float(input("Enter hours worked: "))
comppayRate(jobCode)
payRate = comppayRate(jobCode)
compgrossPay(hoursWork, payRate)
grossPay = compgrossPay(hoursWork, payRate)
print("Last Name: " + lastName)
print("Gross Pay: $" + str(grossPay))
