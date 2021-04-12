def compavg(exam1, exam2, exam3):
  avg = (exam1 + exam2 + exam3) / 3
    
  return avg

def comptotal(exam1, exam2, exam3):
  total = exam1 + exam2 + exam3
    
  return total

lastName = input("Enter last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))
compavg(exam1, exam2, exam3)
avg = compavg(exam1, exam2, exam3)
comptotal(exam1, exam2, exam3)
total = comptotal(exam1, exam2, exam3)
print("Last name: " + lastName)
print("Total points: " + str(total))
print("Average exam score: " + str(avg))