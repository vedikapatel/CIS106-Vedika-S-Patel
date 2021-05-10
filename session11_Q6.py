list1 = []
list2 = [500, 600, 700, 800, 900]
print("Second list of numbers:", list2)
item = int(input("Enter the number of items in list: "))
print("Enter numbers")
for i in range (item):
  data = int(input())
  list1.append(data)
list1.pop(2)
list1.extend(list2)
print("List of numbers:", list1)
