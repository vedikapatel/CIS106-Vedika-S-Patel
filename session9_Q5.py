def compTuition(credit):
  tuition = float(credit) * 250.00
  return tuition

f = open("session9_Q5.txt", "r")

totTuition = 0

totStudent = 0

lastName = f.readline()
totStudent +=1

while lastName != "":
  credit = f.readline()
  print()
  print("Student Last Name:", lastName)
  print("Student Credit taken:", credit)
  tuition = compTuition(credit)
  print("Tuition owed: $"+ str(format(float(tuition),'0,.2f')))
  totTuition = totTuition + tuition
  lastName = f.readline()
  totStudent +=1 
f.close()
print()
print("Total tuition owed for all: $"+ str(format(float(totTuition),'0,.2f')))
print("Number of Students:", totStudent)