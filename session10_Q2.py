def printArray (arr, examScore):

  for x in range(10):
    print(arr[x])
    print(examScore[x])

lastName = ["Patel", "Garcia", "Farag", "Elezi", "Gonzalez", "Mejia", "Aviles", "Guzman", "Nowak","Carbajal"]
examScore = [70, 60, 87, 89, 74, 99, 79, 85, 59, 66]


print("Last name with exam score below:")
printArray(lastName, examScore)