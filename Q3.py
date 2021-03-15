numbook = int(input("Enter the number of books to order: "))
cost = float(input("Enter the cost per book: "))
order = numbook*cost
if order > 50:
  shipping = 0
else:
  shipping = 25
print("Order Total $" + str(order))
print("Shipping $" + str(shipping))