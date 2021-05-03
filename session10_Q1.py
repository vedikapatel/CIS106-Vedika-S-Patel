def printArray (arr):
  for x in range(10):
    print(arr[x])
    print(x)

def revArray (arr):
  for x in range(9, -1, -1):
    print(arr[x]) 
lastName = ["Patel", "Garcia", "Farag", "Elezi", "Gonzalez", "Mejia", "Aviles", "Guzman", "Nowak","Carbajal"]


print("Last name in forward order:")
printArray(lastName)
print()
print("Last name in reverse order:")
revArray(lastName)