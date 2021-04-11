def comptuition(creditHours, disCode):
  if disCode == "I":
    pch = 250.0
  else:
    if disCode == "O":
      pch = 550.0
    else:
      print("Invalid Code")
  tuition = creditHours * pch
    
  return tuition

lastName = input("Enter last name: ")
creditHours = int(input("Enter credit hours: "))
disCode = str(input("Enter District code(I or O): "))
comptuition(creditHours, disCode)
tuition = comptuition(creditHours, disCode)
print("Last Name: " + lastName)
print("Tuition owed: $", tuition)