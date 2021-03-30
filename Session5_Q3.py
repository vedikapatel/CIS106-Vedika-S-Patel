principle = int(input("Enter the Principle: "))
yrMaturity = int(input("Enter the years of Maturity: "))

if principle > 100000 and yrMaturity == 5:
  intRate = 0.06
elif principle >= 50000 and principle <= 100000 and yrMaturity == 10:
  intRate = 0.05
elif principle >= 50000 and principle <= 100000 and yrMaturity == 5:
  intRate = 0.04
else:
  intRate = 0.02

intAmt = principle * intRate

intRate = intRate * 100

print("Principle:      $",principle)
print("Interest Rate:  $",intRate, "%")
print("Interest amount for the first year: $",intAmt)