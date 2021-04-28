def compBonus(salary):
  bonus = (float(salary) * 10)/100
  return bonus

f = open("session9_Q3.txt", "r")

totBonus = 0

lastName = f.readline()

while lastName != "":
  salary = f.readline()
  print()
  print("Employee Last Name:", lastName)
  print("Employee Salary: $"+ str(format(float(salary),'0,.2f')))
  bonus = compBonus(salary)
  print("Employee Bonus: $"+ str(format(float(bonus),'0,.2f')))
  totBonus = totBonus + bonus
  lastName = f.readline()

f.close()
print()
print("Total bonus paidout: $"+ str(format(float(totBonus),'0,.2f')))
  