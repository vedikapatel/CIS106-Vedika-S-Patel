# def printArray (arr, examScore):

#   for x in range(10):
#     print(arr[x])
#     print(examScore[x])
# [2,1,1,5]

def max(array):
  maximum = array[0]
  maxPos = 0 
  for index in range(1, len(array)):
    if maximum < array[index]:
      maximum = array[index]
      maxPos = index

  return maximum, maxPos

def min(array):
  minimum = array[0]
  minPos = 0
  for index in range(1, len(array)):
    if minimum > array[index]:
      minimum = array[index]
      minPos = index
  return minimum, minPos

def sum(array):
    total = 0
    for index in range(len(array)):
        total += array[index]
    return total


lastName = ["Patel", "Garcia", "Farag", "Elezi", "Gonzalez", "Mejia", "Aviles", "Guzman", "Nowak","Carbajal"]
examScore = [70, 60, 87, 89, 74, 99, 79, 85, 59, 66]

maxScore, maxPos = max(examScore)
lastName[maxPos]
print ("Maximum score for:", lastName[maxPos], "is", maxScore)
minScore,minPos = min(examScore)
print ("Minimum score for:", lastName[minPos], "is", minScore)
sumScore = sum(examScore)
print("Average score is:", sumScore/len(examScore))