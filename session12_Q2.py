class Student:

  def __init__(self, first, last, district, credit):
      self.first = first
      self.last = last
      self.district = district
      self.credit = credit

  def tuition_owed(self):
    if self.district == "I":
      self.tuition = (int(self.credit * 250))
    else:
      self.tuition = (int(self.credit * 500))

stu_1 = Student('Vedika', 'Patel', 'I', 12)
stu_2 = Student('Test', 'User', 'O', 9)

print("Student Name:", stu_1.first, stu_1.last,)
print("Student District: ", stu_1.district)
print("Credit Taken: ", stu_1.credit)
stu_1.tuition_owed()
print("Tuition Owed: $" + str(stu_1.tuition))
print()
print("Student Name:", stu_2.first, stu_2.last,)
print("Student District: ", stu_2.district)
print("Credit Taken: ", stu_2.credit)
stu_2.tuition_owed()
print("Tuition Owed: $" + str(stu_2.tuition))