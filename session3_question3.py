ItemPrice = 0.0
Discount = 0.0
DiscountPrice = 0.0
Total = 0.0
ItemPrice = float(input("Enter the price of item: "))
Discount = float(input("Enter the discount percent: "))
DiscountPrice = ((ItemPrice*Discount)/100)
Total = (ItemPrice-DiscountPrice)
print("Discount amount $" + str(DiscountPrice))
print("Total is $" + str(Total))
