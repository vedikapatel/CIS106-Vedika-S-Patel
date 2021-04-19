prog = input("Do you want to do this program? (Y or N) ")
while prog == "Y":
  lastName = input("Enter your last name: ")
  exam1 = float(input("Enter exam 1 score: "))
  exam2 = float(input("Enter exam 2 score: "))
  avg = (exam1 + exam2) / 2
  print(avg)
  prog = input("Do you want to do this program? (Y or N) ")
