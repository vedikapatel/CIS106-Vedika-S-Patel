grades = ["A", "B", "C", "A", "A", "C"]
print(grades)
look_for = "F"
if look_for in grades:
  print("First F in the list:", grades.index(look_for))
else:
  print("F is not in the grade lsit")