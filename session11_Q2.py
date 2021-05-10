list = []
item = int(input("Enter the number of items in list: "))
print("Enter numbers")
for i in range (item):
  data = int(input())
  list.append(data)
list.insert(1, 99)
print("List of numbers:", list)